# Database Application README

## Project Overview

This Flask-based Database Application serves as a management system for film production-related entities, including Production Companies, Employees, Crew Members, Films, Grants, Grant Applications, and Contact Information. The application provides functionality to insert, retrieve, and report data for each entity.

## Directory Structure

The project directory has the following structure:

- **templates:** Contains HTML templates for rendering pages.
  - `all_tables_report.html`: Template for displaying a report of all tables in the database.
  - `contact_info_report_b.html`: Template for generating a report of contact information based on an employee ID.
  - `employee.html`: Form for inserting employee data.
  - `employee_report.html`: Template for displaying a report of employee data.
  - `film_report.html`: Template for generating a report of film data based on title.
  - `grant_application_report.html`: Template for generating a report of grant application data based on application ID.
  - `production_company.html`: Form for inserting production company data.
  - ... (other HTML templates)

- **routes:** Contains Python files defining routes for different entities.
  - `all_tables.py`: Route for displaying a report of all tables in the database.
  - `contact_information.py`: Routes for inserting, reporting, and viewing all contact information.
  - `employee.py`: Routes for inserting, reporting, and viewing employee data.
  - `film.py`: Routes for inserting, reporting, and viewing film data.
  - `grant.py`: Routes for inserting, reporting, and viewing grant data.
  - `grantapplication.py`: Routes for inserting, reporting, and viewing grant application data.
  - ... (other route files)

- **Tables_Creation.sql:** SQL script defining the creation of tables in the database.

- **app.py:** Main application file defining Flask routes and connecting to the database.

## Database Schema

The application uses the following database schema:

- **ProductionCompany:** Information about production companies.
- **Employee:** Details about employees working in the film industry.
- **Film:** Data related to films, including title and release year.
- **Grant:** Information about grants available for film production.
- **Crew:** Details about crew members involved in film production.
- **GrantApplication:** Data regarding grant applications submitted by production companies.
- **ContactInformation:** Information about contact details of employees.

## How to Run the Application

1. **Install Dependencies:**
   ```bash
   pip install Flask psycopg2

2. **Create Database:**
- Set up a PostgreSQL database and update the connection details in the `get_database_connection` function in `database.py`.

3. **Run the Application:**
```bash
python app.py
```

The application will be accessible at http://127.0.0.1:5000/.

## Access Routes:

- * Production Company: http://127.0.0.1:5000/production_company
- * Employee: http://127.0.0.1:5000/employee
- * Film: http://127.0.0.1:5000/film
- * Grant: http://127.0.0.1:5000/grant
- * Grant Application: http://127.0.0.1:5000/grantapplication
- * Contact Information: http://127.0.0.1:5000/ContactInformation
...

> View All Tables Report:
http://127.0.0.1:5000/view_all_tables

> View All Routes:
http://127.0.0.1:5000/


# Flask-FilmProductionDB-Management
