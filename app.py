import streamlit as st
import numpy as np 
import pickle

def load_data():
    books = pickle.load(open('pickle/book_names.pkl', 'rb'))
    rating = pickle.load(open('pickle/final_rating.pkl', 'rb'))
    pivot_table = pickle.load(open('pickle/book_pivot.pkl', 'rb'))
    model = pickle.load(open('pickle/model.pkl', 'rb'))
    return books, rating, pivot_table, model

def create_image(suggestion, rating):
    urls = [rating.iloc[np.where(rating['Title'] == book)[0][0]]['img_url'] for book in suggestion]
    return urls

def recommend_book(book, pivot_table, model, rating):
    book_index = np.where(pivot_table.index == book)[0][0]
    _, recommendation = model.kneighbors(pivot_table.iloc[book_index, :].values.reshape(1, -1), n_neighbors=6)
    recommended_books = pivot_table.index[recommendation.flatten()]
    posters = create_image(recommended_books, rating)

    return recommended_books, posters

def main():
    st.header("Book Recommendation System")

    books, rating, pivot_table, model = load_data()

    selected_book = st.selectbox("Select a book you want recommendations for", books)

    if st.button('Generate Recommendations'): 
        recommendations, posters = recommend_book(selected_book, pivot_table, model, rating)

        cols = st.columns(5)
        for col, (book, poster) in zip(cols, zip(recommendations[1:], posters[1:])):
            col.text(book)
            col.image(poster)

if __name__ == "__main__":
    main()
