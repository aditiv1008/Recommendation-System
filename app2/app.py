from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

# Define the path to the data folder
data_path = 'data'

@app.route('/')
def index():
    # List all users
    users = [user for user in os.listdir(data_path) if os.path.isdir(os.path.join(data_path, user))]
    return render_template('index.html', users=users)

@app.route('/user/<username>')
def user_page(username):
    # Load user data
    user_data_path = os.path.join(data_path, username)
    books_read_df = pd.read_csv(os.path.join(user_data_path, 'books_read.csv'))
    recommended_books_df = pd.read_csv(os.path.join(user_data_path, 'books_rec.csv'))

    # Render the HTML template with the user data
    return render_template('user_page.html', username=username, books_read=books_read_df, recommended_books=recommended_books_df)
    

if __name__ == '__main__':
    app.run(debug=True)