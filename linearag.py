#import streamlit as st
import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

try:
  # Fetch the house_prices dataset with error handling
  df_housing = fetch_openml(name="house_prices", as_frame=True)
except Exception as e:
  st.error(f"An error occurred while fetching the dataset: {e}")

# Check if dataset retrieval was successful
if df_housing is not None:
  X = df_housing.data[['GrLivArea', "YearBuilt"]]
  Y = df_housing.target
  st.write(df_housing.columns())  # Use st.write for Streamlit output

