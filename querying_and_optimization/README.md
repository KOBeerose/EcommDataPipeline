# Part 1: Querying & optimization

This is Querying & optimization part for the Data Engineer Coding Challenge.

## Database Setup

**MYSQL CLI**
```bash
mysql -u root -p
```
**Create Database**
```bash
CREATE DATABASE coding_challenge_data;
```
**Create User and Grant permission to Database**
```bash
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON coding_challenge_data.* TO 'username'@'localhost';
```

### Populating the Database

Before running the script make sure you have store the database credentials in a the following environement variables: 
*db_user* and *db_pwd*

**Choose how you want to Populate your DB**

Populate DB with Zomato Data 
```bash
python ./querying_and_optimization/insert_zomato_data.py
```
Populate DB with Generated data ( YOUCAN run them 🙂 both but make sure to create a new database for the second one )
```bash
python ./querying_and_optimization/insert_data_data.py
```
