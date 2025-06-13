# 📝 Sentiment Analysis Web App

This project builds a **Flask-based** NLP & Machine Learning web application for analyzing text sentiment. Users can input sentences and receive real-time classifications as **positive** or **negative**.

## 🚀 Features

- 🧹 **Text Preprocessing**: Includes tokenization, stop-word removal, and lemmatization.
- 🔍 **Feature Extraction**: Converts text into TF-IDF vectors for model input.
- 🤖 **Sentiment Classification**: Utilizes a trained ML model (e.g., Logistic Regression or Naive Bayes).
- 🌐 **Flask Frontend**: Clean interface for text input and live sentiment results.
- 🧠 **Model Persistence**: Model and vectorizer stored via pickle for easy reuse.
- 📊 **Evaluation & Analysis**: Training and evaluation performed in Jupyter Notebook.

## 🗂️ Project Structure
Sentiment-Analysis/
├── app.py # Flask web application
├── sentiment_analysis.ipynb # Data preprocessing, model training & evaluation
├── model.pkl # Serialized ML model + vectorizer
├── requirements.txt # Python dependencies
├── templates/ & static/ # HTML, CSS for front-end
├── README.md # This documentation file
└── LICENSE # MIT License

## ⚙️ Setup Instructions

### 🔄 Clone the Repository
```
git clone https://github.com/AaryaMehta2506/Sentiment-Analysis.git
cd Sentiment-Analysis
```
### 🧪 Create & Activate Virtual Env
```
python -m venv env
source env/bin/activate       # Windows: env\Scripts\activate
```
### 📦 Install Dependencies
```
pip install -r requirements.txt
```
### 🚀 Run the Flask App
```
python app.py
```

Access the app at http://127.0.0.1:5000/ to input text and see sentiment predictions.

## 📊 Model Training & Evaluation
To retrain the model or view its performance:

Open sentiment_analysis.ipynb in Jupyter or Colab.

Follow steps for cleaning, TF-IDF vectorization, model training, and model evaluation.

Serialize your trained model and vectorizer as model.pkl.

## 💡 Example Use Cases
Input: "I absolutely love this!"
Output: 🚀 Positive

Input: "This was a disappointing experience."
Output: 😞 Negative

## 🤝 Contributing
Contributions are welcome! Here’s how you can help:

Fork the repository

Create a new branch:
```
git checkout -b feature-name
```
Make your changes and commit them:
```
git commit -m "Add feature XYZ"
```
Push and open a Pull Request

## 📄 License
This project is licensed under the [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)

## 👩‍💻 Author

**Aarya Mehta**  
🔗 [GitHub Profile](https://github.com/AaryaMehta2506)

