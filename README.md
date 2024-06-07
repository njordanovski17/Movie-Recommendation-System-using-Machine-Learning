Movie Recommendation System using Machine Learning

Introduction

The movie industry has grown exponentially, resulting in an overwhelming number of movies available for viewers. To help users navigate this vast selection, a movie recommendation system can be invaluable. This report details the development and implementation of a movie recommendation system using machine learning. The project utilizes several key resources, including pandas for data manipulation, sklearn for machine learning algorithms, Streamlit for the user interface, and pickle for model serialization.
Resources and Libraries
Pandas

Pandas is a powerful data manipulation library in Python. It provides data structures and functions needed to manipulate structured data seamlessly.
•	Data Loading: Reading datasets containing movie information and user ratings.
•	Data Cleaning: Handling missing values, duplicates, and ensuring data consistency.
•	Data Transformation: Manipulating and preparing data for the machine learning model.
Sklearn

Sklearn, or Scikit-Learn, is a machine learning library for Python. It features various classification, regression, and clustering algorithms.

•	Model Selection: Choosing the right machine learning algorithm for recommendations.
•	Data Splitting: Dividing the data into training and testing sets.
•	Model Training: Training the model on the dataset.
•	Model Evaluation: Assessing the performance of the model using appropriate metrics.
Streamlit

Streamlit is an open-source app framework in Python for creating beautiful, interactive web applications.

•	Interface Design: Creating a user-friendly web interface to interact with the recommendation system.
•	Interactivity: Allowing users to input their preferences and get real-time recommendations.

Pickle

Pickle is a Python module used to serialize and deserialize Python object structures.

•	Model Serialization: Saving the trained machine learning model to disk.
•	Model Deserialization: Loading the model from disk for making predictions.

Dataset used:
- https://www.kaggle.com/datasets/ahsanaseer/top-rated-tmdb-movies-10k

How to run the program:
1. Make sure all of the above mentioned libraries are installed
2. Load all the files through VScode
3. In the program.py file, open the terminal and type the command: streamlit run program.py
4. A browser should open with the program working.
