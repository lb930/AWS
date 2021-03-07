# Youtube API Project

## Project Overview

I'm using the Youtube API to pull channel statistics (total views, number of subscribers, number of videos) from a few Youtubers. The script runs once a day and is scheduled as cron job on AWS. The data is stored in csv files in an S3 bucket and ingested into a MySQl database instance. The database is automatically started 20 minutes before the API script runs and stopped 5 minutes after the data has been ingested.
