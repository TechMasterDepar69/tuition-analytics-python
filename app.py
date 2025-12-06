import streamlit as st
import pandas as pd
import sqlite3

# 1. Title
st.title("📊 Student Tuition Analytics (SQL Powered)")
st.write("Live analysis of student revenue from SQLite Database.")

# --- NEW: LOAD DATA FROM SQL ---
# 1. Connect to the database file
conn = sqlite3.connect('school.db')

# 2. Write the SQL Query (The Language of Data)
query = "SELECT * FROM students"

# 3. Load directly into Pandas
df = pd.read_sql(query, conn)

# 4. Close connection
conn.close()
# -------------------------------

# 3. Show the Data
if st.checkbox("Show Raw Data"):
    st.dataframe(df)

# 4. The Metrics
total_revenue = df['tuition'].sum()
total_students = len(df)
active_students = len(df[df['status'] == 'Enrolled'])

col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"฿{total_revenue:,}")
col2.metric("Total Students", total_students)
col3.metric("Active Enrolled", active_students)

# 5. The Chart
st.subheader("Revenue by Course")
st.bar_chart(df.set_index('course')['tuition'])

# 6. Sidebar Filters
st.sidebar.header("Filters")
status_filter = st.sidebar.selectbox("Select Status", df['status'].unique())

filtered_df = df[df['status'] == status_filter]
st.sidebar.write(f"Found {len(filtered_df)} students.")
st.sidebar.dataframe(filtered_df)

# --- REVENUE FORECASTER ---
st.divider()
st.header("🔮 Revenue Forecaster")

new_students = st.slider("Projected New Students", 0, 20, 5)
avg_price = st.number_input("Average Tuition", value=4500, step=500)

projected_income = new_students * avg_price
total_projected = total_revenue + projected_income

st.success(f"📈 Projected Extra Revenue: **฿{projected_income:,}**")

forecast_data = pd.DataFrame({
    'Scenario': ['Current', 'Projected'],
    'Amount': [total_revenue, total_projected]
})
st.bar_chart(forecast_data.set_index('Scenario'))
