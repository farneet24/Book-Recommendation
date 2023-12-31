from flask import Flask, render_template, request
import numpy as np
from itertools import chain
import pickle

popular_df = pickle.load(open('popular.pkl','rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_Score = pickle.load(open('similarity_Score.pkl', 'rb'))
app = Flask(__name__)

@app.route('/')
def index():
    # We will send the information from the popular_df to the index.html
    return render_template('index.html', book_name = list(popular_df['Book-Title'].values),
                           author = list(popular_df['Book-Author'].values),
                           image = list(popular_df['Image-URL-M'].values),
                           votes = list(popular_df['Book-Rating'].values),
                           rating = list(popular_df['Average-Rating'].values.round(1)))

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')
    index = np.where(pt.index == user_input)[0][0]
    distances = similarity_Score[index]
    similar_items = sorted(list(enumerate(distances)), key=lambda x:x[1], reverse=True)[1:6] # 5 items
    
    data = []
    
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.append(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.append(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.append(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        flatten_list = list(chain.from_iterable(item))
        data.append(flatten_list)

    return render_template('recommend.html', data=data)
if __name__ == '__main__':
    app.run(debug = False)