# 🤖 DevHelp - FAQ Chatbot

An NLP-based FAQ chatbot developed using Django, Python, NLTK, and scikit-learn as part of the CodeAlpha Artificial Intelligence Internship.

## ✨ Features

- Interactive chatbot web interface
- FAQ dataset containing common questions and answers
- Text preprocessing using NLTK
- TF-IDF vectorization for text representation
- Cosine similarity for matching user questions
- Automatic responses based on the closest matching FAQ
- Fallback response for unrelated questions
- Responsive interface using HTML and CSS

## 🛠️ Technologies Used

- Python
- Django
- NLTK
- scikit-learn
- HTML
- CSS
- JavaScript
- JSON

## 📁 Project Structure

CodeAlpha_FAQChatbot/
├── manage.py
├── config/
│   ├── settings.py
│   └── urls.py
├── chatbot/
│   ├── views.py
│   ├── urls.py
│   ├── faq_data.json
│   ├── templates/
│   │   └── chatbot/
│   │       └── index.html
│   └── static/
│       └── chatbot/
│           └── style.css
├── .gitignore
└── README.md
## ⚙️ Installation and Setup

### 1. Clone the repository

git clone https://github.com/YOUR_USERNAME/CodeAlpha_FAQChatbot.git
Replace YOUR_USERNAME with your GitHub username.

### 2. Open the project folder

cd CodeAlpha_FAQChatbot
### 3. Install dependencies

python -m pip install django nltk scikit-learn
### 4. Run database migrations

python manage.py migrate
### 5. Start the development server

python manage.py runserver
### 6. Open the application

Visit http://127.0.0.1:8000/ in your browser.

## 🧠 How It Works

1. The user enters a question in the chatbot interface.
2. NLTK's Porter Stemmer preprocesses the text.
3. TF-IDF converts questions into numerical vectors.
4. Cosine similarity compares the user's question with the FAQ dataset.
5. The chatbot returns the closest matching answer if its similarity score meets the configured threshold.
6. If no sufficiently close match is found, the chatbot displays a fallback response.

## 🎯 Project Objective

The objective of this project is to demonstrate natural language processing, text preprocessing, similarity matching, and web application development through a simple FAQ chatbot.

## 👩‍💻 Internship

Developed as Task 2 for the CodeAlpha Artificial Intelligence Internship.

## 📌 Future Improvements

- Expand the FAQ dataset
- Add conversation history
- Improve question matching
- Add support for more topics
- Deploy the application online

## 📄 License

This project was created for educational and internship purposes.