import streamlit as st
import pickle
from datetime import date

model = pickle.load(open('car_rf_regression_model.pkl', 'rb'))

def predict_car_price():
    present_price=st.number_input(label="Present price",min_value = 50000)/100000
    kms_driven=st.number_input(label="KMs driven",min_value = 1000)
    owner_count=st.number_input(label="No of owner")
    year=st.number_input(label='Year')
    years_old = date.today().year - year
    fuel_type=st.text_input(label="Fuel type",help="Petrol or Diesel or CNG")
    if fuel_type=='Petrol':
        petrol=1
        diesel=0
    elif fuel_type=='Diesel':
        petrol=0
        diesel=1
    else:
        petrol=0
        diesel=0
    seller_type = st.text_input(label="Seller type",help="Dealer or individual")
    if seller_type == 'Dealer':
        seller_type_ind=0
    else:
        seller_type_ind=1
    trans_type = st.text_input(label="Transmission type",help="Manual or Automatic")
    if trans_type == 'Manual':
        trans_type_manual=1
    else:
        trans_type_manual=0
    prediction=model.predict([[present_price,kms_driven,owner_count,years_old,diesel,petrol,seller_type_ind,trans_type_manual]])
    output=round(prediction[0],2)
    st.write(output, "Lakh(s)")
    