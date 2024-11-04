# DataSync International Banking System

**A Comprehensive Banking Application Simulation**  
  
  If you are just here to view the project and don't want to go through the entire project description, check out this video!  
[DataSync International](https://youtu.be/4D3rZWvm1oI)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Acknowledgements](#acknowledgements)

## Introduction

DataSync International is a near-perfect model of a banking application developed as an extension of the Bank Simulator Part 1: Citizens' Financial. This project, comprising approximately 26,000 lines of code, was built using Python and MySQL, with Tkinter providing a user-friendly graphical interface. Over a span of six months, our team designed, developed, tested, and refined this application to simulate real-world banking operations effectively.

## Features

- **User Account Management**
  - Create new bank accounts
  - Secure login with OTP (One-Time Password) verification
  - Block and unblock accounts

- **Financial Transactions**
  - Deposit and withdraw funds
  - Transfer money between accounts

- **Additional Functionalities**
  - In-app calendar for scheduling
  - Chatbot for user assistance
  - Currency converter for multi-currency transactions

- **Security and Reliability**
  - Robust error handling
  - Consistent and secure database management using MySQL

## Technologies Used

- **Programming Language:** Python 3.8/3.9
- **Database:** MySQL Community Server 8.0
- **UI Framework:** Tkinter
- **Development Tools:** PyCharm, Visual Studio Code, Anaconda Spyder
- **Libraries and Modules:**
  - `mysql.connector`
  - `time`
  - `sys`
  - `datetime`
  - `calendar`
  - `threading`
  - `plyer`
  - `random`

## Installation

### Prerequisites

- **Hardware:**
  - PC with Core i3/i5 10th Gen or higher
  - 4-12 GB RAM

- **Software:**
  - Windows 10 x64
  - Python 3.8 or 3.9 installed
  - MySQL Community Server 8.0

### Steps

1. **Clone the Repository:**
```bash
git clone https://github.com/zaidmohammed7/Bank-Simulator-Part-2-DataSync-International.git
```

2. **Navigate to the Project Directory:**
   - Change your working directory to the cloned repository.

3. **Install Required Python Libraries:**
   - Install mysql-connector-python and plyer
```
pip install mysql-connector-python
pip install plyer
```

4. **Set Up the MySQL Database:**
   - Launch MySQL Community Server.
   - Create a new database named `datasync_international`.
   - Import the provided `.sql` file to set up the necessary tables and initial data.

5. **Configure Database Connection:**
   - Open the configuration file (e.g., `config.py`) and update the MySQL connection details (username, password, host, database).

6. **Run the Application:**
   - Execute the `SystemBootFile.py` script to start the banking application.

## Usage

1. **Launch the Application:**
   - Execute the `SystemBootFile.py` script to start the banking application.

2. **Create an Account:**
   - Navigate to the account creation section and fill in the required details.

3. **Login:**
   - Use your credentials to log in. An OTP will be sent for verification.

4. **Perform Transactions:**
   - Deposit, withdraw, or transfer money using the intuitive interface.

5. **Utilize Additional Features:**
   - Access the in-app calendar, chatbot, and currency converter from the main dashboard.

## Project Structure
```plaintext
.
├── MySQL Database Sources/
│   ├── Admin_Users_SQL_Source_MySQL.sql
│   ├── Client_Users_SQL_Source_MySQL.sql
│   ├── Sample DSI DataSet.xlsx
│   └── dsi_gmail_table___CONFIDENTIAL___SQL_SOURCE.sql
└── main_directory/
    ├── Banking_Calendar__reg__sub__utils__.py
    ├── LoginWindow.py
    ├── SystemBootFile.py
    ├── __pycache__/
    │   ├── Banking_Calendar__reg__sub__utils__.cpython-310.pyc
    │   ├── LoginWindow.cpython-310.pyc
    │   └── ...  # Other compiled Python files
    ├── account_window.py
    ├── admin/
    │   ├── admin_account.py
    │   └── admin_login.py
    ├── client_database.py
    ├── documents/
    │   └── Important.txt
    ├── images/
    │   ├── login.png
    │   └── ...  # Other image files
    ├── operation_functions_pyfiles.py
    └── temp/
        ├── check_conn1.py
        └── ...  # Other temporary files
```

## Acknowledgements

**Primary Contributors**:
  - Abhijeet Rajhans
  - Armaan Shaikh
  - Zaid Khan Md.

Thank you for exploring DataSync International! We hope this application serves as a robust simulation of real-world banking operations and provides valuable insights into full-stack application development.
