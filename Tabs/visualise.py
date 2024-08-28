import warnings
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
import streamlit as st
from web_function import train_model

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

def plot_confusion_matrix(y_true, y_pred, class_names):
    cm = confusion_matrix(y_true, y_pred)
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=class_names, yticklabels=class_names)
    plt.ylabel('Aktual')
    plt.xlabel('Prediksi')
    plt.title('Confusion Matrix')
    return fig

def app(df, x, y):
    st.title('Confusion Matrix')

    if st.checkbox('Tampilkan Confusion Matrix'):
              
        model, score = train_model(x, y)
        y_pred = model.predict(x)
        
        class_names = np.unique(y)
       
        fig = plot_confusion_matrix(y, y_pred, class_names)
     
        st.pyplot(fig)

        st.write(f"Akurasi Model: {score*100:.2f} %")