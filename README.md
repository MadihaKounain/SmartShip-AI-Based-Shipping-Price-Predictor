
# 🚚 SmartShip: AI-Based Shipping Price Predictor

**SmartShip** is a machine learning web application built using Python and Streamlit that predicts the shipping cost (in INR) based on package weight, shipping distance, and delivery speed.

---

## 🔍 Features

- 📦 Predict shipping price based on:
  - Package Weight (kg)
  - Shipping Distance (km)
  - Delivery Speed (Standard, Next-day, Same-day)
- 💡 Powered by a trained Linear Regression model
- 🌐 Clean and interactive Streamlit UI
- 💰 Converts predicted price from USD to INR

---

## 🧠 Machine Learning Model

- **Algorithm:** Linear Regression
- **Input Features:**
  - `weight` (float)
  - `distance` (int)
  - `speed` (categorical encoded: 1–3)
- **Target:** `price` (in USD)
- Trained on historical shipping data

---

## 📁 Project Structure

```
shipping-price-predictor/
│
├── app.py                # Streamlit frontend
├── train_model.py        # Model training script
├── shipping_model.pkl    # Trained ML model (pickle)
├── shipping_data.csv     # Training dataset
└── README.md             # Documentation
```

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/shipping-price-predictor.git
   cd shipping-price-predictor
   ```

2. Install dependencies:
   ```bash
   pip install streamlit pandas scikit-learn numpy
   ```

3. Train the model (optional):
   ```bash
   python train_model.py
   ```

4. Run the web app:
   ```bash
   streamlit run app.py
   ```

---

## 📜 License

MIT License. Feel free to use, modify, and share!

---

## 🙋‍♀️ Developed by

**Madiha Kounain**  
Computer Science & Engineering Student  
