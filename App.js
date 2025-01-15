import React, { useState } from 'react';
import WeatherForm from './components/WeatherForm';
import WeatherDisplay from './components/WeatherDisplay';

function App() {
    const [prediction, setPrediction] = useState(null);

    const fetchPrediction = async (data) => {
        const response = await fetch('http://localhost:5000/api/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data),
        });

        const result = await response.json();
        setPrediction(result.prediction);
    };

    return (
        <div>
            <h1>AI Weather Predictor</h1>
            <WeatherForm onPredict={fetchPrediction} />
            <WeatherDisplay prediction={prediction} />
        </div>
    );
}

export default App;
