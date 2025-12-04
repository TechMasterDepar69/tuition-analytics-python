import streamlit as st
import pandas as pd

# 1. Title
st.title("Student Tuition Analytics")
st.write("Live analysis of student revenue and status.")

# 2. Create Fake Data (Since I don't have the live CSV connected yet)
data = {
    'Student Name': ['Somchai', 'Nong May', 'John', 'Sarah', 'Boss'],
    'Course': ['IELTS', 'Grammar', 'Business Eng', 'Conversation', 'Kids Class'],
    'Tuition': [5000, 3500, 8000, 4000, 3000],
    'Status': ['Enrolled', 'Trial', 'Enrolled', 'Paused', 'Graduated']
}

# Load into DataFrame
df = pd.DataFrame(data)

# 3. Show the Data
if st.checkbox("Show Raw Data"):
    st.dataframe(df)

# 4. The Metrics (The "KPI Cards")
total_revenue = df['Tuition'].sum()
total_students = len(df) 
active_students = len(df[df['Status'] == 'Enrolled'])

col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"฿{total_revenue:,}")
col2.metric("Total Students", total_students)
col3.metric("Active Enrolled", active_students)

# 5. The Bar Chart
st.subheader("Revenues by Course")
st.bar_chart(df.set_index('Course')['Tuition'])

# 6. Sidebar Filters
st.sidebar.header("Filter")
status_filter = st.sidebar.selectbox("Select Status", df['Status'].unique())

# Filter Logic
filtered_df = df[df['Status'] == status_filter]
st.sidebar.write(f"Found {len(filtered_df)} students.")
st.sidebar.dataframe(filtered_df)

# --- NEW SECTION: SCENARIO PLANNER ---
st.divider() # Adds a nice line separator
st.header("Revenue Forecaster")
st.write("Project your future income based on new enrollments.")

# 1. Input: How may new students? (Slider)
new_students = st.slider("Projected New Students", min_value=0, max_value=20, value=5)

# 2. Input: Average price per student (Number Input)
avg_price = st.number_input("Average Tuition per Student", value=4500, step=500)

# 3. The Math (Python Logic)
projected_income = new_students * avg_price
total_projected = total_revenue + projected_income

# 4. The Result (Visuals)
st.success(f"📈 If you add {new_students} students, you will earn an extra **฿{projected_income:,}**.")

# 5. Comparative Chart
forecast_data = pd.DataFrame({
    'Scenario': ['Current Revenue', 'Projected Revenue'],
    'Amount': [total_revenue, total_projected]
})

st.bar_chart(forecast_data.set_index('Scenario'))
