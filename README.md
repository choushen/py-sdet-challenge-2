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
- [ ] Token-based authentication implementation  
- [ ] Data validation for airport IATA codes  
- [ ] Distance calculation verification  
- [ ] Error handling  

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

##### **Non-Functional Tests**

- [ ] Performance Testing
  - [ ] Verify that the response time is within acceptable limits
- [ ] Load Testing
  - [ ] Verify that the system can handle a large number of requests

### **Assumptions and Justifications**  

...

### **Design**  

- The test framework will follow a modular structure; more specifically I will use a POM (Page Object Model) design pattern.  
- Test data will be managed externally to allow for easy updates.  
- Authentication handling will be implemented for protected endpoints.  
- Reporting will be integrated for test execution insights.  

## **Setup Instructions**  

Since you are pulling this repository, I'm going to assume you are familiar with Git and have it installed on your machine. If not, you can download it **[here](https://git-scm.com/downloads)**.  

You'll also need a couple of other things installed on your machine. See below for the prerequisites.  

### **Prerequisites**  

- Python 3.13  
- Pip 25.0  
- Docker  
- Docker Compose  
- Git  

## **Trouble Shooting Guide**

Any issues common issues you may encounter/what I encountered and how I resolved them will be included in this section of the document.

...

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

### Non-Functional Requirements

- WCAG Compliance (e.g. axe-core)
- Cross-Browser Testing
- Device resolution testing
- Track metrics and check console logs
- Measure response times to ensure speed and reliability

## **Author**  

**Name:** Jacob McKenzie
**Email:** jacob.mckenzie@icloud.com

