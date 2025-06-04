# Data Collection
import pandas as pd 

# Load Datasets 
furniture=pd.read_csv("ecommerce_furniture_dataset.csv")

# Check basic info
print("\nDataset Info:")
print(furniture.info())

# Viewing first 5 rows
print("First 5 rows of the dataset:")
print(furniture.head())
