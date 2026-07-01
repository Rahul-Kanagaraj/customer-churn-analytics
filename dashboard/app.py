import streamlit as st

st.set_page_config(
    page_title="Customer Churn Analytics",
    layout="wide"
)

st.title("Customer Churn & Revenue Analytics")

st.markdown("""
## Project Overview

This dashboard analyzes telecom customer churn using:

- Python
- SQL
- Statistical Analysis
- Machine Learning
- Streamlit Dashboard

## Business Problem

Customer churn reduces recurring revenue.  
The goal is to identify churn drivers, high-risk customers, revenue loss, and retention opportunities.

## Dashboard Pages

Use the sidebar to navigate:

1. Executive Dashboard  
2. Customer Analysis  
3. Revenue Analysis  
4. Statistical Analysis  
5. Machine Learning  

## Dataset

IBM Telco Customer Churn Dataset

## Key Features

- Churn Rate Analysis
- Revenue Loss Analysis
- Customer Segmentation
- High-Risk Customer Identification
- Hypothesis Testing
- Machine Learning Churn Prediction
""")