import os
import mysql.connector
from google.cloud import bigquery
from google.cloud.bigquery import LoadJobConfig, WriteDisposition


# Get credentials from environment variables
user = os.environ.get('db_user')
password = os.environ.get('db_pwd')

# Database connection parameters
mysql_config = {
    'host': 'localhost',
    'user': user,
    'password': password,
    'database': 'coding_challenge_db'
}


# BigQuery configuration
dataset_id = 'your_bigquery_dataset_id'
bq_client = bigquery.Client()

# Table names in your MySQL and BigQuery
tables = ['countries', 'stores', 'products', 'orders', 'order_items']

try:
    # Initialize a MySQL connection
    mysql_connection = mysql.connector.connect(**mysql_config)
    mysql_cursor = mysql_connection.cursor(dictionary=True)

    for table_name in tables:
        # Fetch data from MySQL database
        mysql_query = f"SELECT * FROM {table_name}"
        mysql_cursor.execute(mysql_query)
        rows = mysql_cursor.fetchall()

        if rows:
            # Define the BigQuery job configuration
            job_config = LoadJobConfig(write_disposition=WriteDisposition.WRITE_TRUNCATE)

            # Load data into BigQuery
            job = bq_client.load_table_from_json(rows, f"{dataset_id}.{table_name}", job_config=job_config)
            job.result()  # Wait for the job to complete

            # Confirm the load
            table = bq_client.get_table(f"{dataset_id}.{table_name}")
            print(f"Loaded {table.num_rows} rows into BigQuery table: {table_name}")
        else:
            print(f"No data to load for table: {table_name}")

except mysql.connector.Error as e:
    print(f"MySQL error: {e}")
except bigquery.BigQueryError as e:
    print(f"BigQuery error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    # Close MySQL connection
    if mysql_connection.is_connected():
        mysql_cursor.close()
        mysql_connection.close()
