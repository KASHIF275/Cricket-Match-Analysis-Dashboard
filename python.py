import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# Data Loading Function
@st.cache_data
def load_data(file):
    # Load the dataset from the uploaded file
    df = pd.read_csv(file)
    return df

# App Title
st.title("ODI Cricket Dashboard")

# File Uploader
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

# Check if a file is uploaded
if uploaded_file is not None:
    # Load the data
    df = load_data(uploaded_file)

    # (Continue with the rest of your code using the loaded `df`)
else:
    st.warning("Please upload a CSV file to proceed.")
