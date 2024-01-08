# EcommDataPipeline

This is a repo for the Data Engineer Coding Challenge.

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

