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
