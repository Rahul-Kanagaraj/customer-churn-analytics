import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Customer Analysis", layout="wide")

st.title("Customer Analysis")

df = pd.read_csv("data/processed/cleaned_telco_churn.csv")

gender = st.sidebar.multiselect(
    "Gender",
    df["gender"].unique(),
    default=df["gender"].unique()
)

contract = st.sidebar.multiselect(
    "Contract",
    df["Contract"].unique(),
    default=df["Contract"].unique()
)

filtered_df = df[
    (df["gender"].isin(gender)) &
    (df["Contract"].isin(contract))
]

col1, col2 = st.columns(2)

with col1:
    fig = px.histogram(
        filtered_df,
        x="tenure",
        color="Churn",
        title="Tenure Distribution by Churn"
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.box(
        filtered_df,
        x="Churn",
        y="MonthlyCharges",
        title="Monthly Charges by Churn"
    )
    st.plotly_chart(fig, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    gender_churn = filtered_df.groupby("gender")["ChurnFlag"].mean().reset_index()
    gender_churn["Churn Rate"] = gender_churn["ChurnFlag"] * 100

    fig = px.bar(
        gender_churn,
        x="gender",
        y="Churn Rate",
        title="Churn Rate by Gender"
    )
    st.plotly_chart(fig, use_container_width=True)

with col4:
    senior_churn = filtered_df.groupby("SeniorCitizen")["ChurnFlag"].mean().reset_index()
    senior_churn["SeniorCitizen"] = senior_churn["SeniorCitizen"].map({0: "No", 1: "Yes"})
    senior_churn["Churn Rate"] = senior_churn["ChurnFlag"] * 100

    fig = px.bar(
        senior_churn,
        x="SeniorCitizen",
        y="Churn Rate",
        title="Churn Rate by Senior Citizen"
    )
    st.plotly_chart(fig, use_container_width=True)