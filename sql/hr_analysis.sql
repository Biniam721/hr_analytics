SELECT *
FROM hr_analytics
LIMIT 5;

-- Total Employee

SELECT 
    count(*) as total_employee
FROM hr_analytics;

-- Attrition Rate

SELECT 
    ROUND(100.0 * SUM(CASE WHEN attrition='Yes' 
    THEN 1 ELSE 0 END) / COUNT(*), 2) AS attrition_rate
FROM hr_analytics;

-- Average Salary by Department
SELECT
    department,
    round(avg(salary),2) as avg_salary
from hr_analytics
GROUP BY department
ORDER BY avg_salary desc;

--Departments with highest Attrition
SELECT
    department,
    count(*) as total_employee,
    sum(
        case WHEN attrition='Yes' THEN 1 ELSE 0 END
    ) as attrition_count
FROM hr_analytics
GROUP BY department
ORDER BY attrition_count desc;

-- Overtime Impact on Attrition
SELECT
    overtime,
    count(*) as total_employee,
    sum(
        case WHEN attrition='Yes' THEN 1 ELSE 0 END
    ) as attrition_count
FROM hr_analytics
GROUP BY overtime;

-- Salary vs Performance
SELECT
    performance_rating,
    round(avg(salary),2) as avg_salary
FROM hr_analytics
GROUP BY performance_rating
ORDER BY performance_rating desc;

--