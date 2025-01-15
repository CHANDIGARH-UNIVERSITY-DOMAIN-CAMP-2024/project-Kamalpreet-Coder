import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def predict_weather(data, target_date):
    df = pd.DataFrame(data)
    df['temperature'] = df['temperature'].astype(float)
    X = df[['humidity', 'pressure', 'wind_speed']]
    y = df['temperature']

    model = LinearRegression()
    model.fit(X, y)

    # Example input for prediction
    input_data = [[60, 1013, 10]]  # Replace with actual data
    prediction = model.predict(input_data)
    return round(prediction[0], 2)
