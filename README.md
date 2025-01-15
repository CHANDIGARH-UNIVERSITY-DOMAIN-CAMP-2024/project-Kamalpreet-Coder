# **AI-Based Weather Prediction System**

## **Overview**
The AI-Based Weather Prediction System is a project that utilizes artificial intelligence to predict weather conditions based on historical data. It consists of three main components:
- **Backend**: A Flask API powered by TensorFlow for model predictions.
- **Frontend**: A React.js application for the user interface.
- **Database**: MongoDB for storing and retrieving weather data.

This project aims to enhance the accuracy and reliability of weather forecasting, providing valuable insights for users.

---

## **Features**
- AI model trained on historical weather data.
- React.js frontend for user interaction.
- Flask API for real-time weather predictions.
- MongoDB integration for efficient data storage.

---

## **Technologies Used**
1. **Frontend**:
   - React.js
   - Axios for API requests
2. **Backend**:
   - Flask
   - TensorFlow
   - Python
3. **Database**:
   - MongoDB

---

## **Installation Instructions**

### **Prerequisites**
- Python 3.8+
- Node.js and npm
- MongoDB installed locally or hosted (e.g., MongoDB Atlas)

---

### **Backend Setup**

1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```

2. Install required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Insert sample weather data into MongoDB:
   - Update the MongoDB connection string in `insert_data.py` if necessary.
   - Run the script:
     ```bash
     python insert_data.py
     ```

4. Train the AI model (optional if `weather_model.h5` already exists):
   ```bash
   python model.py
   ```

5. Start the Flask API server:
   ```bash
   python app.py
   ```

   By default, the server will run on `http://127.0.0.1:5000`.

---

### **Frontend Setup**

1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```

2. Install required npm packages:
   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   ```

   By default, the app will run on `http://localhost:3000`.

---

## **Usage**

1. Ensure that both the backend and frontend servers are running.
2. Open your browser and navigate to `http://localhost:3000`.
3. Click the **"Get Weather Prediction"** button to receive AI-based weather predictions.

---

## **File Structure**

```plaintext
weather-prediction/
├── backend/
│   ├── app.py              # Flask API
│   ├── model.py            # AI model training
│   ├── insert_data.py      # MongoDB data insertion
│   ├── requirements.txt    # Backend dependencies
│   ├── weather_model.h5    # Trained AI model
│   ├── weather_data.csv    # Sample dataset
├── frontend/
│   ├── public/
│   │   ├── index.html      # HTML template
│   │   └── favicon.ico     # App icon
│   ├── src/
│   │   ├── App.js          # Main React component
│   │   ├── index.js        # React app entry point
│   │   ├── styles.css      # App styling
│   ├── package.json        # Frontend dependencies
│   └── README.md           # Frontend-specific instructions
└── README.md               # Project documentation
```

---

## **Endpoints**

- **GET /predict**  
  Returns the weather prediction based on input features. Example response:
  ```json
  {
    "prediction": [0.8]
  }
  ```
  
---

## **License**
This project is licensed under the MIT License. 
---

## **Contact**
For questions or feedback, feel free to reach out to:
- **Name**: Kamalpreet
- **Email**: singhkamalpreet4745@gmail.com

