# Part 0: Data Preparation

This is Data Preparation part for the Data Engineer Coding Challenge.

## Data Acquisition



### Wrangling Real Data

**Download and unzip dataset**

before running the command make sure that you have kaggle token (kaggle.json) inside the Users/user_name/.kaggle folder.
```bash
kaggle datasets download -d anas123siddiqui/zomato-database -p .\datasets\
```
Unzip the downloaded file using:
```bash
tar -xf .\datasets\zomato-database.zip -C .\datasets\zomato
```
Or in Linux
```
unzip ./datasets/zomato-database.zip -d ./datasets/zomato
```
You can also download it manually and unzip it inside data folder from [kaggle datasets](https://www.kaggle.com/datasets/anas123siddiqui/zomato-database?select=restaurant.csv)

**Run The data wrangling script**
```bash
python ./data_preparation/data_wrangling.py
```
check the datasets directory to verify the csv output files for the script

### Generating Fake Data 
the first approach we can use to get a significant amount of data is random generation using Faker library

**Run data_generation.py file**
```bash

```
