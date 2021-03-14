# Youtube API Project

## Project Overview

I'm using the Youtube API to pull channel statistics (total views, number of subscribers, number of videos) for my favourite Youtubers. The script runs once a day and is scheduled as cron job on AWS. The data is stored in csv files in an S3 bucket and ingested into a MySQL database instance. The database is automatically started 20 minutes before the API script runs and stopped 5 minutes after the data has been ingested to reduce uptime.

[Detailed setup of the pipeline](https://github.com/lb930/AWS/tree/main/S3%20to%20MySQL%20RDS)

## Starting and stopping the database

In order to minimise costs, the database is only briefly active to ingest data from csv files. [Start RDS](https://github.com/lb930/AWS/blob/main/Youtube%20API%20Cron%20Job/Start-RDS-Lambda/lambda_function.py) and [Stop RDS](https://github.com/lb930/AWS/blob/main/Youtube%20API%20Cron%20Job/Stop-RDS-Lambda/lambda_function.py) have been scheduled as cron job. A detailed tutorial can be found [here](https://www.totalcloud.io/blog/how-to-schedule-rds-instances-with-an-aws-lambda-function) or [here](https://www.sqlshack.com/automatically-start-stop-an-aws-rds-sql-server-using-aws-lambda-functions/).

## Youtube API

[youtube.py](https://github.com/lb930/AWS/blob/main/Youtube%20API%20Cron%20Job/Youtube-API-Lambda/youtube.py) does the heavy lifting of calling the API and retrieving channel ID, channel name, views, subscribers and video count from the official Youtube API. The script generates a new csv file every day which is stored on S3. The function is called in the lamda handler which runs once a day.

## S3 to MySQL database ingestion.

Once all the data has been saved on S3, it is [automatically uploaded](https://github.com/lb930/AWS/blob/main/Youtube%20API%20Cron%20Job/Youtube-S3-to-MySQl-Lambda/lambda_function.py) to a RDS instance where it can be queried and analysed.
