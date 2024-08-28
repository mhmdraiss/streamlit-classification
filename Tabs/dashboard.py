import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from web_function import load_data

def app(df, x, y):

    data_viz = pd.read_csv('dataset_modeling.csv')
    gender_viz = data_viz.groupby('GENDER').size().reset_index(name='Count')
    child_viz = data_viz.groupby('CHILDREN').size().reset_index(name='Count')
    age_viz = data_viz.groupby('Age').size().reset_index(name='Count')
    avgi_oc = data_viz.groupby('Type_Occupation')['Annual_income'].mean().reset_index(name='Count')
    avgi_i = data_viz.groupby('Type_Income')['Annual_income'].mean().reset_index(name='Count')
    avgi_edu = data_viz.groupby('EDUCATION')['Annual_income'].mean().reset_index(name='Count')
    
    st.title('Data Frames Overview')

    df_dashboard = df
    st.dataframe(
                    df_dashboard,
                    use_container_width=True
                    )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader('Gender Distribution', divider = 'blue')
        st.bar_chart(
                        gender_viz,
                        x = 'GENDER',
                        y = 'Count',
                        x_label = 'Gender',
                        y_label = 'Count',
                        use_container_width = False,
                        width = 300,
                        height = 300
                        )
        
    with col2:
        st.subheader('Age Distribution', divider = 'blue')
        st.bar_chart(
                        age_viz,
                        x = 'Age',
                        y = 'Count',
                        x_label = 'Age',
                        y_label = 'Count',
                        use_container_width = False,
                        width = 300,
                        height = 300
                        )

    with col2:
        st.subheader('Sebaran Jumlah Anak', divider = 'blue')
        st.bar_chart(
                        child_viz,
                        x = 'CHILDREN',
                        y = 'Count',
                        x_label = 'Children',
                        use_container_width = False,
                        width = 300,
                        height = 300
                        )
        
    with col1:
        st.subheader('Annual Income per Type Occupation', divider = 'red')
        st.bar_chart(
                        avgi_oc,
                        x = 'Type_Occupation',
                        y = 'Count',
                        x_label = 'Type Occupation',
                        use_container_width = False,
                        width = 300,
                        height = 300
                        )
        
    with col2:
        st.subheader('Annual Income per Education', divider = 'red')
        st.bar_chart(
                        avgi_edu,
                        x = 'EDUCATION',
                        y = 'Count',
                        x_label = 'Education',
                        use_container_width = False,
                        width = 300,
                        height = 300
                        )
        
    with col1:
        st.subheader('Annual Income per Type Income', divider = 'red')
        st.bar_chart(
                        avgi_i,
                        x = 'Type_Income',
                        y = 'Count',
                        x_label = 'Type Income',
                        use_container_width = False,
                        width = 300,
                        height = 300
                        )