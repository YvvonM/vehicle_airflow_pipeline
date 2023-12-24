## VEHICLES TRANSMISSION DATA PIPELINING
 The repo contains a data pipeline that is used for loading vehicles data to a postgres database and transforming the data.
 The pipeline uses airflow for orchastration and dbt for performing sql transformations.
 
 ### Pre-requisites
 To run this code, make sure you install:
 > - airflow
 > - dbt postgres adapter
 
### ARRANGEMENT OF THE FOLDER
The folder has 2 folders and one file:
> - The vehicles folder: This contains the dbt environment and the dbt models
> - The source folder: This contains utility functions that are used with the dag file
> - vehicle_dag.py: This is the file that contains the dag itself

## DAG OVERVIEW
**Overview of the DAG**
The Airflow DAG is made up of two tasks:

*1st task: get_csv_data*

PythonOperator Description: This job runs a Python function (get_csv_data) to load data from a CSV file.

*2nd task: transform_data*

DbtRunOperator Task Description: This task runs dbt models to transform the loaded data. The dir option defines the directory containing the dbt models, and the profiles_dir parameter gives the directory containing the dbt profiles file.

## DAG CONFIGURATION
DAG Configuration
The DAG is configured with the following parameters:

> - DAG ID: vehicle_db_dag
> - Start Date: December 22, 2023
> - Schedule Interval: Daily (@daily)
> - Owner: Admin
> - Email Notifications:
> - Receives failure notifications
> - Retries on failure up to 5 times with a delay of 2 minutes between retries

## Configure dbt:

Update the *profiles.yml* file with your database connection details.

**Run Airflow DAG:**
- Ensure your Airflow environment is running.
- Place the DAG file (vehicle_db_dag.py) in the dags directory of your Airflow installation.
- Access the Airflow UI and trigger the DAG manually or wait for the scheduled run.
### To get dbt documentation of the model run:
```
#to generate the documentation
dbt docs generate

#to view the documentation
dbt docs serve
```

You can also use the link below:

[Link to dbt Documentation](file:///C:/Users/User/Documents/airflow/vehicle/target/index.html)

 
