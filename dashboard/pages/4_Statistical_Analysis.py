import streamlit as st
import pandas as pd
from scipy.stats import ttest_ind, chi2_contingency, f_oneway
import plotly.express as px

st.set_page_config(page_title="Statistical Analysis", layout="wide")

st.title("Statistical Analysis")

df = pd.read_csv("data/processed/cleaned_telco_churn.csv")

st.subheader("1. Independent t-Test")

churned = df[df["Churn"] == "Yes"]["MonthlyCharges"]
not_churned = df[df["Churn"] == "No"]["MonthlyCharges"]

t_stat, p_value = ttest_ind(churned, not_churned, equal_var=False)

st.write("H0: Monthly charges are the same for churned and non-churned customers.")
st.write("H1: Monthly charges are different.")
st.metric("T Statistic", round(t_stat, 4))
st.metric("P Value", round(p_value, 6))

if p_value < 0.05:
    st.success("Reject H0: Monthly charges are significantly different.")
else:
    st.warning("Fail to reject H0.")

st.markdown("---")

st.subheader("2. Chi-Square Test")

table = pd.crosstab(df["Contract"], df["Churn"])
chi2, p, dof, expected = chi2_contingency(table)

st.write(table)
st.metric("Chi-Square Statistic", round(chi2, 4))
st.metric("P Value", round(p, 6))
st.metric("Degrees of Freedom", dof)

if p < 0.05:
    st.success("Reject H0: Contract type is associated with churn.")
else:
    st.warning("Fail to reject H0.")

st.markdown("---")

st.subheader("3. ANOVA Test")

groups = [
    group["MonthlyCharges"].values
    for name, group in df.groupby("InternetService")
]

f_stat, p_anova = f_oneway(*groups)

st.metric("F Statistic", round(f_stat, 4))
st.metric("P Value", round(p_anova, 6))

if p_anova < 0.05:
    st.success("Reject H0: Monthly charges differ across internet service types.")
else:
    st.warning("Fail to reject H0.")

st.markdown("---")

st.subheader("4. Correlation Heatmap")

corr = df[["tenure", "MonthlyCharges", "TotalCharges", "ChurnFlag"]].corr()

fig = px.imshow(
    corr,
    text_auto=True,
    title="Correlation Matrix"
)

st.plotly_chart(fig, use_container_width=True)