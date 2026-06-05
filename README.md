# 📊 HR Analytics Dashboard

## Overview

The HR Analytics Dashboard is an interactive Business Intelligence solution designed to analyze workforce trends, employee performance, attrition patterns, compensation, and employee satisfaction. The project leverages PostgreSQL, SQL, Python, Plotly, and Streamlit to transform HR data into actionable insights that support strategic decision-making.

---

## Project Objectives

This project aims to help HR managers and business leaders answer critical workforce questions:

* What is the current employee attrition rate?
* Which departments experience the highest turnover?
* How does overtime affect employee retention?
* Is employee satisfaction related to attrition?
* How do salary and experience influence employee performance?
* What factors contribute to employee productivity?

---

## Dataset Information

The dataset contains 10,000 employee records with workforce, compensation, performance, and engagement metrics.

### Features

| Column                | Description                    |
| --------------------- | ------------------------------ |
| Employee_ID           | Unique employee identifier     |
| Name                  | Employee name                  |
| Gender                | Employee gender                |
| Age                   | Employee age                   |
| Department            | Department name                |
| Job_Role              | Employee position              |
| Education             | Education level                |
| Experience_Years      | Total years of experience      |
| Salary                | Annual salary                  |
| Bonus                 | Annual bonus                   |
| Hire_Date             | Hiring date                    |
| Attrition             | Employee left company (Yes/No) |
| Satisfaction_Score    | Employee satisfaction rating   |
| Performance_Rating    | Performance score              |
| Overtime              | Overtime status                |
| Work_Life_Balance     | Work-life balance score        |
| Training_Hours        | Training completed             |
| Promotion_Last_5Years | Promotion status               |
| Remote_Work           | Remote work status             |
| Manager_Rating        | Manager evaluation score       |
| Absence_Days          | Employee absence days          |

---

## Technologies Used

### Database

* PostgreSQL
* SQL

### Data Analysis

* Python
* Pandas
* NumPy

### Visualization

* Plotly
* Streamlit

### Version Control

* Git
* GitHub

---

## Dashboard Features

### Executive Overview

* Total Employees
* Attrition Rate
* Average Salary
* Average Satisfaction Score

### Workforce Analytics

* Employee Distribution by Department
* Gender Distribution
* Hiring Trends

### Attrition Analysis

* Attrition by Department
* Attrition by Overtime
* Attrition by Age Group
* Satisfaction vs Attrition

### Compensation Analysis

* Salary Distribution
* Salary by Department
* Salary vs Experience

### Performance Analytics

* Training Hours vs Performance
* Manager Rating Analysis
* Work-Life Balance Insights

---

## Database Setup

### Create Database

```sql
CREATE DATABASE hr_analytics;
```

### Create Table

```sql
CREATE TABLE hr_data (
    employee_id INT,
    name VARCHAR(100),
    gender VARCHAR(20),
    age INT,
    department VARCHAR(50),
    job_role VARCHAR(100),
    education VARCHAR(50),
    experience_years INT,
    salary NUMERIC,
    bonus NUMERIC,
    hire_date DATE,
    attrition VARCHAR(10),
    satisfaction_score NUMERIC,
    performance_rating NUMERIC,
    overtime VARCHAR(10),
    work_life_balance NUMERIC,
    training_hours INT,
    promotion_last_5years VARCHAR(10),
    remote_work VARCHAR(10),
    manager_rating NUMERIC,
    absence_days INT
);
```

---

## Sample SQL Queries

### Attrition Rate

```sql
SELECT
ROUND(
100.0 *
SUM(CASE WHEN attrition='Yes' THEN 1 ELSE 0 END)
/
COUNT(*),
2
) AS attrition_rate
FROM hr_data;
```

### Average Salary by Department

```sql
SELECT
department,
ROUND(AVG(salary),2) avg_salary
FROM hr_data
GROUP BY department
ORDER BY avg_salary DESC;
```

### Overtime Impact on Attrition

```sql
SELECT
overtime,
COUNT(*) total_employees,
SUM(CASE WHEN attrition='Yes' THEN 1 ELSE 0 END) attrition_count
FROM hr_data
GROUP BY overtime;
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/hr-analytics-dashboard.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Dashboard

```bash
streamlit run dashboard.py
```

---

## Key Business Insights

* Identify departments with the highest employee turnover.
* Evaluate workforce satisfaction levels.
* Analyze the relationship between overtime and attrition.
* Understand salary trends across departments.
* Discover factors influencing employee performance.

---

## Skills Demonstrated

* SQL Query Optimization
* PostgreSQL Database Management
* Data Cleaning and Transformation
* Exploratory Data Analysis (EDA)
* KPI Development
* Workforce Analytics
* HR Analytics
* Data Visualization
* Interactive Dashboard Development
* Business Intelligence Reporting

---

## Future Enhancements

* Machine Learning Attrition Prediction
* Employee Retention Risk Scoring
* Workforce Forecasting
* Real-Time PostgreSQL Integration
* Dashboard Deployment on Streamlit Cloud

---

## Author

### Biniam Tekeste

Data Analyst | SQL | PostgreSQL | Python | Data Visualization | Business Intelligence

LinkedIn:
[www.linkedin.com/in/biniam-tekeste-646599268](http://www.linkedin.com/in/biniam-tekeste-646599268)

Email:
[btekeste532@gmail.com](mailto:btekeste532@gmail.com)
