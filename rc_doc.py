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

st.header("_...because robocare cares_")


rainbow_flower = "https://images.unsplash.com/photo-1495386786209-f284d613b8d0?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"






st.title('')
st.title('**`Doctor View`**')
st.subheader('Medication Module')
st.write('Page   **1**   of   **3**')

st.title(" ")

st.write('''Our tool enable you to create a prescription 
that can be promptly delivered the patient's chosen pharmacy!''')

st.title(" ")

st.write("Let's first find out the patient's needs.")
# Medication
med = st.text_input("Medication", value = 'Amoxicillin')
dose = st.selectbox("Dosage", [int(x) for x in sorted(drugs_df.dose_per_unit.unique())])
refills = st.text_input("Refills", value = '2')
patient = st.text_input("Patient name", value = 'Phil Sabie')


patient_dict = {
    'name'    : None,
    'address' : None,
    'contact' : None,
    'last_delievery' : None
}


patient_name = patient.split(' ')


patient_dict["name"] = patient
patient_dict["address"] =  patient_df.loc[ (patient_df["first_name"] == patient_name[0]) & (patient_df["last_name"] == patient_name[1])]["address"].values[0]
patient_dict["contact"] = patient_df.loc[ (patient_df["first_name"] == patient_name[0]) & (patient_df["last_name"] == patient_name[1])]["mobile"].values[0]
patient_dict["last_delivery"] = patient_df.loc[ (patient_df["first_name"] == patient_name[0]) & (patient_df["last_name"] == patient_name[1])]["last_delivery"].values[0]

# patient_address_2 = patient_df.loc[ (patient_df["first_name"] == patient_name[0]) & (patient_df["last_name"] == patient_name[1])]["address"].values[0]

st.write('Patient name:', patient)
st.write('Address:', patient_dict["address"])
st.write('Contact:', patient_dict["contact"])
st.write('Last Delivery:', patient_dict["last_delivery"])


# st.write(pharmacy_df.head())
pharmacy_name_list = []
nearest_pharmacy = pharmacy_df.loc[ (pharmacy_df["address2"] == patient_dict["address"]) ]["pharmacist_name"].tolist()[0]
pharmacist_name = str(pharmacy_df.loc[ (pharmacy_df["address2"] == patient_dict["address"]) ]["first_name"].tolist()[0]) +  " " + str(pharmacy_df.loc[ (pharmacy_df["address2"] == patient_dict["address"]) ]["last_name"].tolist()[0])
st.write("Pharmacy near you: \n", nearest_pharmacy)




# doctor information
st.write("Doctor:")

# pharmacist name
st.write("Pharmacist Name:", pharmacist_name)

# medication
st.write(f"Medication: {med} , dosage: {dose}, refills: {refills} ")


st.markdown(
    """        
        <html>
            <hr>
        </html>
    """,
    unsafe_allow_html=True
)


# mock_schedule
med_1 = {"name" : "Amoxicillin", 
         "doze" : "20 mg",
        #  "schedule" : "2 tabs before meal (Morning)",
         "Notes" : "Critical - Pair with Protonix",
         "Date Prescribed" : "2019-01-12"
        }

med_2 = {"name" : "Protonix", 
         "doze" : "10 mg",
        #  "schedule" : "1 tab after meal (Morning)",
         "Notes" : "Critical - Pair with Amoxicillin",
         "Date Prescribed" : "2019-01-12"
        }

med_3 = {"name" : "Levofloxacin", 
         "doze" : "5 mg",
        #  "schedule" : "1 tab after meal (Night)",
         "Notes" : "-",
         "Date Prescribed" : "2020-03-18"
        }

dataframe = pd.DataFrame([med_1, med_2, med_3])
dataframe.set_index("name", inplace=True)

st.write(f"Full Medication Summary")
st.dataframe(dataframe.style.highlight_max(axis=0))


# pharmacy = st.selectbox("Pharmacy near you", set(pharmacy_df.loc[ (pharmacy_df["address2"] == patient_dict["address"]) ]["pharmacist_name"].tolist()))
 
st.title(" ")
st.title(" ")
st.write('### Watch this space, **Robocare** is constantly _`evolving`_ to **care** for you! 💗')



