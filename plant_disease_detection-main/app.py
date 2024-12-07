import os
import random
import json
import threading
import time
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
from flask import Flask, request, render_template, redirect, url_for, session, flash, jsonify
from werkzeug.utils import secure_filename

# Flask application setup
app = Flask(__name__)
app.secret_key = 'your_secret_key'

# File path for storing user data
USER_DATA_FILE = 'users.json'

# Load users from file or initialize an empty dictionary
if os.path.exists(USER_DATA_FILE):
    try:
        with open(USER_DATA_FILE, 'r') as file:
            users = json.load(file)
    except json.JSONDecodeError:
        users = {}  # Initialize as empty if the file is invalid
else:
    users = {}

# Save users to file
def save_users():
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(users, file)

# In-memory storage for predictions
results = []

# Load model
model = load_model('C:/Users/manik/Downloads/plant_disease_detection-main/plant_disease_detection-main/model.h5', compile=False)
print('Model loaded. Access the app at http://127.0.0.1:5000/')

# Labels for predictions
labels = {
    0: 'Healthy',
    1: 'Powdery - Requires treatment to prevent spreading.',
    2: 'Rust - Requires immediate care and treatment.'
}

# Helper function for predictions
def getResult(image_path):
    img = load_img(image_path, target_size=(225, 225))
    x = img_to_array(img) / 255.0
    x = np.expand_dims(x, axis=0)
    predictions = model.predict(x)
    return predictions

# Main Prediction Page
@app.route('/')
def home():
    # Ensure user is logged in before showing the home page
    if not session.get('logged_in', False):
        return redirect(url_for('login'))
    return render_template('index.html')

# Results Page setup
@app.route('/results', methods=['GET'])
def results_page():
    # Ensure user is logged in before showing the results page
    if not session.get('logged_in', False):
        return redirect(url_for('login'))

    return render_template('results.html', results=results)

# Support page route
@app.route('/support')
def support_page():
    # Ensure user is logged in before showing the support page
    if not session.get('logged_in', False):
        return redirect(url_for('login'))
    support_info = {
        "Healthy": "This plant is healthy and requires no special care.",
        "Powdery": "This plant has Powdery disease. Apply a fungicide to prevent spreading.",
        "Rust": "This plant has Rust disease. Immediate treatment is necessary."
    }
    return render_template('support.html', support=support_info)

# Route for uploading images
@app.route('/predict', methods=['GET'])
def show_predict_page():
    # Render the page where the user can upload an image
    if not session.get('logged_in', False):
        return redirect(url_for('login'))
    return render_template('predict.html')

# Route for handling image uploads

@app.route('/predict', methods=['POST'])
def predict():
    # Handle the prediction logic when a file is uploaded
    if not session.get('logged_in', False):
        return jsonify({'error': 'Unauthorized'}), 401

    if 'file' not in request.files:
        return jsonify({'error': 'No file selected'}), 400

    f = request.files['file']
    if f.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if not f.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        return jsonify({'error': 'Unsupported file type. Please upload a PNG, JPG, or JPEG image.'}), 400

    upload_dir = os.path.join(os.path.dirname(__file__), 'static', 'uploads')
    os.makedirs(upload_dir, exist_ok=True)
    file_path = os.path.join(upload_dir, secure_filename(f.filename))
    f.save(file_path)

    try:
        predictions = getResult(file_path)
        predicted_label = labels[np.argmax(predictions)]

        image_url = url_for('static', filename=f'uploads/{secure_filename(f.filename)}')

        # Append the result to the global results list
        results.append({
            'file_name': f.filename,
            'image_url': image_url,
            'prediction': predicted_label
        })

        return jsonify({'result': predicted_label, 'image_url': image_url})
    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({'error': 'An error occurred during prediction. Please try again.'}), 500


# Registration Page route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if username in users:
            flash('Username already taken!', 'danger')
            return redirect(url_for('register'))

        if password != confirm_password:
            flash('Passwords do not match!', 'danger')
            return redirect(url_for('register'))

        # Save user in memory and persist to file
        users[username] = password
        save_users()

        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

# Login Page route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['logged_in'] = True
            session['username'] = username
            session['results'] = []
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password.', 'danger')
    return render_template('login.html')

#Logout Page
@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
