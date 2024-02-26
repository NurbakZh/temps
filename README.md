[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/9TQ_ubhE)
# Bank Management System Project [LAB-TESTING]


## Overview

This project simulates a basic bank management system, designed to demonstrate the functionalities such as managing customers, accounts, and processing transactions. It's developed with a focus on testing, to utilize unit tests, mocks, and end-to-end (E2E) tests to ensure reliability and functionality.

## Background on Testing

Testing is an essential aspect of software development, ensuring that each part of the codebase works correctly and as expected. For this project, we emphasize three main keypoints:

- **Unit Tests**: Aim to test individual components or functions in isolation, ensuring that each piece of the system performs its intended task.
- **Mocking**: Involves simulating the behavior of real objects in controlled ways. Mocking is crucial for unit testing components that interact with external systems, like databases, to ensure tests are isolated and repeatable without side effects.
- **End-to-End (E2E) Tests**: Simulate real-user scenarios from start to finish, testing the system as a whole. E2E tests verify that all components of the application work together correctly to perform the intended tasks.

## Dependency Management with Poetry

For this project, we use [Poetry](https://python-poetry.org/) for dependency management and packaging. Poetry helps to simplify the management of project dependencies and environments.

To get started with Poetry:

1. Install Poetry by following the instructions on the [official documentation](https://python-poetry.org/docs/#installation).
2. Navigate to the project directory and run `poetry install` to install all dependencies defined in `pyproject.toml`.

```bash
sudo -H pip3 install poetry
poetry install
poetry add pytest pytest-mock
```


# LAB ASSIGNMENT

In this lab, you are required to create several tests. Please note that there are 5 main modules of the project under `app/` folder. 
You have to learn them and write tests in the corresponding files inside the `tests/`. 

For `Unit tests` - please add your tests in the files inside `tests/unit/test_*.py`. You'll need to add tests exclusively to these files.

> :warning: **Note:** if you add tests, all tests should pass for final submission.

> :warning: **Note:** the `app/` folder should not be altered and will be replaced in the autograding step.

> :warning: **Note:** use `poetry` for the Python environment and dependencies management.


### 1. Unit Tests (3pt)

- Create unit tests for the following modules to ensure each component functions correctly in isolation:
  - `database.py` (At least 5 tests)
  - `customer.py` (At least 2 tests)
  - `account.py`  (At least 2 tests)
  - `transaction.py`  (At least 2 tests)
  - `bank.py`  
- Utilize `unittest.mock` and `pytest-mock` to simulate external dependencies (code components from other modules) effectively.

- Add your tests in the corresponding files under `/tests/unit/` directory. 


- Apply mocks in testing for all modules to accurately simulate external dependencies without relying on the actual database.

> :warning: **Note:**  that mocking must be proper. For example, when you mock the database, the actual database file should not be touched by the system. 

### 2. End-to-End (E2E) Tests (1pt)

- **`test_bank.py`**: Acts as an E2E test, it should call combination of all scripts. It should simulate real-life usage scenarios of the bank system.

- Add your test in the corresponding file  `/tests/e2e/test_bank.py`

### 3. CI/CD with GitHub Actions (1pt)

- **Pipeline**: Implement a CI/CD pipeline using GitHub Actions, configured in the `main.yaml` file. This pipeline should automate the execution of tests.

> :warning: **Note:** The unit tests with mocks should be called on PUSH and the end-to-end on PULL.The unit tests with mocks should be called on when a commit is pushed and the end-to-end when a pull request is created.


## Running Tests

Tests are to be created inside the corresponding test files ( check the boiler plates in the files). 
To execute all tests, use the following Poetry command:

```bash
poetry run pytest
```

To run a specific test:
```bash
poetry run pytest tests/unit/test_*.py
```

## Project Structure
```
Bank/
│
├── app/
│   ├── __init__.py
│   ├── bank.py
│   ├── database.py
│   ├── customer.py
│   ├── account.py
│   └── transaction.py
│
└── tests/
    ├── __init__.py
    ├── unit/
    │   ├── __init__.py
    │   ├── test_account.py
    │   ├── test_customer.py
    │   ├── test_transaction.py
    │   └── test_database.py  
    └── e2e/
        ├── __init__.py
        └── test_bank.py
```
