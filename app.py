import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Page title
st.set_page_config(page_title="Sales Forecasting", page_icon="📈")

st.title("📈 Sales Forecasting System")
st.write("This application predicts future sales using Linear Regression.")

# Load dataset
df = pd.read_csv("sales_data.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Create Year, Month and Day
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day

# Features and target
X = df[["Year", "Month", "Day"]]
y = df["Sales"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Display dataset
st.subheader("Sales Dataset")
st.dataframe(df.head(10))

# Future dates
future_dates = pd.date_range(
    start=df["Date"].max() + pd.Timedelta(days=1),
    periods=30
)

# Future features
future_X = pd.DataFrame({
    "Year": future_dates.year,
    "Month": future_dates.month,
    "Day": future_dates.day
})

# Predictions
future_predictions = model.predict(future_X)

# Forecast table
future_forecast = pd.DataFrame({
    "Date": future_dates,
    "Predicted Sales": future_predictions
})

# Display forecast
st.subheader("30-Day Sales Forecast")
st.dataframe(future_forecast)

# Graph
st.subheader("Future Sales Forecast")

chart_data = future_forecast.set_index("Date")

st.line_chart(chart_data["Predicted Sales"])