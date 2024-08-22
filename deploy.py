import streamlit as st
from web_function import load_data
from Tabs import home, dashboard, predict, visualise

Tabs = {
    'Home' : home,
    'Dashboard' : dashboard,
    'Prediction' : predict,
    'Confusion Matrix' : visualise
}

st.sidebar.title('Navigations')

page = st.sidebar.radio('Pages', list(Tabs.keys()))

df, x, y = load_data()

if page in Tabs:
    if page in ['Prediction', 'Confusion Matrix', 'Dashboard']:
        Tabs[page].app(df, x, y)

    else:
        Tabs[page].app()
else:
    st.error(f"Page '{page}' not found in Tabs")