import psycopg2
from database import get_database_connection

def insert_grant_application_data(ApplicationDate, DesiredAmount, Outcome, GrantTitle, CompanyName, ApplicationId):
    print("Starting insert_grant_application_data function")
    
    connection = get_database_connection()
    print(f"Database connection: {connection}")

    if connection is not None:
        try:
            cursor = connection.cursor()
            print("Cursor created successfully.")

            insert_query = """ INSERT INTO grantapplication (applicationdate, desiredamount, outcome, granttitle, companyname, applicationid) 
                               VALUES (%s, %s, %s, %s, %s, %s) """
            record_to_insert = (ApplicationDate, DesiredAmount, Outcome, GrantTitle, CompanyName, ApplicationId)

            print(f"Executing query: {insert_query}")
            print(f"With data: {record_to_insert}")

            cursor.execute(insert_query, record_to_insert)
            connection.commit()
            print("Record inserted successfully into grantapplications table")

        except (Exception, psycopg2.Error) as error:
            print("Failed to insert record into grantapplications table", error)

        finally:
            # Closing database connection.
            if connection:
                cursor.close()
                print("Cursor closed.")
                connection.close()
                print("PostgreSQL connection is closed")
    else:
        print("Failed to establish database connection.")


def fetch_grant_application_by_id(applicationid):
    connection = get_database_connection()
    if connection is not None:
        try:
            cursor = connection.cursor()
            select_query = """ SELECT * FROM grantapplication WHERE applicationid = %s """
            cursor.execute(select_query, (applicationid,))
            grant_application = cursor.fetchone()
            return grant_application

        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)
            return None

        finally:
            if connection:
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")


def fetch_all_grant_applications():
    print("Starting to fetch all grant applications...")
    connection = get_database_connection()
    print(f"Database connection: {connection}")

    if connection is not None:
        try:
            cursor = connection.cursor()
            print("Cursor created successfully.")

            select_query = "SELECT * FROM grantapplication"
            print(f"Executing query: {select_query}")
            cursor.execute(select_query)

            all_grant_applications = cursor.fetchall()
            print(f"Query executed successfully. Fetched data: {all_grant_applications}")
            return all_grant_applications

        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)
            return []

        finally:
            if connection:
                cursor.close()
                print("Cursor closed.")
                connection.close()
                print("PostgreSQL connection is closed")
    else:
        print("Failed to establish database connection.")

