🧠 Sentiment Analysis on Customer Reviews
This project applies Deep Learning and Natural Language Processing (NLP) techniques to classify customer reviews as Positive or Negative in real time. It features a Flask-based web interface and is developed using Keras, TensorFlow, and Jupyter Notebook for easy experimentation and visualization.

🚀 Features
🧠 Sentiment Classification: Predicts whether the input text conveys a positive or negative sentiment.

🌐 Flask Web Interface: Simple and interactive web app for users to input reviews and view results instantly.

🤖 Deep Learning Model: Built with Keras and trained on labeled review data.

📊 Visualization & Metrics: Development and evaluation done in Jupyter Notebook with insights into model performance.

🧪 Realtime Prediction: Instant feedback from the web interface using a trained model.

🛠️ Technologies Used
Python: Core programming language

Flask: Web framework for the interactive UI

Keras: Deep learning library to build and train the model

TensorFlow: Backend for Keras to execute deep learning operations

Jupyter Notebook: For model training, visualization, and evaluation

Pandas & NumPy: For data manipulation and preprocessing

🗂️ Project Structure

Sentiment-Analysis/
├── sentiment_model.h5                 # Trained Keras model
├── app.py                             # Flask web application
├── Sentiment_Analysis_Notebook.ipynb # Jupyter notebook for model training & testing
├── data/                              # Dataset folder with labeled reviews
├── requirements.txt                   # Python dependencies
├── README.md                          # Project documentation
├── static/ & templates/               # HTML/CSS/JS for the Flask app
└── LICENSE                            # MIT License

⚙️ Setup Instructions
🔄 Clone the Repository

git clone https://github.com/your-username/Sentiment-Analysis.git
cd Sentiment-Analysis
🧪 Create and Activate Virtual Environment (Recommended)

python -m venv env
source env/bin/activate     # On Windows: env\Scripts\activate
📦 Install Required Packages
bash
Copy
Edit
pip install -r requirements.txt
🚀 Run the Flask App
bash
Copy
Edit
python app.py
Then, open your browser and go to: http://127.0.0.1:5000/

📊 Model Training & Evaluation
To retrain the model or explore how it works:

Open Sentiment_Analysis_Notebook.ipynb in Jupyter Notebook or Google Colab.

Follow the steps for:

Data loading & cleaning

Tokenization and preprocessing

Model creation using Keras

Training and evaluation

Save the trained model as sentiment_model.h5.

💡 Example Use Case
Input Review	Output
"I absolutely love this product!"	Positive
"Terrible experience. Will not buy again."	Negative

📁 Dataset
The model is trained using a dataset of labeled positive and negative reviews. The dataset is located in the data/ folder.

🤝 Contributing
Contributions are welcome! Feel free to fork the repo and submit a pull request. For major changes, please open an issue first to discuss your ideas.

📄 License
This project is licensed under the MIT License – see the LICENSE file for details.

🙏 Acknowledgements
TensorFlow

Keras

Flask

