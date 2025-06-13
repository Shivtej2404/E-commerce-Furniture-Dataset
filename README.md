# 🛋️ Furniture Sales Prediction

This project analyzes and predicts sales of furniture items using machine learning techniques. It includes data cleaning, exploratory data analysis (EDA), feature engineering, model training, and evaluation, concluding with saving the best-performing model.

## 📁 Files Included

- `ecommerce_furniture_dataset.csv` - Raw dataset containing furniture listings and their attributes.
- `furniture-analysis.py` - Python script for full analysis and model development.
- `furniture_sales_model.pkl` - Trained machine learning model saved using `pickle`.

## 🚀 Project Workflow

### 1. Data Collection
- Loaded the dataset using pandas.
- Inspected data structure and previewed rows.

### 2. Data Cleaning
- Handled missing values and duplicates.
- Cleaned numerical columns (`price`, `originalPrice`) by removing currency symbols and converting them to numeric format.
- Encoded categorical values (`tagText`) using Label Encoding.

### 3. Exploratory Data Analysis (EDA)
- Visualized distributions of price and sold units.
- Plotted relationships between price, original price, and sold units using seaborn.

### 4. Feature Engineering
- Calculated discount percentage as a new feature.
- Transformed `productTitle` into TF-IDF features (top 100 tokens).
- Combined all features into a single dataset for modeling.

### 5. Model Training
- Split the data into training and testing sets.
- Trained two models:
  - **Linear Regression**
  - **Random Forest Regressor**

### 6. Model Evaluation
- Compared models using:
  - **Mean Squared Error (MSE)**
  - **R² Score**
- Chose the better model (Random Forest or Linear Regression based on performance) and saved it to `furniture_sales_model.pkl`.

## 📊 Libraries Used

- `pandas`, `numpy`
- `matplotlib`, `seaborn`
- `scikit-learn`
- `pickle`

## 🧠 Model Use Case

The saved model can be used to predict how many units of a product are likely to be sold based on features like price, discount, shipping tag, and title keywords.

## 🔧 How to Run

1. Clone this repo or download the files.
2. Install required packages:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
3. Run the script
python furniture-analysis.py
4. Use the generated furniture_sales_model.pkl to make future predictions.


✍️ Author
Shivtej Jad
Email: shivtej0907@gmail.com