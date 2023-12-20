# main_app.py
from flask import Flask, render_template, request
from my_search_engine import MySearchEngine  # Import your search engine class

import nltk

print("Before NLTK download")

# Set NLTK data path
nltk.data.path.append("nltk_data")

nltk.download('stopwords', download_dir='nltk_data')
nltk.download('punkt', download_dir='nltk_data')
nltk.download('wordnet', download_dir='nltk_data')

print("After NLTK download")



app = Flask(__name__)
search_engine = MySearchEngine()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        suggestions = search_engine.extract_suggestions(user_input)
        tfidf_scores = search_engine.extract_tfidf_scores(user_input)  # this line to get TF-IDF scores
        # keywords = search_engine.extract_keywords()
        return render_template('index.html', suggestions=suggestions, user_input=user_input, tfidf_scores=tfidf_scores) #keywords=keywords,
    return render_template('index.html', suggestions=[], tfidf_scores=[]) #, keywords=[]

@app.route('/keywords', methods=['POST', 'GET'])
def keywords():
    if request.method == 'POST':
        keywords = search_engine.extract_keywords()
        return render_template('index.html', keywords=keywords)
    return render_template('index.html', suggestions=[], keywords=[], tfidf_scores=[])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
    # app.run(debug=False)