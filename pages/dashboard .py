import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

# Load the KMeans model
with open('kmeans_model.pkl', 'rb') as file:
    kmeans_model = pickle.load(file)

# Load your dataset (replace with the actual dataset path)
df = pd.read_csv('data.csv.zip')  # Ensure the correct dataset is being loaded

# Streamlit layout with three columns
st.title("Customer Segmentation Dashboard")

