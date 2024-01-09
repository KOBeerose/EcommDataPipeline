# EcommDataPipeline

This is a repo for the Data Engineer Coding Challenge.

- **[Part 0: Data Preparation](https://github.com/KOBeerose/EcommDataPipeline/tree/main/data_preparation)**: This section covers the steps of preparing and processing data.

- **[Part 1: Querying and Optimization](https://github.com/KOBeerose/EcommDataPipeline/tree/main/querying_and_optimization)**: This part involves populating and optimizing database.

- **[Part 2: Cohort Analysis](https://github.com/KOBeerose/EcommDataPipeline/tree/main/cohort_analysis)**: Here, you'll explored customer behavior and retention over time.
- **[Part 3: Elasticsearch](https://github.com/KOBeerose/EcommDataPipeline/tree/main/elasticsearch)**: This section focuses on integrating Elasticsearch for data monitoring.
- **[Part 4: BigQuery](https://github.com/KOBeerose/EcommDataPipeline/tree/main/bigquery)**: In this part, we integrated BigQuery as a data warehouse for data analytics.


## Launching Project

### Environment setup

**Create and Activate virtual environment**
```bash
pip install virtualenv
virtualenv coding_challenge
```
Activate the environment using:
```bash
.\coding_challenge\Scripts\activate
```
Or in Linux
```bash
source coding_challenge/Scripts/activate
```

**Clone the repo and install libraries**
```bash
git clone https://github.com/KOBeerose/EcommDataPipeline
```
Install libraries:
```bash
cd .\EcommDataPipeline
pip install -r requirements.txt
```
### Database Setup

**Install MySQL Server**

Download and install MySQL Server from the [official website](https://dev.mysql.com/downloads/mysql/). 

After installation in Windows:
```bash
setx PATH "%PATH%;C:\Program Files\MySQL\MySQL Server 8.0\bin"
```

Install in Linux using:
```bash
sudo apt install mysql-server
sudo systemctl start mysql
```

