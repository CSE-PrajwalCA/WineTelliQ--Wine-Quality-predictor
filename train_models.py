import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os

def download_data():
    red_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
    white_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"
    red_data = pd.read_csv(red_url, sep=';')
    white_data = pd.read_csv(white_url, sep=';')
    
    os.makedirs('data', exist_ok=True)
    red_data.to_csv('data/winequality-red.csv', index=False)
    white_data.to_csv('data/winequality-white.csv', index=False)
    return red_data, white_data

def train_model(data, wine_type):
    X = data.drop('quality', axis=1)
    y = data['quality']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    param_grid = {
        'n_estimators': [100, 200],
        'max_depth': [10, 20, None],
        'min_samples_split': [2, 5]
    }
    
    rf = RandomForestRegressor(random_state=42)
    grid_search = GridSearchCV(rf, param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
    grid_search.fit(X_train, y_train)
    
    best_model = grid_search.best_estimator_
    y_pred = best_model.predict(X_test)
    
    print(f"\n{wine_type} Wine Model Performance:")
    print(f"Best Parameters: {grid_search.best_params_}")
    print(f"MSE: {mean_squared_error(y_test, y_pred):.4f}")
    print(f"R² Score: {r2_score(y_test, y_pred):.4f}")
    
    return best_model

def main():
    print("Downloading wine quality datasets...")
    red_data, white_data = download_data()
    
    print("Training red wine model...")
    red_model = train_model(red_data, "Red")
    
    print("Training white wine model...")
    white_model = train_model(white_data, "White")
    
    os.makedirs('app/models/saved_models', exist_ok=True)
    joblib.dump(red_model, 'app/models/saved_models/red_wine_model.joblib')
    joblib.dump(white_model, 'app/models/saved_models/white_wine_model.joblib')
    print("Models saved successfully!")

if __name__ == "__main__":
    main()
