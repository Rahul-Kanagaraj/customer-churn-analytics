import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Revenue Analysis", layout="wide")

st.title("Revenue Analysis")

df = pd.read_csv("data/processed/cleaned_telco_churn.csv")

total_revenue = df["TotalCharges"].sum()
monthly_revenue = df["MonthlyCharges"].sum()
revenue_lost = df[df["Churn"] == "Yes"]["MonthlyCharges"].sum()
avg_monthly_charge = df["MonthlyCharges"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"${total_revenue:,.2f}")
col2.metric("Monthly Revenue", f"${monthly_revenue:,.2f}")
col3.metric("Revenue Lost", f"${revenue_lost:,.2f}")
col4.metric("Avg Monthly Charge", f"${avg_monthly_charge:.2f}")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    revenue_contract = df.groupby("Contract")["MonthlyCharges"].sum().reset_index()

    fig = px.bar(
        revenue_contract,
        x="Contract",
        y="MonthlyCharges",
        title="Monthly Revenue by Contract"
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    revenue_internet = df.groupby("InternetService")["MonthlyCharges"].sum().reset_index()

    fig = px.bar(
        revenue_internet,
        x="InternetService",
        y="MonthlyCharges",
        title="Monthly Revenue by Internet Service"
    )
    st.plotly_chart(fig, use_container_width=True)

fig = px.histogram(
    df,
    x="MonthlyCharges",
    color="Churn",
    title="Monthly Charges Distribution"
)

st.plotly_chart(fig, use_container_width=True)