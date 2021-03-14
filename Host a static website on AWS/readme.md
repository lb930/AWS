# How to host a static website on AWS

## Project Description

This project hosts a static website designed by [Tanaka Jera](https://www.linkedin.com/in/tjera/) on AWS using S3, Route 53, Certificate Manager and CloudFront. The contents of the website are stored in a public S3 bucket. When a user goes to our domain name Route 53 routes the user to CloudFront. CloudFront gets an https certificate from AWS Certificate Manager and serves the website from an S3 bucket to the user.

<p>
    <img src="Screenshots/project.PNG" width="600" height="200" />
</p>
