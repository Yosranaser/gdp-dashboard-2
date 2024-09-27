import streamlit as st
import pickle
import pandas as pd
from sklearn.cluster import KMeans
import sklearn
! pip install scikit-learn
st.title("KMeans Model Predictor")
st.image("Customer-Segmentation.png", caption="Customer-Segmentation", use_column_width=True)

# Sidebar for input
st.sidebar.title("Input Data")

# Taking inputs from the user in the sidebar
unit_price = st.sidebar.number_input("Enter Unit Price", min_value=0.0, step=0.01)  # Use a float step for unit price
quantity = st.sidebar.number_input("Enter Quantity", min_value=0, step=1)  # Integer step for quantity
customer_id = st.sidebar.text_input("Enter Customer ID")

stock_code = st.sidebar.text_input("Enter Stock Code")
day = st.sidebar.number_input("Enter day", min_value=0, step=1)  # Integer step for day
month = st.sidebar.number_input("Enter month", min_value=0, step=1)  # Integer step for month
year = st.sidebar.number_input("Enter year", min_value=0, step=1)  # Integer step for year


