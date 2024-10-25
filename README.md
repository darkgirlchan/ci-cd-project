# ci-cd-project

## Project Overview

This project demonstrates a Continuous Integration/Continuous Deployment (CI/CD) pipeline using GitHub Actions for a Python application. The setup automates testing whenever code is pushed to the repository. The main function of this application is to add two numbers, and the tests ensure that this function operates correctly. This project is designed to be simple but effective in showcasing CI/CD automation.

## User Manual

#### Prerequisites

- **Python 3.9**: Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/).
- **Git**: Git must be installed to clone the repository and interact with GitHub. Download Git [here](https://git-scm.com/).

#### Setup Steps

1. **Clone the Repository**: Open a terminal or command prompt and run the following command to clone this repository:

   ```bash
   git clone https://github.com/your-username/ci-cd-project.git
   cd ci-cd-project

## Install Dependencies

2. python -m pip install -r requirements.txt

## Run the Application: To test the function locally, run the Python file:

3. python app/main.py

## Run Tests: 

4. python -m unittest discover tests

## Project Structure

ci-cd-project/
├── app/
│   └── main.py            # Main application code with add function
├── tests/
│   └── test_main.py       # Unit tests for add function
└── .github/
    └── workflows/
        └── ci.yml         # GitHub Actions workflow configuration