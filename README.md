# QA Automation Portfolio

A QA automation project built with Python, Pytest, and Playwright to practice web testing and develop practical software testing skills.

## Project Overview

This project contains automated end-to-end tests for the official Playwright website.

The goal is to practice essential QA automation concepts, including page navigation, HTTP response validation, page title verification, and element visibility assertions.

## Technologies

- **Python 3.14**
- **Pytest** — Test execution and organization
- **Playwright** — Browser automation
- **Git and GitHub** — Version control and project management

## Test Cases

| Test Case | Description |
|---|---|
| Homepage response | Verifies that the homepage responds with HTTP status 200. |
| Page title | Checks that the page title matches the expected value. |
| Main heading | Verifies that the main heading is visible. |

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

3. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Install the Playwright Chromium browser:

   ```bash
   python -m playwright install chromium
   ```

## Running the Tests

Run the test suite with:

```bash
python -m pytest tests/test_homepage.py -v
```

## Current Results

The initial test suite contains three automated tests, all of which passed in the initial local execution.

## Future Improvements

- Add more positive and negative test scenarios.
- Improve test organization and maintainability.
- Generate automated test reports.
- Integrate the test suite with GitHub Actions.
- Expand the portfolio with API automation tests.

## Author

**Sergio Sanabria**

GitHub: [@sergixoxo](https://github.com/sergixoxo)

---

This project is part of my ongoing learning journey in Quality Assurance and test automation.
