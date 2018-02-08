# Notes

## Requirements

- Problem:
  - Insurers:
    - Generic relationships. No database tables for each risk type.
    - Define their custom data model for risks
    - Create risk types
    - Attach as many fields as they like
  - Sample fields: first name, age, zip code, model, serial number, price
  - Field types: text, date, number, currency, enum,

- Deliverables:
  - Details
    - Host live instance
      - Bonus points for AWS with CloudFormation
      - Mega bonus points for AWS Lambda with Zappa
    - Send github repo to phil@britecore.com
  - Data:
    - [ ] Python file containing ORM classes
    - [ ] An entity-relationship diagram
  - Backend
    - [ ] Two endpoints (REST API)
      - [ ] Return a single risk type
      - [ ] List of all risk types (all data for each)
      - [ ] Tests
  - Frontend
    - [ ] Single page
    - [ ] Display field types in a form (show all fields types)
    - [ ] Fields should be appropriate widgets
    - [ ] Use ES6
    - [ ] Use Vue.js for bonus points

## Deployment to AWS

### Setup Flask app with Zappa on AWS Lambda

0. Move to the `backend` directory.

1. Deploy Flask project to AWS lambda

```
zappa deploy dev
```

Response contains something like:

```
# ...
Deployment complete!: https://u9hhr6ktg1.execute-api.us-east-1.amazonaws.com/dev
# ...
```

Take note of this URL.

2. Initialize the database with the demo data:

```
zappa invoke dev demo_fixtures.create_demo_data
```

### Serve static SPA on S3

0. Move to the `frontend` directory.

1. Build the frontend (note we're using the URL from the backend's deploy step)

```
API_BASE_URL='https://u9hhr6ktg1.execute-api.us-east-1.amazonaws.com/dev' yarn run build --report
```

2. Create bucket to host static files:

```
aws s3api create-bucket --bucket britecore-interview-kirbuchi --acl public-read
```

3. Allow it to serve a website:

```
aws s3 website s3://britecore-interview-kirbuchi/ --index-document index.html --error-document error.html
```

4. Sync files from the `frontend/dist` folder:

```
aws s3 sync dist s3://britecore-interview-kirbuchi --acl "public-read"
```
