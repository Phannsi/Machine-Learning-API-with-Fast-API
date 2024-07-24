
import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader


## page configuration settings
st.set_page_config(
page_title="Home",
page_icon="🏠",
layout="wide"
)


with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized']
)

name, username, authentication_status = authenticator.login(location='sidebar')

if st.session_state['authentication_status'] == True:
    def display_contact():
        st.sidebar.write(
            """
        Let's connect, Your feedback, questions and recommendations are welcome.
        """
        )


        with st.container(border=True):st.sidebar.write(
            """
    <div style="display: flex; justify-content: center; background-color: white; padding: 10px; border-radius: 10px;">
        <a href="https://github.com/Phannsi" style="padding: 5px; list-style-type: none; text-decoration: none;">
            <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="35px"></img>
        </a>
        <a href="https://www.linkedin.com/in/ezekielphannsi" style="padding: 5px; list-style-type: none; text-decoration: none;">
            <img src="https://i.pinimg.com/736x/96/8e/a6/968ea62882943e88bbd318ae5fa67429.jpg" width="35px"></img>
        </a>
    </div>
    """,
            unsafe_allow_html=True,
        )


    # put title element in container
    def display_home_title():
        with st.container(border=True):
            st.markdown(
                "<h1 style='text-align: center;  font-size: 70px; color: blue'>Sepsis Prediction App! </h1>",
                unsafe_allow_html=True,
            )

    # Sample text for the sections
    home_text = "Welcome to the Sepsis prediction application."
    how_to_run_text = "To run the application, simply login and navigate through the sidebar."


    def logo():
        col1, col2, col3 = st.columns(3)

        with col1:
            pass

        with col2:
            pass
            #with st.container(border=True):
                    #st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Logo_vodafone_new.png/1200px-Logo_vodafone_new.png')
        with col3:
            pass


    def display_home_body():
        col1, col2, col3 = st.columns(3)

        with col1:
            with st.container(border=True):
                st.subheader('Definition of sepsis')
                st.markdown(
                    '''    
                'Sepsis is a serious condition in which the body responds improperly to an infection.
                The infection-fighting processes turn on the body, causing the organs to work poorly.
                Sepsis may progress to septic shock. This is a dramatic drop in blood pressure that can damage the lungs, kidneys, liver and other organs.'

                Is Sepsis Contagious:
                
                Sepsis itself isn’t contagious — you can’t spread it to other people. But you can spread the infections that can cause sepsis.
                '''

                )

        with col2:
            with st.container(border=True):

                st.image('https://my.clevelandclinic.org/-/scassets/images/org/health/articles/12361-sepsis', use_column_width=True)


        with col3:
            with st.container(border=True):
                st.subheader('Who does sepsis affect')
                '''
                Sepsis can affect anyone, but people with any kind of infection, especially bacteremia, are at a particularly high risk.

                Other people who are at a high risk include:

                People older than 65 years old, newborns and infants, and pregnant people.
                People with medical conditions such as diabetes, obesity, cancer and kidney disease.
                People with weakened immune systems.
                People who are in the hospital for other medical reasons.
                People with severe injuries, such as large burns or wounds.
                People with catheters, IVs or breathing tubes.
                '''

        # Center-align text using CSS styles
        centered_text1 = f"<p style='text-align: center;'>This application was built as a data Science project for Azubi Africa!</p>"
        centered_text2 = f"<p style='text-align: center;'>Copyright © 2024!</p>"
        

        
        st.write(centered_text1, unsafe_allow_html=True)
        
        st.write(centered_text2, unsafe_allow_html=True)
       
        

    def main():
        
        display_contact()

        display_home_title()

        logo()

        display_home_body()


    if __name__ == "__main__":

        main()  


elif st.session_state['authentication_status'] == False:
    st.error('Wrong username or password')
elif st.session_state['authentication_status'] == None:
    st.info('Kindly login on the sidebar to gain access to the app')
    st.code('''
        Guest Account
        Username: guest
        Password: Guest123
    ''')
