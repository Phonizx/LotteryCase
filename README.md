## Introduction

I created a service that powers a lottery system, incorporating several key features:
- It allows users to easily register and participate in the lottery.
- Participants can submit multiple entries for any ongoing lottery until it closes.
- Each day at midnight, the system automatically closes the current lottery and selects a random winner from that day’s entries.
- Users can check the winning entry for any date they choose.
- The service includes persistent storage to retain all lottery-related data.

# How to Run the Lottery System

1. At the project's root, create .env and copy .env.local values for local deployment
2. docker-compose build
3. docker-compose up -d
4. Go to http://localhost:8001/docs to start your journey or docs/Lottery.postman_collection.json there is the postman collection with the all endpoints requests/response


# Hot to run Integrations / unit tests
1. Install the all requirements + the dev.txt requirements:
    - pip install -r requirements/requirements.txt
    - pip install -r requirements/dev.txt
2. Go to /app/tests
3. Create .env and copy .env.test values for running the tests
4. and run docker-compose up -d
5. Go back to /app and run the test script ./tests/run_test.sh
