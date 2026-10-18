import os
import json
import string
import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Store NLTK data inside project directory to avoid folder-permission warnings
nltk_data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "nltk_data")
os.makedirs(nltk_data_dir, exist_ok=True)
nltk.data.path.append(nltk_data_dir)

# Download all required corpora including 'punkt_tab'
for package in ['punkt', 'punkt_tab', 'stopwords', 'wordnet']:
    nltk.download(package, download_dir=nltk_data_dir, quiet=True)



# Page configuration
st.set_page_config(page_title="FAQ Chatbot", page_icon="🤖", layout="centered")

st.title("🤖 Customer Support FAQ Chatbot")
st.write("Ask any questions about orders, shipping, returns, or payments.")

# Load FAQ dataset
@st.cache_data
def load_faq_data():
    with open("faqs.json", "r", encoding="utf-8") as f:
        return json.load(f)

faqs = load_faq_data()
faq_questions = [item["question"] for item in faqs]
faq_answers = [item["answer"] for item in faqs]

# Text preprocessing function
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    tokens = word_tokenize(text)
    cleaned_tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]
    return " ".join(cleaned_tokens)

# Preprocess all FAQ questions
preprocessed_faqs = [preprocess_text(q) for q in faq_questions]

# Vectorize FAQ questions
vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(preprocessed_faqs)

def get_best_faq_response(user_query, threshold=0.25):
    cleaned_query = preprocess_text(user_query)
    if not cleaned_query.strip():
        return "I couldn't quite understand that. Could you please rephrase your question?"

    # Vectorize user query and compute cosine similarity
    query_vector = vectorizer.transform([cleaned_query])
    similarity_scores = cosine_similarity(query_vector, faq_vectors).flatten()

    best_index = similarity_scores.argmax()
    best_score = similarity_scores[best_index]

    if best_score >= threshold:
        return faq_answers[best_index]
    else:
        return "I'm sorry, I don't have information on that topic. Please contact our support team at support@example.com."

# Initialize chat message history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am your FAQ assistant. How can I assist you today?"}
    ]

# Display conversation history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input prompt
if user_prompt := st.chat_input("Type your question here..."):
    # Render user query
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.write(user_prompt)

    # Generate and display bot response
    bot_reply = get_best_faq_response(user_prompt)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.write(bot_reply)
