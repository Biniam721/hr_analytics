CREATE Table hr_analytics (
    employee_id int,
    name varchar(100),
    gender varchar(20),
    age int,
    department varchar(20),
    job_role varchar(100),
    education varchar(50),
    experience_years FLOAT,
    salary numeric,
    bonus numeric,
    hire_date date,
    attrition varchar(10),
    satisfaction_score numeric,
    performance_rating numeric,
    overtime varchar(10),
    work_life_baance numeric,
    training_hours int,
    promotion_last_5years varchar(10),
    remote_work varchar(10),
    manager_rating numeric,
    absence_days int
);

--\COPY hr_data FROM '/Users/biniamtekeste/Desktop/hr analytics/data/hr_analytics_dataset.csv' DELIMITER ',' CSV HEADER;

