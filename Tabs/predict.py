import streamlit as st
from sklearn.preprocessing import MinMaxScaler
from web_function import predict

def conv_num(data, map):
    data = map[data]

    return data

def app(df, x, y):

    st.title('Approval Prediction')

    col1, col2 = st.columns(2)

    '''
    #dict
    gender_map = { 'Female' : 0, 'Male' : 1}
    car_map = {'Yes' : 1, 'No' : 0}
    prop_map = {'Yes' : 1, 'No' : 0}
    typei_map = {'Commercial Associate' : 0, 'Pensioner' : 1, 'State servant' : 2, 'Working' : 3}
    edu_map = {'Academic Degree' : 0,'Higher Education' : 1,'Incomplete Higher' : 2,
               'Lower Secondary' : 3,'Secondary / Secondary Special' : 4}
    marital_map = {'Civil Marriage' : 0, 'Married' : 1, 'Separated' : 2, 'Single / Not Married' : 3, 'Widow' : 4}
    house_map = {'Co-op apartment' : 0, 'House / apartment' : 1, 'Municipal apartment' : 2,
                 'Office apartment' : 3, 'Rented apartment' : 4, 'With parents' : 5}
    occu_map = {'Accountants' : 0, 'Cleaning staff' : 1, 'Cooking staff' : 2, 'Core staff' : 3, 'Drivers' : 4, 'HR staff' : 5,
                'High skill tech staff' : 6, 'IT staff' : 7, 'Laborers' : 8, 'Low-skill Laborers' : 9, 'Managers' : 10, 'Medicine staff' : 11,
                'Private service staff' : 12, 'Realty agents' : 13, 'Sales staff' : 14, 'Secretaries' : 15, 'Security staff' : 16, 'Waiters/barmen staff' : 17}
    boolean_map = {'Yes' : 1, 'No' : 1}
    '''
    
    
    #list
    gender_list = ['Female', 'Male']
    car_list = ['Yes', 'No']
    prop_list = ['Yes', 'No']
    typei_list = ['Commercial Associate', 'Pensioner', 'State servant', 'Working']
    edu_list = ['Academic Degree','Higher Education','Incomplete Higher',
               'Lower Secondary','Secondary / Secondary Special']
    marital_list = ['Civil Marriage', 'Married', 'Separated', 'Single / Not Married', 'Widow']
    house_list = ['Co-op apartment', 'House / apartment', 'Municipal apartment',
                 'Office apartment', 'Rented apartment', 'With parents']
    occu_list = ['Accountants', 'Cleaning staff', 'Cooking staff', 'Core staff', 'Drivers', 'HR staff',
                'High skill tech staff', 'IT staff', 'Laborers', 'Low-skill Laborers', 'Managers', 'Medicine staff',
                'Private service staff', 'Realty agents', 'Sales staff', 'Secretaries', 'Security staff', 'Waiters/barmen staff']

    with col1:
        gender_map = { 'Female' : 0, 'Male' : 1}
        GENDER = st.selectbox('GENDER', gender_list)
        st.write('You Selected:', GENDER)
        GENDER = conv_num(GENDER, gender_map)
    with col2:
        Age = st.text_input('AGE')
        st.write('You are', Age, 'years old')
    with col1:
        car_map = {'Yes' : 1, 'No' : 0}
        Car_Owner = st.selectbox('CAR OWNED', car_list)
        st.write('You Selected:', Car_Owner)
        Car_Owner = conv_num(Car_Owner, car_map)
    with col2:
        prop_map = {'Yes' : 1, 'No' : 0}
        Propert_Owner = st.selectbox('PROPERTY OWNED', prop_list)
        st.write('You Selected:', Propert_Owner)
        Propert_Owner = conv_num(Propert_Owner, prop_map)
    with col1:
        CHILDREN = st.text_input('CHILDREN')
        st.write('You have', CHILDREN, 'Children')
    with col2:
        Annual_income = st.text_input('ANNUAL INCOME')
        st.write('Your Annual Income is $', Annual_income)
    with col1:
        typei_map = {'Commercial Associate' : 0, 'Pensioner' : 1, 'State servant' : 2, 'Working' : 3}
        Type_Income = st.selectbox('TYPE INCOME', typei_list)
        st.write('You Selected:', Type_Income)
        Type_Income = conv_num(Type_Income, typei_map)
    with col2:
        edu_map = {'Academic Degree' : 0,'Higher Education' : 1,'Incomplete Higher' : 2,
                    'Lower Secondary' : 3,'Secondary / Secondary Special' : 4}
        EDUCATION = st.selectbox('EDUCATION', edu_list)
        st.write('You Selected:', EDUCATION)
        EDUCATION = conv_num(EDUCATION, edu_map)
    with col1:
        marital_map = {'Civil Marriage' : 0, 'Married' : 1, 'Separated' : 2, 'Single / Not Married' : 3, 'Widow' : 4}
        Marital_status = st.selectbox('MARITAL STATUS', marital_list)
        st.write('You Selected:', Marital_status)
        Marital_status = conv_num(Marital_status, marital_map)
    with col2:
        house_map = {'Co-op apartment' : 0, 'House / apartment' : 1, 'Municipal apartment' : 2,
                    'Office apartment' : 3, 'Rented apartment' : 4, 'With parents' : 5}
        Housing_type = st.selectbox('HOUSING TYPE', house_list)
        st.write('You Selected:', Housing_type)
        Housing_type = conv_num(Housing_type, house_map)
    with col1:
        Employed_days = st.text_input('EMPLOYED DAYS')
        st.write('You have been working for', Employed_days, 'Days')
    with col2:
        boolean_map = {'Yes' : 1, 'No' : 1}
        Mobile_phone = st.selectbox('MOBILE PHONE', ('Yes', 'No'))
        st.write('You Selected:', Mobile_phone)
        Mobile_phone = conv_num(Mobile_phone, boolean_map)
    with col1:
        boolean_map = {'Yes' : 1, 'No' : 1}
        Work_Phone = st.selectbox('WORK PHONE', ('Yes', 'No'))
        st.write('You Selected:', Work_Phone)
        Work_Phone = conv_num(Work_Phone, boolean_map)
    with col2:
        boolean_map = {'Yes' : 1, 'No' : 1}
        Phone = st.selectbox('HAVE PHONE?', ('Yes', 'No'))
        st.write('You Selected:', Phone)
        Phone = conv_num(Phone, boolean_map)
    with col1:
        boolean_map = {'Yes' : 1, 'No' : 1}
        EMAIL_ID = st.selectbox('HAVE EMAIL?', ('Yes', 'No'))
        st.write('You Selected:', EMAIL_ID)
        EMAIL_ID = conv_num(EMAIL_ID, boolean_map)
    with col2:
        occu_map = {'Accountants' : 0, 'Cleaning staff' : 1, 'Cooking staff' : 2, 'Core staff' : 3, 'Drivers' : 4, 'HR staff' : 5,
                    'High skill tech staff' : 6, 'IT staff' : 7, 'Laborers' : 8, 'Low-skill Laborers' : 9, 'Managers' : 10, 'Medicine staff' : 11,
                    'Private service staff' : 12, 'Realty agents' : 13, 'Sales staff' : 14, 'Secretaries' : 15, 'Security staff' : 16, 'Waiters/barmen staff' : 17}
        Type_Occupation = st.selectbox('TYPE OCCUPATION', occu_list)
        st.write('You Selected:', Type_Occupation)
        Type_Occupation = conv_num(Type_Occupation, occu_map)
    with col1:
        Family_Members = st.text_input('FAMILY MEMBER')
        st.write('You have', Family_Members, 'Family Members')
        

    features = [Annual_income, EDUCATION, Marital_status,
                  Age, Employed_days, Type_Occupation, Family_Members]
    
    '''
    norm = MinMaxScaler()
    df['Annual_income'] = norm.fit_transform(df[['Annual_income']])
    '''

    if st.button('Approval Prediction'):
        prediction, score = predict(x, y, features)
        score = score
        st.info('Prediction Success')

        if (prediction == 1):
            st.success('Approved')
        if (prediction == 0):
            st.success('Rejected')

        st.write(f"Akurasi Model: {score*100:.2f} %")