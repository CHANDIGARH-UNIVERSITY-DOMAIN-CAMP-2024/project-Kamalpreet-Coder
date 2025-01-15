from flask import Flask, jsonify, request
from flask_cors import CORS
from model import predict_weather
import pymongo

app = Flask(__name__)
CORS(app)

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['weatherDB']
collection = db['historical_data']

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.json
    city = data['city']
    date = data['date']

    # Retrieve historical data for prediction
    historical_data = list(collection.find({'city': city}))
    prediction = predict_weather(historical_data, date)

    return jsonify({'prediction': prediction})

@app.route('/api/data', methods=['POST'])
def add_data():
    data = request.json
    collection.insert_one(data)
    return jsonify({'message': 'Data added successfully'})

if __name__ == "__main__":
    app.run(debug=True)
