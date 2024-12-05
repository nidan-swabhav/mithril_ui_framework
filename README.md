# Mithril UI Automation framework

This repository contains a Selenium-based test automation framework for interacting with and validating the functionality of Mithril UI. It includes features like login, batch creation, and dropdown selection, with data-driven testing support.

---

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Setup Instructions](#setup-instructions)
4. [Test Data Configuration](#test-data-configuration)
5. [Running Tests](#running-tests)
6. [Folder Structure](#folder-structure)
7. [Contributing](#contributing)

---

## Overview
The Mithril UI Automation Framework leverages:
- **Selenium WebDriver** for browser automation
- **Pytest** for test execution and parameterization
- **Page Object Model (POM)** for organized code structure
- **JSON** for dynamic locator and test data management

---

## Features
- Automated Login with role-based user selection
- Add Batch functionality:
  - Input validation (integer-only intake fields, non-empty fields)
  - Dropdown interaction with dynamic data
- Modularized Page Object Model for scalability
- Parameterized tests with Pytest
- JSON-driven locators and data for flexible updates

---

## Setup Instructions

### Prerequisites
1. Python 3.7+
2. Selenium WebDriver
3. Google Chrome/Chromium browser and [ChromeDriver](https://chromedriver.chromium.org/)
4. Virtual environment (optional but recommended)

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/nidan-swabhav/mithril_ui_framework.git]
   cd mithril_ui_automation
   cd tests

### Running Tests
1.command to run all tests:
```bash
  pytest
```
2.command to run tests with detail info:
```bash
  pytest -vvv
```
3.command to run test and print any statement (Mostly for debugging)
```bash
  pytest -s
```
### Folder Structure
```
  mithril_ui_automation/
  ├── tests/
  |     ├── assets/                 # Static assets (e.g., stylesheets)
  |     │   └── style.css           # CSS for HTML reports
  |     ├── pages/                  # Page Object Models (POMs)
  |     │   ├── batch_page.py       # Batch Page logic
  |     │   ├── bd_page.py          # BD Page logic
  |     │   ├── dashboard_page.py   # Dashboard Page logic
  │     |   ├── dropdowns.json      # Dropdown data for multiple pages
  |     │   ├── login.py            # Login Page logic
  |     │   └── training_page.py    # Training Page logic
  |     ├── test_cases/             # Test scripts
  |     │   ├── test_batchpage.py
  |     │   ├── test_bd.py
  |     │   ├── test_loginpage.py
  |     │   ├── test_training.py
  |     │   └── test_demo.py    # Sample/demo test case
  |     ├── conftest.py         # Pytest fixtures and configurations
  |     └── report.html         # Test execution report
  ├── pytest.ini              # Pytest configuration
  ├── requirements.txt        # Python dependencies
  └── README.md               # Project documentation
```
### Contributing
We welcome contributions to enhance this framework! Follow these steps:

1.Fork the repository.
2.Create a feature branch:
```bash
git checkout -b feature-name
```
3.Commit your changes:
```bash
git commit -m "Add new feature"
```
4.Push the branch:
```bash
git push origin feature-name
```
5.Open a pull request.

### Created by Nidan Gavali
