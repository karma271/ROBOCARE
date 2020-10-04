# Imports:
import dill
import pandas as pd
import numpy as np
import re
import streamlit as st

# ------------------------------------------------------------------------
st.image('./Robocare_name_logo.PNG', use_column_width=True)


@st.cache(allow_output_mutation=True)
def get_data():

    patient_df = pd.read_csv("../data/patient_dataset.csv")
    drugs_df = pd.read_csv("../data/drugs_dataset.csv")
    pharmacy_df = pd.read_csv("../data/pharmacist_dataset.csv")
    
    return patient_df, drugs_df, pharmacy_df


patient_df, drugs_df, pharmacy_df = get_data()

st.title('')
st.title('**`Pharmacists View`**')
st.subheader('Pharmacists Name: Ed Nigma')
st.write('Page   **2**   of   **3**')


st.write('''Our tool assists Pharmacists to accurately and efficiently place prescription order for the patient''')


st.title(" ")   
st.radio("Welcome to Walgreens, Rosie Jetsons! How would you like to interact with me?", options = ['Text', 'Audio', 'Haptic Braille'])


st.selectbox("Please select the language of your choice", options = ['English', 'Spanish', 'Portugees', 'French', 'German', 'Italian', 'Mandarin', 'Cantonese', 'Hindi', 'Japanese', 'Korean'])

st.write('Note: RoboCare is working hard to add more languages.')

st.markdown(
    """        
        <html>
            <hr>
        </html>
    """,
    unsafe_allow_html=True
)
st.subheader('Patient Information')
st.write('Patient name : Rosie Jetsons')
st.write('Date of Birth : 01/12/****')
st.write('Please login to view more personal information.')

st.markdown(
    """        
        <html>
            <hr>
        </html>
    """,
    unsafe_allow_html=True
)

st.subheader('Prescription')
st.write("I understand you need 2 refills. I can give you 1 today.")
st.write(" I can mail the second refill to you in 5 business days - we will make sure your medicine reaches you on time! 🙂")

st.write("Do you still want to send this to:")
st.write("142 Martian Steet, \n New York 10029")

response =st.radio(" ", options = ['Yes', 'No'])

st.title(" ")
if response == "No":
    st.write("**Please add your new address:**")
    st.text_input("")
else:
    pass

st.image('./robot.png', use_column_width=True)


# <script>
#     function bigImg(x) {
#     x.style.height = "80px";
#     x.style.width = "80px";
#     x.style.opacity = "0.1";
# }

#     function normalImg(x) {
#     x.style.height = "80px";
#     x.style.width = "80px";
#     x.style.opacity = "10";
#     }
# </script>