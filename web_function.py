import pandas as pd
import numpy as np
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, ConfusionMatrixDisplay

# @st.cache_data()
def load_data():
    df = pd.read_csv('dataset_modeling(encoding).csv')
    df = df.reset_index(drop=True)

    x = df[['Annual_income', 'EDUCATION', 'Marital_status', 'Age',
            'Employed_days', 'Type_Occupation', 'Family_Members']]
    y = df[['label']]

    return df, x, y

def train_model(x, y):

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(
            n_estimators= 100,
            random_state= 42
            )
    model.fit(x_train, y_train)
    score = model.score(x_test, y_test)

    return model, score

def predict(x, y, features):
    model, score = train_model(x, y)

    prediction = model.predict(np.array(features).reshape(1, -1))

    return prediction, score