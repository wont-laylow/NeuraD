# Diabetes Prediction API

A simple neural network built with PyTorch and FastAPI for predicting the likelihood of diabetes. The model is exposed via a REST API for easy integration.

Installation
1️. Clone the repository

git clone https://github.com/wont-laylow/NeuraD.git
cd NeuraD

2️. Create a virtual environment & install dependencies
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt

3️. Run the FastAPI server
uvicorn main:app --reload

Usage
Make a Prediction (POST /predict/) in this format
{
  "Glucose": 120,
  "BMI": 30.5,
  "DiabetesPedigreeFunction": 0.8,
  "Age": 45
}