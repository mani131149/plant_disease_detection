# Plant Leaf Disease Detection System 🌱

A Flask-based web application that uses a machine learning model to detect plant leaf diseases, helping users identify and manage plant health effectively.

---

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Technology Stack](#technology-stack)
4. [Setup and Installation](#setup-and-installation)
5. [Usage](#usage)
6. [Project Structure](#project-structure)
7. [Future Enhancements](#future-enhancements)
8. [Contributors](#contributors)

---

## Introduction
The Plant Leaf Disease Detection System is designed to assist farmers and gardeners in identifying common plant leaf diseases. Users can upload leaf images, and the system predicts whether the leaf is healthy or has diseases like Powdery or Rust. Additionally, it provides actionable recommendations for disease treatment.

---

## Features
- **User Authentication**: Registration, login, and logout functionalities.
- **Image Upload**: Users can upload leaf images for disease prediction.
- **Real-Time Predictions**: The system uses a pre-trained machine learning model to classify diseases.
- **Personalized Results**: Users can view only their own prediction history.
- **Support Page**: Offers detailed guidance on treating detected diseases.

---

## Technology Stack
- **Backend**: Flask
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning**: TensorFlow/Keras
- **Data Preprocessing**: ImageDataGenerator
- **Model**: Convolutional Neural Network (CNN)
- **Storage**: JSON for user data and session management

---

## Setup and Installation

### Prerequisites
- Python 3.8 or higher
- TensorFlow/Keras
- Flask and other dependencies (specified in `requirements.txt`)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/plant-leaf-disease-detection.git
   cd plant-leaf-disease-detection
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the dataset and pre-trained model:
   - Place the dataset in the `/archive` folder.
   - Place the `model.h5` file in the root directory.

4. Run the application:
   ```bash
   python app.py
   ```

5. Access the application at:
   ```
   http://127.0.0.1:5000/
   ```

---

## Usage
1. **Register** as a new user or **login** with existing credentials.
2. Navigate to the **Upload Image** page to upload a plant leaf image.
3. View the prediction on the **Results Page**.
4. Visit the **Support Page** for disease-specific recommendations.
5. **Logout** securely to end your session.

---

## Project Structure
```
plant-leaf-disease-detection/
├── static/                  # Static assets (images, CSS, JS)
├── templates/               # HTML templates
├── archive/                 # Dataset folder
├── app.py                   # Main Flask application
├── model.h5                 # Pre-trained ML model
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation

---

## Future Enhancements
- Add support for more diseases and plant types.
- Integrate multilingual support for global accessibility.
- Create a mobile-friendly design.
- Add treatment recommendations based on location-specific resources.

---

## Contributors
- **SaiTeja** (Project Lead)
- **Manikanta** (Frontend Developer)
- **Ketan** (Machine Learning Engineer)
- **Raghu** (Backend Developer)
- **Vishnu_Priya** (UI/UX Designer)

---
