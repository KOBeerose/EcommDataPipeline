# Part 4: BigQuery

This section is dedicated to integrating BigQuery as a Data Warehouse for the Data Engineer Coding Challenge
## Tools Setup

### BigQuery Setup

**Google Cloud Project**

Ensure you have a Google Cloud Project with BigQuery enabled. For detailed instructions on setting up BigQuery, visit: https://cloud.google.com/bigquery/docs/quickstarts


**BigQuery Credentials**

Set up the service account key and configure the `GOOGLE_APPLICATION_CREDENTIALS` environment variable:

```bash
GOOGLE_APPLICATION_CREDENTIALS="path_to_your/service_account_key.json"
```

### Python Script for Data Transfer

The Python script is designed to extract data from MySQL and load it into BigQuery. Ensure you have the necessary Python librarie and change the credentials in the script.

**Running the Script**

Run the script to transfer data from MySQL to BigQuery. Adapt the script to match your database schema and BigQuery configuration:
```bash
python path_to_your_script.py
```

