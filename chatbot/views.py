import json
import re
from pathlib import Path

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load the FAQ dataset
FAQ_FILE = Path(__file__).parent / "faq_data.json"

with open(FAQ_FILE, "r", encoding="utf-8") as file:
    FAQS = json.load(file)


# Initialize the NLP stemmer
stemmer = PorterStemmer()


# Preprocess text
def preprocess(text):
    words = re.findall(r"[a-zA-Z0-9']+", text.lower())

    stemmed_words = [
        stemmer.stem(word) for word in words
    ]

    return " ".join(stemmed_words)


# Prepare FAQ questions for similarity matching
questions = [
    faq["question"] for faq in FAQS
]

vectorizer = TfidfVectorizer(
    preprocessor=preprocess,
    token_pattern=r"(?u)\b\w+\b",
    ngram_range=(1, 2)
)

question_vectors = vectorizer.fit_transform(questions)


# Display the chatbot webpage
def home(request):
    return render(
        request,
        "chatbot/index.html",
        {"faqs": questions[:6]}
    )


# Handle chatbot questions
def chat(request):
    if request.method != "POST":
        return JsonResponse(
            {"answer": "Only POST requests are allowed."},
            status=405
        )

    try:
        data = json.loads(request.body)
        user_question = data.get("message", "").strip()

        if not user_question:
            return JsonResponse({
                "answer": "Please enter a question.",
                "matched_question": None
            })

        # Convert user question into a vector
        user_vector = vectorizer.transform(
            [user_question]
        )

        # Calculate similarity scores
        scores = cosine_similarity(
            user_vector,
            question_vectors
        ).flatten()

        best_index = int(scores.argmax())
        best_score = float(scores[best_index])

        # Return fallback for unrelated questions
        if best_score < 0.18:
            return JsonResponse({
                "answer": (
                    "Sorry, I couldn't find a matching FAQ. "
                    "Please ask about Python, HTML, CSS, "
                    "Django, AI, NLP, or internships."
                ),
                "matched_question": None
            })

        # Return the closest matching answer
        return JsonResponse({
            "answer": FAQS[best_index]["answer"],
            "matched_question": FAQS[best_index]["question"]
        })

    except (json.JSONDecodeError, AttributeError):
        return JsonResponse({
            "answer": "Invalid request. Please try again."
        }, status=400)