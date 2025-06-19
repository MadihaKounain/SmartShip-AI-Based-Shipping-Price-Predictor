# train_model.py
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load the dataset
df = pd.read_csv(r'C:\Users\Madiha Kounain\Documents\shipping_price_prediction\shipping_data.csv')

# Features and target
X = df[['weight', 'distance', 'speed']]
y = df['price']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model to disk

with open("shipping_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved as 'shipping_model.pkl'")

