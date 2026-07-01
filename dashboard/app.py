import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Customer Churn Dashboard", layout="wide")

st.title("Customer Churn & Revenue Analytics Dashboard")

df = pd.read_csv("data/processed/cleaned_telco_churn.csv")

# Sidebar filters
st.sidebar.header("Filters")

contract = st.sidebar.multiselect(
    "Contract Type",
    df["Contract"].unique(),
    default=df["Contract"].unique()
)

internet = st.sidebar.multiselect(
    "Internet Service",
    df["InternetService"].unique(),
    default=df["InternetService"].unique()
)

payment = st.sidebar.multiselect(
    "Payment Method",
    df["PaymentMethod"].unique(),
    default=df["PaymentMethod"].unique()
)

filtered_df = df[
    (df["Contract"].isin(contract)) &
    (df["InternetService"].isin(internet)) &
    (df["PaymentMethod"].isin(payment))
]

# KPI cards
total_customers = filtered_df.shape[0]
churned_customers = filtered_df[filtered_df["Churn"] == "Yes"].shape[0]
churn_rate = churned_customers / total_customers * 100 if total_customers > 0 else 0
monthly_revenue = filtered_df["MonthlyCharges"].sum()
revenue_lost = filtered_df[filtered_df["Churn"] == "Yes"]["MonthlyCharges"].sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Customers", f"{total_customers:,}")
col2.metric("Churned Customers", f"{churned_customers:,}")
col3.metric("Churn Rate", f"{churn_rate:.2f}%")
col4.metric("Revenue Lost", f"${revenue_lost:,.2f}")

st.markdown("---")

# Charts
col1, col2 = st.columns(2)

with col1:
    churn_contract = filtered_df.groupby("Contract")["ChurnFlag"].mean().reset_index()
    churn_contract["Churn Rate"] = churn_contract["ChurnFlag"] * 100

    fig = px.bar(
        churn_contract,
        x="Contract",
        y="Churn Rate",
        title="Churn Rate by Contract Type",
        text="Churn Rate"
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    churn_internet = filtered_df.groupby("InternetService")["ChurnFlag"].mean().reset_index()
    churn_internet["Churn Rate"] = churn_internet["ChurnFlag"] * 100

    fig = px.bar(
        churn_internet,
        x="InternetService",
        y="Churn Rate",
        title="Churn Rate by Internet Service",
        text="Churn Rate"
    )
    st.plotly_chart(fig, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    fig = px.box(
        filtered_df,
        x="Churn",
        y="MonthlyCharges",
        title="Monthly Charges by Churn"
    )
    st.plotly_chart(fig, use_container_width=True)

with col4:
    fig = px.box(
        filtered_df,
        x="Churn",
        y="tenure",
        title="Tenure by Churn"
    )
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

st.subheader("High-Risk Customers")

high_risk = filtered_df[
    (filtered_df["Contract"] == "Month-to-month") &
    (filtered_df["MonthlyCharges"] >= 70) &
    (filtered_df["tenure"] <= 18) &
    (filtered_df["Churn"] == "No")
]

st.dataframe(high_risk)

st.download_button(
    label="Download High-Risk Customers",
    data=high_risk.to_csv(index=False),
    file_name="high_risk_customers.csv",
    mime="text/csv"
)