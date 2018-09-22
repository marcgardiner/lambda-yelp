# Lambda-Yelp

## Overview
This lambda function gets rating of location, using Yelp service and built based on Python 3.6

## Prerequisites:
 - please make sure that AWS account has the role `LambdaExecutionRole`
 - please set up configuration for Yelp in the file _dev.json_
 - please set up search parameters from AWS console

## How to run:
 1. Clone this repo - git clone https://github.com/marcgardiner/lambda-yelp.git
 2. Run build.sh in the following way:
   ./build.sh -p <path-to-lambda-yelp>
 3. Step 2 creates a .zip file in the <path-to-lambda-yelp> folder
 4. Upload the zip file created into AWS console
