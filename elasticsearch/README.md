# Part 3: Elasticsearch

This is Elasticsearch part for the Data Engineer Coding Challenge. note that YOUCAN run this locally but you need a lot of system ram 😎

In this part we will be using Elasticsearch for Orders active monitoring and analysis. to do that we use **JDBC driver** to connect our **MySQL Database** to **Logstash** that will push data to **Elasticsearch**
## Tools Setup

### Elasticsearch Setup

**Install Elasticsearch**

Download and Elasticsearch from the [official website](https://www.elastic.co/downloads/elasticsearch). 

Follow the setup in the documentation depending on you platform:
```bash
https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html
```
**Elasticsearch Config**

Add this line in config/elasticsearch.yml file 
```yaml
action.auto_create_index: .monitoring*,.watches,.triggered_watches,.watcher-history*,.ml*
```

Change the exisitng part of the configuration to the following ( Set true to false for these )
```yaml
xpack.security.http.ssl:
    enabled: false
    keystore.path: certs/http.p12

xpack.security.transport.ssl:
    enabled: false
    verification_mode: certificate
    keystore.path: certs/transport.p12
    truststore.path: certs/transport.p12
```
        
Change directory to bin folder and Start the Elasticsearch 
```bash
elasticsearch.bat
```
Verify that Elasticsearch is running by heading to:
```bash
http://localhost:9200/
```

### Logstash Setup

**Install Logstash**

Download and install Logstash from the [official website](https://www.elastic.co/downloads/logstash).

After installation verify that Logstash can run using:
```bash
bin\logstash.bat --version
```
Or in Linux:
```bash
bin/logstash --version
```

**Logstash Config**

In the Logstash conf file named config\logstash-sample.conf change the user and password to the crediantials for Elasticsearch
```json
elasticsearch {
    hosts => ["http://localhost:9200"]
    index => "test.logstash"
    user => "elastic"
    password => "changeme"
}
```

**Testing Elasticsearch & Logstash**
Copy the logstash-sample.conf to the config directory in Logstash folder and run the following:
```bash
bin\logstash -f .\config\logstash-sample.conf --config.reload.automatic
```
and then:
```bash
curl -u elastic:changme -X GET "localhost:9200/index_name/_search?pretty"
```

##  Sync the DB with Elasticsearch
We will use Logstash with its JDBC plugin to pull data from the database at regular intervals and push it to Elasticsearch.

### JDBC MySQL

**Download JDBC**

Download JDBC MySQL from the [official website](https://downloads.mysql.com/archives/c-j/) 

Unzip the folder and make sure to put the **mysql-connector-j-version.jar** file in a directory that exists in PATH.

**logstach.conf file**

The logstash.conf files contain the configuration that defines the JDBC input for each table in our database and specifies how this data should be output to Elasticsearch

**Which is better having daily or monthly indices and why?**

So our usecase is a fast growing company like Zomato or YOUCAN which have high data volume and high frequency operations. In this case I belive it's better to have **a daily indices**  because it will make it easier to manage the data lifecycle ( you can delete old indices without affecting newer data )