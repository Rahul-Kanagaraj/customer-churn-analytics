import streamlit as st
import pandas as pd
import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
)

st.set_page_config(page_title="Machine Learning", layout="wide")

st.title("Machine Learning - Churn Prediction")

df = pd.read_csv("data/processed/cleaned_telco_churn.csv")

model_df = df.drop(columns=["customerID", "Churn"])
model_df = pd.get_dummies(model_df, drop_first=True)

X = model_df.drop("ChurnFlag", axis=1)
y = model_df["ChurnFlag"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Accuracy", round(accuracy_score(y_test, y_pred), 3))
col2.metric("Precision", round(precision_score(y_test, y_pred), 3))
col3.metric("Recall", round(recall_score(y_test, y_pred), 3))
col4.metric("F1 Score", round(f1_score(y_test, y_pred), 3))
col5.metric("ROC-AUC", round(roc_auc_score(y_test, y_prob), 3))

st.markdown("---")

st.subheader("Confusion Matrix")

cm = confusion_matrix(y_test, y_pred)

cm_df = pd.DataFrame(
    cm,
    index=["Actual No Churn", "Actual Churn"],
    columns=["Predicted No Churn", "Predicted Churn"]
)

fig_cm = px.imshow(
    cm_df,
    text_auto=True,
    title="Confusion Matrix"
)

st.plotly_chart(fig_cm, use_container_width=True)

st.markdown("---")

st.subheader("Feature Importance")

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
}).sort_values(by="Importance", ascending=False).head(15)

fig = px.bar(
    importance,
    x="Importance",
    y="Feature",
    orientation="h",
    title="Top 15 Important Features"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

st.subheader("Simple Churn Risk Scoring")

tenure = st.slider("Tenure", 0, 72, 12)
monthly_charges = st.slider("Monthly Charges", 0, 120, 70)

contract = st.selectbox(
    "Contract Type",
    ["Month-to-month", "One year", "Two year"]
)

if contract == "Month-to-month" and tenure <= 12 and monthly_charges >= 70:
    st.error("Prediction: High Churn Risk")
elif contract == "Month-to-month" and tenure <= 24 and monthly_charges >= 60:
    st.warning("Prediction: Medium Churn Risk")
else:
    st.success("Prediction: Low Churn Risk")