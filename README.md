# QA Automation Portfolio

A QA Automation portfolio project built with Python, Pytest, Playwright, and Requests. This project demonstrates practical skills in UI testing, API testing, test organization, Page Object Model (POM), and Continuous Integration.

![CI](https://github.com/sergixoxo/qa-automation-portfolio/actions/workflows/tests.yml/badge.svg)

## Project Overview

This project contains automated tests for web applications and REST APIs.

The main objective is to develop practical QA automation skills by applying testing concepts such as:

- Positive and negative test scenarios.
- UI and API validation.
- Page Object Model (POM).
- Test organization using Pytest.
- Browser automation with Playwright.
- Continuous Integration with GitHub Actions.
- Test reporting and failure evidence.

## Technologies

- **Python 3.14** — Programming language.
- **Pytest** — Test execution and organization.
- **Playwright** — Browser automation and UI testing.
- **Requests** — HTTP requests and API testing.
- **pytest-html** — HTML test reporting.
- **Git and GitHub** — Version control.
- **GitHub Actions** — Continuous Integration (CI).

## Project Structure

```text
qa-automation-portfolio/
├── .github/
│   └── workflows/
│       └── tests.yml
├── pages/
│   └── saucedemo_page.py
├── tests/
│   ├── test_api.py
│   ├── test_homepage.py
│   ├── test_saucedemo.py
│   ├── test_saucedemo_login_negative.py
│   └── test_saucedemo_purchase.py
├── conftest.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Automated Test Coverage

### UI Testing — Playwright

**Homepage Testing**
- Verify successful HTTP response.
- Validate expected page title.
- Verify main heading visibility.

**SauceDemo Login Testing**
- Successful login with valid credentials.
- Login with invalid credentials.
- Login with empty username.
- Login with empty password.
- Login with locked-out user.

**SauceDemo Purchase Flow**
- Login with valid credentials.
- Verify product visibility and price.
- Add a product to the shopping cart.
- Validate cart contents.
- Complete checkout information.
- Validate checkout summary and total.
- Finish the purchase and verify confirmation.

### API Testing — Requests

**JSONPlaceholder API**
- Validate successful GET request for an existing post.
- Validate HTTP 404 response for a nonexistent post.
- Retrieve posts using query parameters (`userId`).
- Validate JSON response structure and data consistency.
- Validate response fields and data types.
- Send POST requests to create new posts.
- Validate HTTP 201 Created response.
- Validate POST response data against the submitted payload.

## Test Summary

| Test Category | Test Cases |
|---|---:|
| UI Testing | 9 |
| API Testing | 4 |
| **Total** | **13** |

## Test Architecture

The project uses the **Page Object Model (POM)** to separate page elements and interactions from test logic.

The `pages/` directory contains reusable page objects, while the `tests/` directory contains the automated test scenarios.

This approach improves code organization, maintainability, and reusability.

## Prerequisites

- Python 3.14
- Git
- Visual Studio Code or another code editor

## Installation

1. Clone the repository:

```bash
git clone https://github.com/sergixoxo/qa-automation-portfolio.git
cd qa-automation-portfolio
```

2. Create and activate a virtual environment:

**macOS / Linux**

```bash
python3.14 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

4. Install Playwright Chromium:

```bash
python -m playwright install chromium
```

## Running the Tests

Run the complete test suite:

```bash
pytest -v
```

Run UI tests:

```bash
pytest tests/test_homepage.py tests/test_saucedemo.py tests/test_saucedemo_login_negative.py tests/test_saucedemo_purchase.py -v
```

Run API tests:

```bash
pytest tests/test_api.py -v
```

Generate a local HTML report:

```bash
pytest -v --html=report.html --self-contained-html
```

## Continuous Integration

This project uses GitHub Actions to automatically execute the test suite.

The workflow is triggered by:

- Push events to the `main` branch.
- Pull requests targeting the `main` branch.

The pipeline performs the following steps:

1. Checks out the repository.
2. Sets up Python.
3. Installs project dependencies.
4. Installs Playwright and Chromium.
5. Executes all automated tests using Pytest.
6. Generates a self-contained HTML test report.
7. Uploads the HTML report as a GitHub Actions artifact.
8. Configures screenshots and Playwright traces to be retained when tests fail.

The current CI workflow successfully executes all **13 automated tests**.

[View GitHub Actions](https://github.com/sergixoxo/qa-automation-portfolio/actions)

## AI Usage

AI tools are used as learning and development assistants to:

- Understand QA automation concepts.
- Explore testing approaches and possible edge cases.
- Review code structure and identify potential improvements.
- Troubleshoot errors during development.

All suggested changes are reviewed, understood, and tested as part of the learning process.

## Future Improvements

- Implement API POST requests and resource creation tests.
- Add more UI test scenarios.
- Explore data-driven testing with Pytest parametrization.
- Implement additional test design techniques.
- Explore advanced automation and reporting strategies.

## Author

**Sergio Sanabria**

GitHub: [@sergixoxo](https://github.com/sergixoxo)

---

This project is part of my ongoing learning journey in Quality Assurance and Test Automation.
