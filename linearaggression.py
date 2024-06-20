#import streamlit as st
import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.linear_model import LinearRegression
#from sklearn.model_selection import train_test_split

df_housing = fetch_openml(name="house_prices", as_frame=True)
X = df_housing.data[['GrLivArea',"YearBuilt"]]
Y = df_housing.target
print(df_housing.columns)

