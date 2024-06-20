import streamlit as st
import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

housing_dataset = fetch_openml(name="house_prices", as_frame=True)

df_housing = housing_dataset.data

X = df_housing[["GrLivArea", "YearBuilt"]]

Y = housing_dataset.target

print(df_housing.columns)
