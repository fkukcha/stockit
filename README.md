# Stockit

*Note: PyCharm is the recommended IDE for this project.*

## Table of Contents
- [Getting Started](#getting-started)
  - [Clone the Repository](#clone-the-repository)
  - [Setting up the Virtual Environment](#setting-up-the-virtual-environment)
- [Usage](#usage)
- [Contributing](#contributing)
- [Moscow Requirements](#moscow-requirements)
  - [Muss-Kriterien (Must-Have Criteria)](#muss-kriterien-must-have-criteria)
  - [Soll-Kriterien (Should-Have Criteria)](#soll-kriterien-should-have-criteria)
  - [Kann-Kriterien (Can-Have Criteria)](#kann-kriterien-can-have-criteria)

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

## Moscow Requirements

### Muss-Kriterien (Must-Have Criteria)

* Das System muss ein Menü mit den Optionen Dashboard, Mitarbeiter, Lieferant, Kategorie und Produkte bereitstellen.
* Das System muss die Möglichkeit bieten, einen Mitarbeiter hinzuzufügen, zu aktualisieren und zu löschen.
* Das System muss die Möglichkeit bieten, nach einem Mitarbeiter nach Name, Kontakt oder E-Mail zu suchen.
* Das System muss die Möglichkeit bieten, einen Lieferanten hinzuzufügen, zu aktualisieren und zu löschen.
* Das System muss die Möglichkeit bieten, nach einem Lieferanten anhand der Rechnungsnummer zu suchen.
* Das System muss die Möglichkeit bieten, eine Kategorie hinzuzufügen und zu löschen.
* Das System muss die Möglichkeit bieten, ein Produkt hinzuzufügen, zu aktualisieren und zu löschen.
* Das System muss die Möglichkeit bieten, ein Produkt einer Kategorie und einem Lieferanten zuzuordnen.
* Das System muss die Möglichkeit bieten, den Status eines Produkts als aktiv oder inaktiv festzulegen.
* Das System muss die Möglichkeit bieten, nach einem Produkt nach Name, Kategorie oder Lieferant zu suchen.
* Das System kann die Möglichkeit bieten, einen Mitarbeiter mit dem Benutzertyp "Admin" oder "Mitarbeiter" hinzuzufügen.
* Das System sollte den Benutzern die Möglichkeit bieten, sich mit Benutzername und Passwort anzumelden.
* Das System sollte den Benutzern die Möglichkeit bieten, sich abzumelden.

### Soll-Kriterien (Should-Have Criteria)

* Das System sollte die Möglichkeit bieten, die aktuelle Uhrzeit und das aktuelle Datum beim Betreten der Startseite anzuzeigen.
* Das System muss eine Übersicht mit der Gesamtanzahl der Mitarbeiter, Lieferanten, Kategorien und Produkte anzeigen.
* Das System sollte eine Sales Option im Menü der Übersicht anzeigen.
* Das System sollte den Gesamtumsatz in der Übersicht anzeigen.
* Das System sollte ein Abrechnungssystem bereitstellen, in dem alle Produkte, ein Taschenrechner und die Kundenrechnungen abgebildet werden.
* Das System sollte den Rechnungsbetrag und den Zahlungsbetrag unter Berücksichtigung des Rabatts berechnen.
* Das System sollte eine Rechnung generieren.
* Das System sollte dem Benutzer die Möglichkeit bieten, die bevorzugte Menge der Produkte zum Warenkorb hinzuzufügen und zu aktualisieren.

### Kann-Kriterien (Can-Have Criteria)

* Das System kann dem Benutzer die Möglichkeit bieten, den Rechnungsbetrag auszudrucken.
* Das System kann dem Benutzer die Möglichkeit bieten, die Anzahl der aktiven Produkte im Lager zu sehen.
* Das System kann dem Benutzer die Möglichkeit bieten, ein Produkt aus dem Warenkorb zu entfernen.
* Das System kann dem Benutzer die Möglichkeit bieten, alle aktiven Produkte im Abrechnungssystem anzuzeigen.
* Das System kann dem Benutzer die Möglichkeit bieten, nach einem aktiven Produkt im Abrechnungssystem zu suchen.
* Das System kann dem Benutzer die Möglichkeit bieten, Kundenrechnungen einzusehen.
* Das System kann dem Benutzer die Möglichkeit bieten, nach Kundenrechnungen anhand der Rechnungsnummer zu suchen.

