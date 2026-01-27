🤖 FAQ Chatbot using Streamlit

CodeAlpha Internship – Task 2

📌 Description

This project is a FAQ Chatbot developed as part of Task 2 of the CodeAlpha Internship.
The chatbot answers user questions by matching them with predefined FAQs using TF-IDF vectorization and Cosine Similarity.
The application is built using Python and Streamlit.

🛠️ Technologies Used

Python
Streamlit
Scikit-learn

📂 Project Structure
├── app.py              # Main Streamlit application
├── faqs.py             # Contains FAQ questions and answers
├── utils.py            # Utility functions for preprocessing and similarity logic
├── requirements.txt    # Required dependencies
└── README.md           # Project documentation

⚙️ How It Works

FAQ questions are stored in faqs.py.

Text is preprocessed by:
Converting to lowercase
Removing punctuation
Questions are converted into vectors using TF-IDF Vectorizer.
User input is compared with stored questions using Cosine Similarity.
If similarity score is greater than 0.3, the best matching answer is returned.
Otherwise, a default response is shown.

▶️ How to Run

Install required libraries:

pip install -r requirements.txt

Run the Streamlit app:

streamlit run app.py

🧪 Sample Output

User: What is CodeAlpha?
Bot: CodeAlpha is an internship platform that provides real-world project experience.

✅ Features

Simple and interactive chatbot
Accurate FAQ matching
Handles unknown queries gracefully
Beginner-friendly implementation

📌 Internship Details

Organization: CodeAlpha

Task: Task 2 – FAQ Chatbot

Domain: Artificial Intelligence

🙏 Acknowledgement

I would like to thank CodeAlpha for providing this internship opportunity and guidance.


