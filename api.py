from flask import Flask, request, jsonify, render_template
import re
import pickle
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

STOPWORDS = set(stopwords.words("english"))

app = Flask(__name__)

@app.route("/test", methods=["GET"])
def test():
    return "Test request received successfully. Service is running."

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("landing.html")

@app.route("/predict", methods=["POST"])
def predict():
    predictor = pickle.load(open(r"model_xgb.pkl", "rb"))
    scaler = pickle.load(open(r"scaler.pkl", "rb"))
    cv = pickle.load(open(r"countVectorizer.pkl", "rb"))
    try:
        if "text" in request.json:
            # Single string prediction
            text_input = request.json["text"]
            rating = request.json.get("rating", 3)  
            predicted_sentiment = single_prediction(predictor, scaler, cv, text_input, rating)

            return jsonify({"prediction": predicted_sentiment})

    except Exception as e:
        return jsonify({"error": str(e)})

def single_prediction(predictor, scaler, cv, text_input, rating):
    corpus = []
    stemmer = PorterStemmer()
    review = re.sub("[^a-zA-Z]", " ", text_input)
    review = review.lower().split()
    review = [stemmer.stem(word) for word in review if not word in STOPWORDS]
    review = " ".join(review)
    corpus.append(review)
    X_prediction = cv.transform(corpus).toarray()
    X_prediction_scl = scaler.transform(X_prediction)
    y_predictions = predictor.predict_proba(X_prediction_scl)
    if rating >= 3:
        return "Positive"
    elif rating <= 2:
        return "Negative"
    else:
        return "Neutral"

if __name__ == "__main__":
    app.run(port=5000, debug=True)
