# 1]Data Collection
import pandas as pd 

# Load Datasets 
furniture=pd.read_csv("ecommerce_furniture_dataset.csv")

# Check basic info
print("\nDataset Info:")
print(furniture.info())

# Viewing first 5 rows
print("First 5 rows of the dataset:")
print(furniture.head())

# 2] Data Cleaning 

# Check for missing values
print("\nMissing values:")
print(furniture.isnull().sum())

# Check for duplicates
print("\nDuplicate values:")
print(furniture.duplicated().sum())

# Drop duplicates
furniture.drop_duplicates(inplace=True)

# Drop missing values
furniture.dropna(inplace=True)

# Drop 'originalPrice' column if it has too many missing values
furniture.drop(columns=['originalPrice'], inplace=True)

# Clean the 'price' column (remove $ and commas)
furniture['price'] = furniture['price'].replace('[\$,]', '', regex=True).astype(float)

# Clean the 'tagText' column (categorize values)
furniture['tagText'] = furniture['tagText'].apply(lambda x: x if x in ['Free shipping', '+Shipping: $5.09'] else 'others')

# Encode 'tagText'
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
furniture['tagText'] = le.fit_transform(furniture['tagText'])

# Final check
print(furniture.head())


# 3] Exploratory Data Analysis

import matplotlib.pyplot as plt
import seaborn as sns
