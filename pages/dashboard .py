import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import rarfile
import os


# Load the KMeans model
with open('kmeans_model.pkl', 'rb') as file:
    kmeans_model = pickle.load(file)
# Path to the .rar file
rar_path = 'data.rar'

# Extract the .rar file
with rarfile.RarFile(rar_path) as rf:
    rf.extractall()  # Extracts files to the current directory

# Assuming the extracted file is named 'data.csv'
csv_file_path = 'data.csv'

# Check if the file was extracted and exists
if os.path.exists(csv_file_path):
    df = pd.read_csv(csv_file_path)
    st.write(df)  # Display the dataframe
else:
    st.write("Extracted file not found.")
 

# Streamlit layout with three columns
st.title("Customer Segmentation Dashboard")


