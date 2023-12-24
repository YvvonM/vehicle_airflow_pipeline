#importing libraries
from airflow.providers.postgres.hooks.postgres import PostgresHook

def get_csv_data():

    sql_st =  """
COPY tracks 
FROM 'C:\Users\User\Desktop\df_track.csv' 
WITH CSV HEADER DELIMITER ',';
"""
    sql_st2 = """
COPY trajectory 
FROM 'C:\Users\User\Desktop\df_trajectory.csv' 
WITH CSV HEADER DELIMITER ',';

"""
    
    pg_hook = PostgresHook( postgres_conn_id='postgres_connection', schema='public'),
    pg_hook.run(sql_st)
    pg_hook.run(sql_st2)