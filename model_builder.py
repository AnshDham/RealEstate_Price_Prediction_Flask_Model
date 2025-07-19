# model_builder.py (you can run this once and delete after exporting)
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load the dataset
df = pd.read_excel('real_estate_data.xlsx')  # Ensure this file is in your folder

# Rename relevant columns if needed
df = df[['X2 house age', 'X3 distance to the nearest MRT station',
         'X4 number of convenience stores', 'Y house price of unit area']]
df.columns = ['age', 'distance', 'stores', 'price']

# Train model
X = df[['age', 'distance', 'stores']]
y = df['price']

model = LinearRegression()
model.fit(X, y)

# Export model
joblib.dump(model, 'price_model.pkl')
print("✅ Model saved as price_model.pkl")
