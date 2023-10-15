# Book Recommendation Website

A simple yet effective book recommendation website built with Flask and styled with Bootstrap. The site displays a list of the top 50 books from the database and provides a feature for users to input a book name and receive a list of top 5 similar or recommended books.

## Features

- Display of top 50 books from the database.
- A search field to input a book name and get a list of top 5 similar or recommended books.
- Responsive design thanks to Bootstrap.

## Technologies Used

- Flask (Backend)
- Bootstrap (Frontend)
- SQL (Database)

## Setup and Installation

1. **Clone the Repository**:
    - Clone the repository to your local machine using the following command:
    ```bash
    git clone https://github.com/farneet24/Book-Recommendation.git
    cd Book-Recommendation
    ```

2. **Install Dependencies**:
    - It's recommended to create a virtual environment to manage dependencies for this project.
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```
    - Install the required packages using pip:
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure the Database**:
    - Ensure you have a SQL server running.
    - Create a database and update the database configuration settings in `config.py` with your database credentials.

4. **Initialize the Database**:
    - Run the following command to initialize the database with the necessary tables and data:
    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

5. **Run the Application**:
    - Now that everything is set up, run the application using the following command:
    ```bash
    flask run
    ```

6. **Access the Application**:
    - Open your web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to access the application.

7. **(Optional) Customize**:
    - Feel free to customize the application by modifying the templates, adding new features, or styling with additional CSS.

