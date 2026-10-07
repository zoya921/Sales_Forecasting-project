# Sales Forecasting

A machine learning project that predicts future sales using **Linear Regression** and displays the results through an interactive **Streamlit** web application.

## Project Overview

This project uses historical sales data to build a sales forecasting model. The model uses date-based features such as:

- Year
- Month
- Day

The trained Linear Regression model is used to predict sales for the next 30 days.

## Dataset

The dataset contains 731 records with the following columns:

- Date
- Sales
- Product
- Category
- Year
- Month
- Day

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit
- Linear Regression

## Model Performance

The model achieved the following results:

- **MAE:** 601.10
- **RMSE:** 717.02

## Features

- Historical sales data visualization
- 30-day future sales forecasting
- Predicted sales table
- Future sales trend graph
- Interactive Streamlit interface

## Project Structure

```text
sales-forecasting-project/
│
├── app.py
├── sales_data.csv
├── requirements.txt
└── README.md
```

## How to Run

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

## Conclusion

The project demonstrates how Linear Regression can be used with date-based features to forecast future sales. The resulting Streamlit application provides an easy-to-use interface for viewing the dataset and future sales predictions.
