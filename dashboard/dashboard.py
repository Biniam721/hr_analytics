import streamlit as st
import pandas as pd
from db import engine

@st.cache_data
def load_data():
    query = """
    SELECT *
    FROM hr_analytics
    """
    return pd.read_sql(query, engine)

df = load_data()

# Page configuration
st.set_page_config(
    page_title="HR Analytics Dashboard",
    layout="wide"
)

st.title("📊 HR Analytics Dashboard")

# sidebar filters
st.sidebar.header("Filters")

department = st.sidebar.multiselect(
    "department",
    df["department"].unique(),
    default=df["department"].unique()
)

gender = st.sidebar.multiselect(
    "gender",
    df["gender"].unique(),
    default=df["gender"].unique()
)

attrition = st.sidebar.multiselect(
    "attrition",
    df["attrition"].unique(),
    default=df["attrition"].unique()
)

df = df[
    (df["department"].isin(department)) &
    (df["gender"].isin(gender)) &
    (df["attrition"].isin(attrition))
]

total_employees = len(df)

if len(df) > 0:
    attrition_rate = round(
        (len(df[df["attrition"]=="Yes"]) / len(df)) * 100,
        2
    )
else:
    attrition_rate = 0

avg_salary = round(df["salary"].mean(),2)

avg_satisfaction = round(
    df["satisfaction_score"].mean(),
    2
)

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Employees",
    f"{total_employees:,}"
)

col2.metric(
    "Attrition Rate",
    f"{attrition_rate}%"
)

col3.metric(
    "AvgsSalary",
    f"${avg_salary:,.0f}"
)

col4.metric(
    "Satisfaction",
    avg_satisfaction
)

import plotly.express as px

dept = (
    df["department"]
    .value_counts()
    .reset_index()
)

dept.columns = ["department","Employees"]

fig = px.bar(
    dept,
    x="department",
    y="Employees",
    title="Employees by department"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

attrition_dept = (
    df[df["attrition"]=="Yes"]
    .groupby("department")
    .size()
    .reset_index(name="Attrition_Count")
)

fig = px.bar(
    attrition_dept,
    x="department",
    y="Attrition_Count",
    title="Attrition by department"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

fig = px.histogram(
    df,
    x="salary",
    nbins=30,
    title="Salary Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

fig = px.scatter(
    df,
    x="experience_years",
    y="salary",
    color="department",
    title="Salary vs Experience"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

fig = px.scatter(
    df,
    x="training_hours",
    y="performance_rating",
    color="attrition",
    title="Training vs Performance"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

fig = px.box(
    df,
    x="attrition",
    y="satisfaction_score",
    title="Satisfaction vs Attrition"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

overtime = (
    df.groupby(
        ["overtime","attrition"]
    )
    .size()
    .reset_index(name="Count")
)

fig = px.bar(
    overtime,
    x="overtime",
    y="Count",
    color="attrition",
    barmode="group",
    title="Overtime Impact on Attrition"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("Key Insights")

st.write("""
• Identify departments with the highest employee turnover.

• Analyze whether overtime contributes to attrition.

• Evaluate employee satisfaction trends.

• Explore salary fairness across departments.

• Understand the relationship between training and performance.
""")