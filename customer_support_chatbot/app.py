from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


app = Flask(__name__)

# Step 1: Updated predefined questions and answers (Add more here)
qa_pairs = {
    "What is your refund policy?": "Our refund policy allows you to return products within 30 days for a full refund.",
    "How can I track my order?": "You can track your order by logging into your account and visiting the 'Orders' section.",
    "What are your working hours?": "We are available from 9 AM to 6 PM, Monday to Friday.",
    "How can I contact customer support?": "You can contact customer support by emailing support@company.com or calling 1-800-123-4567.",
    "Where are you located?": "Our office is located at 123 Main Street, Cityville, Country.",
    "Can I change my shipping address?": "Yes, you can update your shipping address before your order is shipped. Please contact support immediately.",
    "How do I return a product?": "You can return a product by visiting our Returns page or contacting customer support.",
    "What payment methods do you accept?": "We accept credit cards, debit cards, PayPal, and bank transfers.",
    "Do you offer gift cards?": "Yes, we offer gift cards for various amounts. You can purchase them on our website."
}

# Step 2: Create the TF-IDF Vectorizer and retrain it on the updated questions
vectorizer = TfidfVectorizer()
predefined_questions = list(qa_pairs.keys())
tfidf_matrix = vectorizer.fit_transform(predefined_questions)

# Step 3: Function to get the response based on user query
def get_ml_response(user_query):
    query_tfidf = vectorizer.transform([user_query])
    similarity = cosine_similarity(query_tfidf, tfidf_matrix)
    
    most_similar_idx = similarity.argmax()
    if similarity[0][most_similar_idx] < 0.5:  # Threshold to determine low similarity
        return "I'm sorry, I couldn't understand your question. Can you please rephrase it?"
    response = qa_pairs[predefined_questions[most_similar_idx]]
    return response

    
    # Find the index of the most similar predefined question
    most_similar_idx = similarity.argmax()
    response = qa_pairs[predefined_questions[most_similar_idx]]
    
    return response

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    user_query = request.form['query']
    
    # Step 4: Get the response from the ML-based model (TF-IDF approach)
    response = get_ml_response(user_query)
    
    return render_template('index.html', user_query=user_query, response=response)

if __name__ == '__main__':
    app.run(debug=True)
