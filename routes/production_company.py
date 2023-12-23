import psycopg2 
from database import get_database_connection


def insert_production_company_data(CompanyName, Address, ZIPCode, City, Nation, TypeOfOrganization, NumEmployees, NetValue, RegistrationDate, RegistrationOffice, RegistrationFee):
    connection = get_database_connection()
    if connection:
        try:
            # Create a cursor
            cursor = connection.cursor()

            # SQL query to insert data into the ProductionCompany table
            insert_query = """
            INSERT INTO ProductionCompany (CompanyName, Address, ZIPCode, City, Nation, TypeOfOrganization, NumEmployees, NetValue, RegistrationDate, RegistrationOffice, RegistrationFee)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            data_tuple = (CompanyName, Address, ZIPCode, City, Nation, TypeOfOrganization, NumEmployees, NetValue, RegistrationDate, RegistrationOffice, RegistrationFee)
            cursor.execute(insert_query, data_tuple)

            # Commit the transaction
            connection.commit()
        except (Exception, psycopg2.Error) as error:
            print(f"Error in insert_production_company_data function: {error}")
            if connection:
                connection.rollback()
            raise error
        finally:
            # Close the cursor and connection
            if cursor:
                cursor.close()
            if connection:
                connection.close()

def fetch_production_companies(company_name=None):
    connection = get_database_connection()
    if connection:
        try:
            # Create a cursor
            cursor = connection.cursor()

            # Check if a specific company name is given
            if company_name:
                # Use parameterized query to fetch a specific company
                cursor.execute("SELECT * FROM ProductionCompany WHERE CompanyName = %s", (company_name,))
            else:
                # Fetch all records
                cursor.execute("SELECT * FROM ProductionCompany")

            # Fetch the records
            companies = cursor.fetchall()
            return companies
        except (Exception, psycopg2.Error) as error:
            print(f"Error while fetching production companies: {error}")
            return []
        finally:
            # Closing the cursor and connection
            if cursor:
                cursor.close()
            if connection:
                connection.close()

def fetch_all_production_companies():
    connection = get_database_connection()
    if connection:
        try:
            # Create a cursor
            cursor = connection.cursor()

            # Execute the query to fetch all records
            cursor.execute("SELECT * FROM ProductionCompany")

            # Fetch all records
            companies = cursor.fetchall()
            return companies
        except (Exception, psycopg2.Error) as error:
            print(f"Error while fetching all production companies: {error}")
            return []
        finally:
            # Closing the cursor and connection
            if cursor:
                cursor.close()
            if connection:
                connection.close()