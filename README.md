# Stockit

*Note: PyCharm is the recommended IDE for this project.*

## Table of Contents
- [Getting Started](#getting-started)
  - [Clone the Repository](#clone-the-repository)
  - [Setting up the Virtual Environment](#setting-up-the-virtual-environment)
- [Usage](#usage)
- [Contributing](#contributing)

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine.

### Clone the Repository

To clone this repository to your local machine, use the following command:

```bash
git clone https://github.com/fkukcha/stockit.git
```

### Setting up the Virtual Environment

Navigate to the project directory:

```bash
cd stockit
```

Ensure that you have pipenv installed. If not, run the following command:

```bash
pip install pipenv
```

Run the following commands to set up and activate the virtual environment:

```bash
pipenv install
pipenv shell
```

## Usage

### 1. Running the Application

To use the Stockit application, follow these steps:

#### a. Login

Run the following command to login:

```bash
python app/authentication/login.py
```

or

```bash
python3 app/authentication/login.py
```

##### Admin Credentials:

* Employee ID: (Find admin employee ID in `app/services/employee.py`)
* Password: (Find admin password in `app/services/employee.py`)

Optionally, to skip the login process for an admin, run:

```bash
python app/services/dashboard.py
```

or

```bash
python3 app/services/dashboard.py
```

This will redirect you to `app/services/dashboard.py`, where you'll have all the functionalities of an admin user.

##### Employee Credentials:

* Employee ID: (Find employee ID in `app/services/employee.py`)
* Password: (Find employee password in `app/services/employee.py`)

Optionally, to skip the login process for an employee, run:

```bash
python app/services/billing.py
```

OR

```bash
python3 app/services/billing.py
```

This will redirect you to `app/services/billing.py`, where you'll have all the functionalities of an employee.

#### b. Functionalities

##### Admin Functionalities:

* After logging in as an admin, you can access all functionalities in `app/services/dashboard.py`.

##### Employee Functionalities:

* After logging in as an employee, you can access all functionalities in `app/services/billing.py`.

## Contributing

If you'd like to contribute to this project, please follow these guidelines:

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Open a pull request.
