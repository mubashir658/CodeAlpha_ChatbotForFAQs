# CodeAlpha FAQ Chatbot

An intelligent customer support FAQ chatbot built with Python, NLTK, scikit-learn, and Streamlit. This project was developed as part of the CodeAlpha Artificial Intelligence Internship program.

## Overview

The chatbot reads questions from a FAQ dataset, preprocesses the text, converts it into a vector representation, and matches the user input with the most relevant answer using TF-IDF and cosine similarity.

## Features

- Natural language preprocessing with NLTK
  - tokenization
  - stopword removal
  - lemmatization
- TF-IDF vectorization for text similarity
- Cosine similarity matching for accurate FAQ retrieval
- Interactive chat interface built with Streamlit
- Easy-to-edit JSON knowledge base for different FAQ domains

## Project Structure

- `app.py` — main Streamlit app
- `faqs.json` — FAQ dataset
- `requirements.txt` — project dependencies
- `nltk_data/` — NLTK data files
- `.gitignore` — ignored files
- `README.md` — project documentation

## Setup and Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mubashir658/CodeAlpha_ChatbotForFAQs.git
   cd CodeAlpha_ChatbotForFAQs
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   streamlit run app.py
   ```

5. Verify the project files:

   ```bash
   ls -a
   ```

   You should see files such as:
   - `app.py`
   - `requirements.txt`
   - `.gitignore`
   - `README.md`
   - `faqs.json`

## Usage

- Start the app with Streamlit.
- Enter a question in the chat interface.
- The chatbot will match your question with the closest FAQ and return the most relevant answer.
- You can update or expand the data in `faqs.json` to customize the chatbot for different use cases.

## Requirements

- Python 3.x
- NLTK
- scikit-learn
- Streamlit

## Notes

This project is a straightforward FAQ-based chatbot and can be extended with features such as:

- intent recognition
- database-backed FAQs
- multilingual support
- API integration for live customer support systems
