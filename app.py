from flask import Flask, render_template, request, redirect, url_for
from routes.production_company import *
from routes.employee import *
from routes.crew import *
from routes.film import *
from routes.grant import *
from routes.contact_information import *
from routes.grantapplication import *
from database import get_database_connection


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/success')
def success():
    return render_template('success.html')


# Production Company Routes
@app.route('/production_company', methods=['GET', 'POST'])
def production_company():
    if request.method == 'POST':
        # Extract form data
        CompanyName = request.form['CompanyName']
        Address = request.form['Address']
        ZIPCode = request.form['ZIPCode']
        City = request.form['City']
        Nation = request.form['Nation']
        TypeOfOrganization = request.form['TypeOfOrganization']
        NumEmployees = int(request.form['NumEmployees'])
        NetValue = float(request.form['NetValue'])
        RegistrationDate = request.form['RegistrationDate']
        RegistrationOffice = request.form['RegistrationOffice']
        RegistrationFee = float(request.form['RegistrationFee'])

        # Call the function to insert data into the database
        try:
            insert_production_company_data(
                CompanyName,
                Address,
                ZIPCode,
                City,
                Nation,
                TypeOfOrganization,
                NumEmployees,
                NetValue,
                RegistrationDate,
                RegistrationOffice,
                RegistrationFee
            )
            return redirect(url_for('production_company_success'))
        except Exception as e:
            # Handle error and possibly show a failure message to the user
            print(e)
            # Here you may want to use Flask's flash() to show an error message
            # flash('An error occurred while adding the production company.')

    # If it's a GET request, just render the form
    return render_template('production_company.html')

@app.route('/production_company/success')
def production_company_success():
    return render_template('success.html')

@app.route('/production_company/report')
def production_company_report():
    company_name = request.args.get('reportCompanyName')
    company = fetch_production_companies(company_name)
    return render_template('production_company_report.html', companies=company)

@app.route('/production_company/all')
def view_all_companies():
    all_companies = fetch_all_production_companies()  
    return render_template('production_company_report.html', companies=all_companies)


# Employee Routes
@app.route('/employee', methods=['GET', 'POST'])
def employee():
    if request.method == 'POST':
        # Extract form data
        EmployeeID = request.form['EmployeeID']
        FirstName = request.form['FirstName']
        Surname = request.form['Surname']
        MiddleName = request.form['MiddleName']
        DateOfBirth = request.form['DateOfBirth']
        CommencementDate = request.form['CommencementDate']
        EmailAddress = request.form['EmailAddress']
        CompanyName = request.form['CompanyName']

        # Call the function to insert data into the database
        try:
            insert_employee_data(
                EmployeeID,
                FirstName,
                Surname,
                MiddleName,
                DateOfBirth,
                CommencementDate,
                EmailAddress,
                CompanyName
            )
            return redirect(url_for('employee_success'))
        except Exception as e:
            # Handle error and possibly show a failure message to the user
            print(e)
            # Here you may want to use Flask's flash() to show an error message
            # flash('An error occurred while adding the employee.')

    # If it's a GET request, just render the form
    return render_template('employee.html')

@app.route('/employee/success')
def employee_success():
    return render_template('success.html')

@app.route('/employee/report', methods=['GET'])
def employee_report():
    # Get the Employee ID for the report
    employee_id = request.args.get('reportEmployeeID')

    # Call the function to fetch the employee data based on Employee ID
    employees = fetch_employees_by_id(employee_id)

    return render_template('employee_report.html', employees=employees)

@app.route('/employee/all')
def view_all_employees():
    all_employees = fetch_all_employees()
    return render_template('employee_report.html', employees=all_employees)


# Crew Routes
@app.route('/crew', methods=['GET', 'POST'])
def crew():
    if request.method == 'POST':

        # Retrieve data from form
        Role = request.form['Role']
        RoleDescription = request.form['RoleDescription']
        Bonus = request.form['Bonus']
        EmployeeID = request.form['EmployeeID']
        MovieCode = request.form['MovieCode']

        try:
            # Attempt to insert crew data into the database
            insert_crew_data(
                Role, RoleDescription, Bonus, EmployeeID, MovieCode
            )
            print("Crew data inserted successfully.")
            return redirect(url_for('crew_success'))
        except Exception as e:
            print(f"An error occurred while adding the crew member: {e}")

    # Render the crew form if it's not a POST request or if insertion fails
    return render_template('crew.html')

@app.route('/crew/success')
def crew_success():
    return render_template('success.html')

@app.route('/crew/report', methods=['GET'])
def crew_report():
    crew_id = request.args.get('reportCrewID')
    crew_members = fetch_crew_by_id(crew_id)
    print("Debug - crew_members:", crew_members)
    return render_template('crew_report.html', crew=crew_members)

@app.route('/crew/all')
def view_all_crew():
    all_crew = fetch_all_crew()
    print("Debug - all_crew data:", all_crew) 
    return render_template('crew_report.html', crew=all_crew)


# Film Routes
@app.route('/film', methods=['GET', 'POST'])
def film():
    if request.method == 'POST':
        MovieCode = request.form['MovieCode']
        Title = request.form['Title']
        FirstReleaseYear = request.form['FirstReleaseYear']

        insert_film_data(MovieCode, Title, FirstReleaseYear)
        return redirect(url_for('film_success'))

    return render_template('film.html')

@app.route('/film/success')
def film_success():
    return render_template('success.html')

@app.route('/film/report')
def film_report():
    title = request.args.get('reportTitle')  # Update the parameter name to 'reportTitle'
    print(f"Debug - Received title for film report: {title}")

    film = fetch_film_by_title(title)
    print(f"Debug - Retrieved film data: {film}")

    return render_template('film_report.html', films=[film])

@app.route('/film/all')
def view_all_films():
    all_films = fetch_all_films()
    return render_template('film_report.html', films=all_films)


# All Tables
@app.route('/view_all_tables')
def fetch_all_tables():
    try:
        print("Attempting to connect to the database...")
        # Establish a database connection using your database module
        connection = get_database_connection()

        if connection:
            print("Database connection established.")
            # Create a cursor
            with connection.cursor() as cursor:
                # Querying all table names in the public schema
                cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
                result = cursor.fetchall()
                
                # Print result for debugging
                print("Query executed successfully. Result:", result)

                # Return the query result (you can customize this)
                return render_template('all_tables_report.html', result=result)

        else:
            print("Failed to connect to the database.")
            return "Failed to connect to the database."

    except Exception as e:
        # Handle any exceptions (e.g., database connection error)
        print(f"Error occurred: {str(e)}")
        return f"Error: {str(e)}"

    finally:
        # Close the connection when done, if it was successfully established
        if connection:
            print("Closing database connection.")
            connection.close()


# Contact Information Routes
@app.route('/ContactInformation', methods=['POST', 'GET'])
def insert_contact_info():
    if request.method == 'POST':
        # Retrieve data from the form
        telephone_number = request.form['TelephoneNumber']
        telephone_number_description = request.form['TelephoneNumberDescription']
        national_insurance_number = request.form['NationalInsuranceNumber']
        passport_number = request.form['PassportNumber']
        employee_id = request.form['EmployeeID']

        # Establish a database connection
        connection = get_database_connection()

        if connection:
            # Insert data into ContactInformation table
            if insert_contact_information(connection, telephone_number, telephone_number_description, national_insurance_number, passport_number, employee_id):
                # Data inserted successfully, you can redirect to a success page or do something else
                return redirect(url_for('contact_info_success'))
            else:
                return "Failed to insert data."
        else:
            return "Failed to connect to the database."

    # Render the form for inserting data
    print("Rendering contact_info.html")  # Added print statement
    return render_template('contact_info.html')

@app.route('/ContactInformation/report', methods=['GET'])
def generate_contact_info_report():
    print("Entered the generate_contact_info_report route")  # Debug print

    # Get the employee ID from the query parameter
    employee_id = request.args.get('reportEmployeeID')
    print(f"Received employee_id: {employee_id}")  # Debug print

    # Establish a database connection
    print("Attempting to establish a database connection...")  # Debug print
    connection = get_database_connection()
    print(f"Database connection established: {connection is not None}")  # Debug print

    if connection:
        print("Fetching contact information...")  # Debug print

        # Fetch data for the specified employee based on employee_id
        contact_info = fetch_contact_information_by_id(connection, employee_id)

        print("Fetched data, closing the database connection...")  # Debug print
        # Close the connection
        connection.close()

        if contact_info:
            print(f"Contact info fetched successfully: {contact_info}")  # Debug print
            # Return the query result in a template
            print("Rendering template with contact info...")  # Debug print
            return render_template('contact_info_report_b.html', contact_info=contact_info)
        else:
            print("Failed to fetch contact information data. No data returned.")  # Debug print
            return "Failed to fetch contact information data."
    else:
        print("Failed to connect to the database.")  # Debug print
        return "Failed to connect to the database."

@app.route('/contact_info_success')
def contact_info_success():
    return render_template('success.html')

@app.route('/ContactInformation/all')
def view_all_contact_info():
    # Establish a database connection
    connection = get_database_connection()

    if connection:
        # Fetch all data from ContactInformation table
        all_contact_info = fetch_contact_information(connection)

        # Close the connection
        connection.close()

        print("Fetched contact info data:", all_contact_info)  # Debug print

        if all_contact_info:
            # Return all data in a template
            return render_template('contact_info_report.html', all_contact_info=all_contact_info)
        else:
            print("Data is empty or not fetched.")  # Debug print
            return "Data is empty or not fetched."  # Update the message

    else:
        print("Failed to connect to the database.")  # Debug print
        return "Failed to connect to the database."



# Grant Routes
@app.route('/grant', methods=['GET', 'POST'])
def grant():
    if request.method == 'POST':
        GrantTitle = request.form['GrantTitle']
        FundingOrganization = request.form['FundingOrganization']
        MaxMonetaryValue = request.form['MaxMonetaryValue']
        DeadlineForSubmission = request.form['DeadlineForSubmission']

        insert_grant_data(GrantTitle, FundingOrganization, MaxMonetaryValue, DeadlineForSubmission)
        return redirect(url_for('grant_success'))

    return render_template('grant.html')

@app.route('/grant/success')
def grant_success():
    return render_template('success.html')

@app.route('/grant/report')
def grant_report():
    print("Entering grant_report function")

    # Retrieve the title from the request arguments
    title = request.args.get('reportTitle')
    print(f"Debug - Received title for grant report: {title}")

    if title:
        # Fetch grant data from the database using the title
        print(f"Debug - Calling fetch_grant_by_title with title: {title}")
        grant = fetch_grant_by_title(title)
        print(f"Debug - Retrieved grant data: {grant}")
    else:
        print("Debug - No title provided for grant report")
        grant = None

    # Check if the grant data was successfully retrieved
    if grant:
        print("Debug - Grant data found, rendering grant_report.html")
    else:
        print("Debug - No grant data found, rendering grant_report.html with no data")

    # Render the template with the grant data
    return render_template('grant_report.html', grants=[grant if grant else []])

@app.route('/grant/all')
def view_all_grants():
    print("Entering view_all_grants function")

    # Fetch all grants from the database
    print("Calling fetch_all_grants()")
    all_grants = fetch_all_grants()

    # Format the date in each grant
    formatted_grants = []
    for grant in all_grants:
        formatted_grant = list(grant)
        if formatted_grant[3]:  # Assuming the date is in the fourth position
            formatted_grant[3] = formatted_grant[3].strftime("%Y-%m-%d")
        formatted_grants.append(formatted_grant)

    print(f"Fetched {len(formatted_grants)} grants")
    print("Rendering grant_report.html with fetched grant data")
    return render_template('grant_report.html', grants=formatted_grants)


# GrantApplication Routes
@app.route('/grantapplication', methods=['GET', 'POST'])
def grant_application():
    print("Accessing /grantapplication route, Method:", request.method)

    if request.method == 'POST':
        ApplicationDate = request.form['ApplicationDate']
        print("ApplicationDate:", ApplicationDate)

        DesiredAmount = request.form['DesiredAmount']
        print("DesiredAmount:", DesiredAmount)

        Outcome = request.form['Outcome']
        print("Outcome:", Outcome)

        GrantTitle = request.form['GrantTitle']
        print("GrantTitle:", GrantTitle)

        CompanyName = request.form['CompanyName']
        print("CompanyName:", CompanyName)

        ApplicationId = request.form['ApplicationId']
        print("ApplicationId:", ApplicationId)

        insert_grant_application_data(ApplicationDate, DesiredAmount, Outcome, GrantTitle, CompanyName, ApplicationId)
        print("Data inserted successfully")

        return redirect(url_for('grant_application_success'))

    print("Rendering grant_application.html")
    return render_template('grant_application.html')

@app.route('/grantapplication/report')
def grant_application_report():
    print("Debug - Accessing /grantapplication/report route")

    applicationid = request.args.get('applicationId')
    print(f"Debug - Received application ID for grant application report: {applicationid}")

    if applicationid is not None:
        grant_application = fetch_grant_application_by_id(applicationid)
        print(f"Debug - Retrieved grant application data: {grant_application}")

        return render_template('grant_application_report.html', grant_applications=[grant_application])
    else:
        print("Debug - No application ID provided")
        # Optionally, you can redirect to another page or show an error message
        return render_template('grant_application_report.html', grant_applications=[])

@app.route('/grantapplication/success')
def grant_application_success():
    print("Rendering success.html after successful submission")
    return render_template('success.html')

@app.route('/grantapplication/all')
def view_all_grant_applications():
    print("Route /grantapplication/all accessed.")

    all_grant_applications = fetch_all_grant_applications()
    print(f"Data fetched from fetch_all_grant_applications: {all_grant_applications}")

    return render_template('grant_application_report.html', grant_applications=all_grant_applications)


if __name__ == '__main__':
    app.run(debug=True) 
