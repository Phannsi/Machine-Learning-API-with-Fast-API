
#Loading necessary libraries
import streamlit as st
import joblib
import pandas as pd
import os
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import requests
import pandas as pd

# Define the backend URL
backend_url = 'http://127.0.0.1:8000'

# Set page configuration
st.set_page_config(
    page_title='Predict',
    page_icon='🔮',
    layout='wide'
)

# Load config file
with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Calling variables from the config file
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized']
)

# Place login widget to the sidebar
name, username, authentication_status = authenticator.login(location='sidebar')

# Load page if the user has logged in
if st.session_state['authentication_status'] == True:

    # Set page title with HTML
    with st.container(border=True):
        st.markdown(
                "<h1 style='text-align: center;  font-size: 50px; color: blue'>Prediction Page</h1>",
                unsafe_allow_html=True,
            )       
    # Create function to display form
    def display_form():

        st.write("Input Patient's Results")
        data = {}  # Initialize data as an empty dictionary

        with st.form('input-feature'):
            col1, col2 = st.columns(2)

            with col1:
                PRG = st.number_input('Plasma Glucose', min_value=0.0, value=0.1, key='PRG')
                PL = st.number_input('Blood Work Result-1 (mu U/ml)', min_value=0.0, value=0.1, key='PL')
                PR = st.number_input('Blood Pressure(mm Hg)', min_value=0.0, value=0.1, key='PR')
                SK = st.number_input('Blood Work Result-2 (mm)', min_value=0.0, value=0.1, key='SK')

            with col2:
                TS = st.number_input('Blood Work Result-3 (mu U/ml)', min_value=0.0, value=0.1, key='TS')
                M11 = st.number_input('Body Mass Index (weight in kg/(height in m)^2', min_value=0.0, value=0.1, key='M11')
                BD2 = st.number_input('Blood Work Result-4(mu U/ml)', min_value=0.0, value=0.1, key='BD2')
                Age = st.number_input('Age (Years)',min_value=1, value=1, key='Age')
            
            # Create submit button to submit details on form
            if st.form_submit_button ('Predict Sepsis'):

                # Call Selected model from the session state
                selected_model = st.session_state['selected_model']

                # Create a dictionary with the data
                data = {
                    'PRG' : PRG, 
                    'PL' : PL,
                    'PR' : PR,
                    'SK' : SK,
                    'TS' : TS,
                    'M11' : M11,
                    'BD2' : BD2,
                    'Age' : Age
                }

                # Select endpoint in API based on model selection
                if selected_model == 'Random Forest':
                    response = requests.post(f'{backend_url}/Random_forest_prediction', json=data)
                    
                else:
                    response = requests.post(f'{backend_url}/Logistic_regression_prediction', json=data)

                    # Display the Prediction
                    if response.status_code == 200:

                        # Display Variables from the API endpoint
                        prediction = response.json()['Prediction']
                        probability = response.json()['Probability']
                        message = response.json()['Message']

                        # Assign variables to session state
                        st.session_state['probability'] = probability
                        st.session_state['prediction'] = prediction
                        st.session_state['message'] = message
                          
                    else:
                        # Show error details if there is an error at the endpoint
                        st.error(f"Error: {response.json()['detail']}")

    # Create widget to select model to use
    def select_model():
        col1, col2 = st.columns(2)

        with col1:
            st.selectbox('Select a Model', options=['Logistic Regression', 'Random Forest'], key='selected_model')

        with col2:
            pass


    if __name__ == "__main__":

        select_model()
        
        display_form()

    # Display text if prediction has not been made
    if 'prediction' not in st.session_state:
        st.write('Your Prediction will show here')
        
    else:

        # Calling variables form the Session state
        prediction = st.session_state['prediction']
        selected_model = st.session_state['selected_model']
        message = st.session_state['message']
        probability = st.session_state['probability'] 

        # Assigning probabilities from the dictionary
        probability_of_negative = probability['Negative']
        probability_of_positive = probability['Positive']

        # Display predictions from the endpoint
        if prediction == 'Negative':
            st.write(f'Per the {selected_model} model selected, the prediction is {prediction}, {message} with a probability of {probability_of_negative}%')
        else:
            st.write(f'Per the {selected_model} model selected, the prediction is {prediction}, {message} with a probability of {probability_of_positive}%')
# Display Message if User has not logged in
elif st.session_state['authentication_status'] == False:
    st.error('Wrong username or password')
elif st.session_state['authentication_status'] == None:
    
    # Show guest login information for user to login
    st.info('Kindly login on the sidebar to gain access to the app')
    st.code('''
        Guest Account
        Username: guest
        Password: Guest123
    ''')