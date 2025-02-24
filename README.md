# **Challenge 2 - API Automation Testing - Airport Gap**  

The challenge is to create and containerize a test automation framework for the **Airport Gap API** application.  

## **Task & Requirements**  

### **Requirements**  

#### **Framework Requirements**  

- Use Python with `requests` and `pytest`.  
- Implement test data management.  
- Implement token-based authentication.  
- Validate data for airport IATA codes.  
- Implement distance calculation verification.  
- Implement error handling.  
- Implement non-functional tests.  
- Implement reporting.  

#### **Standards and Code Quality**

- Add test documentation.
- Project setup instructions.  
- Test execution guidelines.  
- Environment configuration.  
- Troubleshooting guide.  
- Follow **PEP 8** standards.  

### **Task**  

Create an automated test suite for **[Airport Gap API](https://airportgap.com/)** that includes:  

- [ ] Testing of all endpoints  
- [x] Token-based authentication implementation  
- [x] Data validation for airport IATA codes  
- [ ] Distance calculation verification  
- [x] Error handling  

#### **Identified Test Cases**  

- Authentication Tests
  - [ ] Verify that valid token allows access to the protected endpoints
  - [ ] Verify that invalid token does not allow access to the protected endpoints returning a 401 status code
- [ ] Data Validation Tests
  - [ ] Validate that the airport IATA codes are valid
  - [ ] Validate that invalid airport IATA codes return 404
- Distance Calculation Tests
  - [ ] Verify that the distance calculation is accurate
- Favourite Management Tests
  - [ ] Verify that the favourite airports can be added
  - [ ] Verify that a favourite airport can be removed
  - [ ] Verify that all favourite airports can be cleared
- JSON Schema Validation Tests
  - [ ] Verify that the response schema is correct for GET requests
  - [ ] Verify that the request schema is correct for POST requests
  - [ ] Verify that the response schema is correct for DELETE requests
  - [ ] Verify that the response schema is correct for PATCH requests

##### **Non-Functional Tests**

- [ ] Performance Testing
  - [ ] Verify that the response time is within acceptable limits
- [ ] Load Testing
  - [ ] Verify that the system can handle a large number of requests

### **Design**  

- Test execution is kept separate from the API logic
- Test data is stored externally
- Common utilities are under a separate module
- .evn file is used for environment configuration

## **Setup Instructions**  

Since you are pulling this repository, I'm going to assume you are familiar with Git and have it installed on your machine. If not, you can download it **[here](https://git-scm.com/downloads)**.  

You'll also need a couple of other things installed on your machine. See below for the prerequisites.  

### **Prerequisites**  

- VSCode
- Python 3.13  
- Pip 25.0  
- Docker
- Git
- Secrets Zip File

### **How to run the tests using Docker**


1. Clone the repository to your local machine using the following command:  

```bash

git clone

```

2. Navigate to the project directory:  

```bash

cd py-sdet-challenge-2

```

3a. Open the **secrets_pt_2** folder and place the .env file in the root of the project diretory. Next go to https://airportgap.com/tokens/new and generate yourself a token. Open the .env file that you should have added to the root of the project directory and add the token string to the .env file as shown below:  

```bash
AUTH_TOKEN=<your_token_here>
```

3b. Drop the resources folder into the project directory.  It should contain 3 files:

- airport_data.json
- api_endpoints.json
- favourites.json

Once you are set up, you can run the tests using Docker.

4. build the docker image:  

```bash
docker build -t sdet_challenge .
```

5. Run the docker container:  

```bash
docker run --env-file .env -v ${PWD}/reports:/app/reports sdet_challenge pytest --html=reports/test_report.html
```

6. View the test report:  

#### Windows

```bash
Start-Process reports\test_report.html
```

#### MacOS/Linux

```bash
open reports/test_report.html
```

### **How to run the tests locally**

1. Clone the repository to your local machine using the following command:  

```bash

git clone git@github.com:choushen/py-sdet-challenge-2.git

```

2. Navigate to the project directory:  

```bash

cd py-sdet-challenge-2

```

3. Install the required dependencies:  

```bash

pip install -r requirements.txt

```

4a. Unzip the **secrets_pt_2.zip** file and place the .env file in the root of the project diretory. Next go to https://airportgap.com/tokens/new and generate yourself a token. Open the .env file that you should have added to the root of the project directory and add the token string to the .env file as shown below:  

```bash
AUTH_TOKEN=<your_token_here>
```

4b. Drop the resources folder into the project directory.  It should contain 3 files:
- airport_data.json
- api_endpoints.json
- favourites.json


5. Run the tests:  

```bash

pytest --html=reports/test_report.html

```

6. View the test report:

#### Windows

```bash

Start-Process reports\test_report.html

```

#### MacOS/Linux

```bash

open reports/test_report.html

```

## **Troubleshooting Guide**

Any issues common issues you may encounter/what I encountered and how I resolved them will be included in this section of the document.

### **Common Troubleshooting Issues & Fixes**  

| **Issue** | **Fix** |
|-----------|---------|
| **Reports missing** | `mkdir -p reports`, use **absolute paths** for `-v`. |
| **`.env` not working** | Pass vars manually with `--env VAR=value`. |
| **Docker can’t find `pytest`** | Ensure `pytest-html` is in `requirements.txt` and rebuild. |
| **Report won’t open** | Check inside container with `ls -la /app/reports`. |

If after following the setup instructions you encounter any issues, please go to the **[author](#author)** section of this document and reach out to me with any questions you might have.

## Future Considerations

### General Improvements

- Comprehensive logging
- Implementing a test data management system (e.g. Test Database/API)
- Use pydantic for data validation
  - Include more logging in the data_reader utility
- Shorter docstrings for PEP 8 compliance
- Implement allure reporting for better reporting (e.g. screenshots, videos, etc.)
- Implement a CI (e.g. Jenkins, GitHub Actions)
- Revise the project structure
- Containerise the test suite
- Add more edge cases to the test suite
  - Boundary testing
  - Adding an invalid airport to a favourite list
  - Token expiration handling (e.g. 401 status code)
  - Provide a comprehensive list of my postman test collection
- Generate a token using the API

### Non-Functional Requirements

- WCAG Compliance (e.g. axe-core)
- Cross-Browser Testing
- Device resolution testing
- Track metrics and check console logs
- Measure response times to ensure speed and reliability
- Jmeter or K6 for load testing
- Implement a security testing tool (e.g. OWASP ZAP)

## **Author**  

- **Name:** Jacob McKenzie
- **Email:** jacob.mckenzie@icloud.com
