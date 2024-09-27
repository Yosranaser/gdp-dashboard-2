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

col1, col2, col3 = st.columns(3)

# Plot 1: First column (e.g., cluster vs feature1)
with col1:
    st.header("Cluster vs Quantity")
    plt.figure(figsize=(5, 4))
    sns.scatterplot(x=df['Quantity'], y=df['Country'], hue=kmeans_model.labels_, palette='viridis')
    plt.title('Location Clusters')
    st.pyplot(plt)

# Plot 2: Second column (e.g., services distribution)
with col2:
    st.header("Services Distribution")
    plt.figure(figsize=(5, 4))
    service_counts = df['Quantity'].value_counts()
    sns.barplot(x=service_counts.index, y=service_counts.values)
    plt.xticks(rotation=90)
    plt.title('Distribution of Services')
    st.pyplot(plt)

# Plot 3: Third column (e.g., clusters in specific area)
with col3:
    st.header("Clusters by Area")
    plt.figure(figsize=(5, 4))
    sns.countplot(x=kmeans_model.labels_, data=df)
    plt.title('Number of Customers per Cluster')
    st.pyplot(plt)
