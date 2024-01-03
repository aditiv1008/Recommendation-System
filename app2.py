# Importing RecommendationModel from User-Based.ipynb

import pandas as pd
import numpy as np
import streamlit as st
from user_recommendation import PersonalizedRecommender, recommend_books, main
#from tensorflow.keras.models import load_model

# Assuming RecommendationModel is defined in the same way as in User-Based.ipynb
model = RecommendationModel(num_users, num_book_titles, embedding_size=50)

# Placeholder paths, replace these with the actual paths to your data
users_data_path = 'data/Users.csv'
books_data_path = 'data/Books.csv'

# Load user data
users_df = pd.read_csv(users_data_path)

# Load book data
books_df = pd.read_csv(books_data_path)

# User encoding
unique_user_ids = users_df['User-ID'].unique()
user_to_user_encoded = {user_id: index for index, user_id in enumerate(unique_user_ids)}

# Reverse user encoding
user_encoded_to_user = {index: user_id for index, user_id in enumerate(unique_user_ids)}

# ISBN encoding
unique_isbns = books_df['ISBN'].unique()
isbn_to_isbn_encoded = {isbn: index for index, isbn in enumerate(unique_isbns)}

# Reverse ISBN encoding
isbn_encoded_to_isbn = {index: isbn for index, isbn in enumerate(unique_isbns)}

# Function to recommend books for a given user
def recommend_books(user_id):
    # Placeholder logic, replace these with your actual data processing and recommendation logic
    books_read_by_user = []  # Replace this with the actual list of books read by the user
    book_not_read = []  # Replace this with the actual list of books not read by the user

    # Avoid SettingWithCopyWarning by creating a copy
    final_ratings_df = final_ratings_df.copy()
    final_ratings_df['user'] = final_ratings_df['User-ID'].map(encoded_user)
    final_ratings_df['book_title'] = final_ratings_df['ISBN'].map(isbn_to_isbn_encoded)

    # Additional processing...

    book_not_read = [[isbn_to_isbn_encoded.get(x)] for x in book_not_read]
    user_encoder = user_to_user_encoded.get(user_id)
    user_book_array = np.hstack(
        ([[user_encoder]] * len(book_not_read), book_not_read)
    )
    ratings_model = model.predict(user_book_array).flatten()

    top_ratings_indices = ratings_model.argsort()[-10:][::-1]

    recommended_book_ids = [
        isbn_encoded_to_isbn.get(book_not_read[x][0]) for x in top_ratings_indices
    ]

    return recommended_book_ids


def main():
    st.title("Book Recommendation System")

    # Get user input
    user_id = st.number_input("Enter User ID", min_value=1, max_value=10000, step=1)

    # Display recommendations when the user clicks the button
    if st.button("Get Recommendations"):
        recommendations = recommend_books(user_id)

        # Display recommended books
        st.subheader("Recommended Books:")
        for book_id in recommendations:
            st.write(f"- Book ID: {book_id}")

if __name__ == "__main__":
    main()