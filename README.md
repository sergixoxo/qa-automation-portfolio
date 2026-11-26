# QA Automation Portfolio

A QA Automation portfolio project built with Python, Pytest, Playwright, and Requests. This project demonstrates practical skills in UI testing, API testing, test organization, Page Object Model (POM), and Continuous Integration.

![CI](https://github.com/sergixoxo/qa-automation-portfolio/actions/workflows/tests.yml/badge.svg)


## Project Overview

This project demonstrates practical Quality Assurance (QA)
and Test Automation skills through functional testing,
automated UI and API testing, and requirements analysis.

The main objective is to apply testing concepts such as:

- Positive and negative test scenarios.
- UI and API validation.
- Page Object Model (POM).
- Test organization and parametrization using Pytest.
- Browser automation with Playwright.
- User stories and acceptance criteria.
- Functional test case design and manual execution.
- Requirements Traceability Matrix (RTM).
- Defect identification, reporting, and reproduction.
- Expected failure management (XFAIL).
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
├── docs/
│   ├── bugs/
│   │   ├── BUG-001.md
│   │   ├── BUG-002.md
│   │   └── BUG-003.md
│   ├── requirements/
│   │   ├── US-001.md
│   │   └── traceability-matrix.md
│   └── test-cases/
│       └── shopping-cart.md
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
- Validate shopping cart counter.
- Verify button transition from "Add to cart" to "Remove".
- Validate product name, price, and exact quantity.
- Complete checkout information.
- Validate checkout summary and total.
- Finish the purchase and verify confirmation.

**SauceDemo Defect Reproduction**
- BUG-001: Incorrect product images using `problem_user`.
- BUG-002: Remove button not working using `problem_user`.
- BUG-003: Checkout allowed with an empty cart using `standard_user` (potential defect based on a proposed business rule).

These scenarios are marked as expected failures (XFAIL).

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

| Test Category | Total | Passed | Expected Failures |
|---|---:|---:|---:|
| UI Testing | 12 | 9 | 3 |
| API Testing | 8 | 8 | 0 |
| **Total** | **20** | **17** | **3** |

### Latest Local Execution

- Total tests: 20.
- Passed: 17.
- Expected failures (XFAIL): 3.
- Unexpected failures: 0.
- Execution time: 15.43 seconds.

### Expected Failures

- [BUG-001](docs/bugs/BUG-001.md): Incorrect product images.
- [BUG-002](docs/bugs/BUG-002.md): Remove button not working.
- [BUG-003](docs/bugs/BUG-003.md): Checkout allowed with an empty cart.

Expected failures are documented using Pytest's
`xfail` marker to track reproduced defects.

BUG-003 is classified as a potential defect based
on a proposed business rule rather than an official
SauceDemo requirement.

## Requirements and Traceability

The project includes functional QA documentation
that demonstrates the relationship between business
requirements, acceptance criteria, test cases,
automated tests, and defect reports.

### Documentation

- [User Story — US-001](docs/requirements/US-001.md)
- [Functional Test Cases](docs/test-cases/shopping-cart.md)
- [Requirements Traceability Matrix (RTM)](docs/requirements/traceability-matrix.md)

### Requirements Coverage

| Metric | Result |
|---|---:|
| User Stories | 1 |
| Acceptance Criteria | 6 |
| Designed Test Cases | 6 |
| Automated Acceptance Criteria | 6 |
| Satisfied Acceptance Criteria | 5 |
| Unsatisfied Acceptance Criteria | 1 |
| Requirements Automation Coverage | 100% |
| Acceptance Criteria Satisfaction Rate | 83.33% |

### Defect Reports

- [BUG-001 — Incorrect Product Images](docs/bugs/BUG-001.md)
- [BUG-002 — Remove Button Not Working](docs/bugs/BUG-002.md)
- [BUG-003 — Checkout Allowed with an Empty Cart](docs/bugs/BUG-003.md)

The requirements were defined for portfolio purposes
and are not official SauceDemo requirements.

BUG-003 is classified as a potential defect based
on a proposed business rule.

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

### Run Tests in Headed Mode

Execute tests with a visible browser:

```bash
pytest -v --headed
```

### Run the Purchase Flow with Slow Motion

Execute purchase tests with a visible browser
and a 500 ms delay between Playwright actions:

```bash
pytest tests/test_saucedemo_purchase.py -v --headed --slowmo 500
```

### Display Expected Failure Reasons

Execute the complete test suite and display
the reasons for documented expected failures:

```bash
pytest -v -rx
```

## Continuous Integration

This project uses GitHub Actions to automatically
execute the test suite on pushes and pull requests
to the `main` branch.

The CI pipeline performs the following steps:

1. Checks out the repository.
2. Sets up Python 3.14.
3. Installs project dependencies.
4. Installs Playwright and Chromium.
5. Executes the automated test suite.
6. Generates an HTML test report.
7. Uploads test reports and available failure evidence
   as workflow artifacts.

### Regression Suite

The pipeline is configured to execute 20 automated
tests:

- 12 UI tests.
- 8 API tests.
- 3 documented expected failures.

Test reports and available failure evidence can be
downloaded from the GitHub Actions workflow artifacts.

Expected failures are tracked using Pytest's `xfail`
marker to distinguish documented defects from
unexpected test failures.

## AI Usage

AI tools are used as learning and development assistants to:

- Understand QA automation concepts.
- Explore testing approaches and possible edge cases.
- Review code structure and identify potential improvements.
- Troubleshoot errors during development.

All suggested changes are reviewed, understood, and tested as part of the learning process.

## Future Improvements

- Expand UI and API regression test coverage.
- Add cross-browser testing with Firefox and WebKit.
- Attach visual evidence to documented defect reports.
- Expand requirements traceability to additional modules.
- Improve test data management and environment configuration.
- Extend automated reporting and test execution metrics.
- Enhance checkout validation with explicit rejection signals.

## Author

**Sergio Sanabria**

GitHub: [@sergixoxo](https://github.com/sergixoxo)

---

This project is part of my ongoing learning journey in Quality Assurance and Test Automation.
