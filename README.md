# WineTelliQ--Wine-Quality-predictor
Developed a full-stack Wine Quality Prediction web application using Flask for the backend and HTML, CSS, and JavaScript for the frontend. Trained a machine learning model on the Wine Quality Dataset (WineQT.csv) to accurately predict wine quality, integrating the model into the web application for real-time predictions. 

## 📌 Overview
The **Wine Quality Predictor** is a machine learning web application built with **Flask** that predicts the quality of red and white wines based on physicochemical features. It uses trained models on the popular **Wine Quality Dataset** to provide real-time predictions via an interactive web interface.

## 🚀 Features
- Train machine learning models for both **red** and **white** wines.
- Web-based prediction system with **Flask backend** and **HTML/CSS/JS frontend**.
- Interactive forms for user input of wine characteristics.
- Pre-trained models (`.joblib`) for immediate predictions.
- Modular design for easy extension and deployment.

## 🏗 Project Structure
![Home Page](screenshots/Dir_Str.png)

## 📊 Dataset
The project uses the **Wine Quality Data Set** from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/wine+quality).

- `winequality-red.csv` → Red wine dataset  
- `winequality-white.csv` → White wine dataset  

Each sample contains 11 physicochemical features such as:
- Fixed acidity  
- Volatile acidity  
- Citric acid  
- Residual sugar  
- Chlorides  
- Free sulfur dioxide  
- Total sulfur dioxide  
- Density  
- pH  
- Sulphates  
- Alcohol  

**Target variable:** Wine Quality (0–10 scale)

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/wine_quality_predictor.git
cd wine_quality_predictor
### **2. Create and activate a virtual environment**

python -m venv venv
source venv/bin/activate    # On Mac/Linux
venv\Scripts\activate       # On Windows
### 3. Install dependencies

pip install -r requirements.txt
🧠 Model Training
To train models for red and white wines:

python train_models.py
This generates:

red_wine_model.joblib

white_wine_model.joblib

Stored inside app/models/saved_models/

### ▶️ Running the Application
Start the Flask server:

python run.py
By default, it runs at:
👉 http://127.0.0.1:5000/

### 💻 Usage
Open the app in your browser.

Enter wine attributes (fixed acidity, pH, alcohol, etc.).

Choose red or white wine.

Click Predict to get the predicted quality score.

### 📦 Tech Stack
Backend: Flask (Python)

Frontend: HTML, CSS, JavaScript

ML Models: Scikit-learn

Data: UCI Wine Quality Dataset

Serialization: Joblib

📌 Example Workflow
Train ML models → save as .joblib

Flask app loads models at startup

User enters input via web form

Flask routes handle request → model prediction

Prediction displayed on web page
### 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to improve.

### 📜 License
This project is licensed under the MIT License.

### 👨‍💻 Author
Prajwal Channarayapatna Anand
📧 acesstopjl@gmail.com

