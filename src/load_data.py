import pandas as pd
import sqlite3

# Read cleaned dataset
df = pd.read_csv("data/processed/cleaned_telco_churn.csv")

# Create SQLite database
conn = sqlite3.connect("customer_churn.db")

# Store dataframe as SQL table
df.to_sql(
    "telco_churn",
    conn,
    if_exists="replace",
    index=False
)

conn.commit()
conn.close()

print("Database created successfully!")