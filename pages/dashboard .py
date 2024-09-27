import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

# Load the KMeans model
with open('kmeans_model.pkl', 'rb') as file:
    kmeans_model = pickle.load(file)


# Streamlit layout with three columns
st.title("Customer Segmentation Dashboard")

