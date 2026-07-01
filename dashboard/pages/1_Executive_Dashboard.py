import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Executive Dashboard", layout="wide")

st.title("Executive Dashboard")

df = pd.read_csv("data/processed/cleaned_telco_churn.csv")

total_customers = len(df)
churned_customers = len(df[df["Churn"] == "Yes"])
churn_rate = churned_customers / total_customers * 100
monthly_revenue = df["MonthlyCharges"].sum()
revenue_lost = df[df["Churn"] == "Yes"]["MonthlyCharges"].sum()
avg_tenure = df["tenure"].mean()

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Customers", f"{total_customers:,}")
col2.metric("Churned Customers", f"{churned_customers:,}")
col3.metric("Churn Rate", f"{churn_rate:.2f}%")
col4.metric("Revenue Lost", f"${revenue_lost:,.2f}")
col5.metric("Avg Tenure", f"{avg_tenure:.1f} months")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    churn_counts = df["Churn"].value_counts().reset_index()
    churn_counts.columns = ["Churn", "Count"]

    fig = px.pie(
        churn_counts,
        names="Churn",
        values="Count",
        title="Customer Churn Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    contract_churn = df.groupby("Contract")["ChurnFlag"].mean().reset_index()
    contract_churn["Churn Rate"] = contract_churn["ChurnFlag"] * 100

    fig = px.bar(
        contract_churn,
        x="Contract",
        y="Churn Rate",
        title="Churn Rate by Contract"
    )
    st.plotly_chart(fig, use_container_width=True)

st.subheader("High-Risk Customers")

high_risk = df[
    (df["Churn"] == "No") &
    (df["Contract"] == "Month-to-month") &
    (df["MonthlyCharges"] >= 70) &
    (df["tenure"] <= 18)
]

st.dataframe(high_risk.head(50))