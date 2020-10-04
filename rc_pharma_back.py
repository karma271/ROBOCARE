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
st.title('**`Pharmacy Backend`**')
st.subheader('RoboCare Name: R@D@')
st.write('Page   **2**   of   **3**')


st.write('''Robocare can implement ML to detect anomalies in the system - notify system admin / security admin.''')

st.markdown(
    """        
        <html>
            <hr>
        </html>
    """,
    unsafe_allow_html=True
)

st.subheader('Real Time Inventory Information')
st.markdown(
    """
    * **Low Stock alert!**
    
    > only 2 of `Hydroxyzine Hydrochloride` left in the stock
 
    > ration mode ON for `Hydroxyzine Hydrochloride`
   
    ** Query to the databse: **
    
    * when is next delivery due for `Hydroxyzine Hydrochloride`?
    
    > 1 week
 """
 )


st.markdown(
    """        10.
        <html>
            <hr>
        </html>
    """,
    unsafe_allow_html=True
)


st.subheader('Security of the RoboCares')
st.write("All 50 active RoboCare is 100% secure")

st.markdown(
    """        10.
        <html>
            <hr>
        </html>
    """,
    unsafe_allow_html=True
)


st.subheader('Health of the RoboCares')
st.write("47 out of 50 Active RoboCares are in good health.")
st.write("2 out of 50 Active RoboCares need to recharged.")
st.write("1 out of 50 Active RoboCares need maintenance.")


st.markdown(
    """        
        <html>
            <hr>
        </html>
    """,
    unsafe_allow_html=True
)



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