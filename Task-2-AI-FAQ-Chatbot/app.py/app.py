import streamlit as st
import string
from faqs import faqs
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

questions = list(faqs.keys())
answers = list(faqs.values())

processed_questions = [preprocess(q) for q in questions]

vectorizer = TfidfVectorizer(stop_words="english")
question_vectors = vectorizer.fit_transform(processed_questions)

def chatbot_response(user_input):
    user_input = preprocess(user_input)
    user_vector = vectorizer.transform([user_input])

    similarity_scores = cosine_similarity(user_vector, question_vectors)
    best_match = similarity_scores.argmax()
    confidence_score = similarity_scores[0][best_match]

    if confidence_score > 0.3:
        return answers[best_match]
    else:
        return "Sorry, I could not find a relevant answer to your question."

st.set_page_config(page_title="CodeAlpha FAQ Chatbot", page_icon="🤖")
st.title("🤖 CodeAlpha FAQ Chatbot")

user_query = st.text_input("Ask your question:")

if st.button("Get Answer"):
    if user_query.strip():
        st.success(chatbot_response(user_query))
    else:
        st.warning("Please enter a valid question.")
