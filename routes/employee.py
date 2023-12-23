import psycopg2
from database import get_database_connection

def insert_employee_data(EmployeeID, FirstName, Surname, MiddleName, DateOfBirth, CommencementDate, EmailAddress, CompanyName):
    connection = get_database_connection()
    if connection:
        try:
            # Create a cursor
            cursor = connection.cursor()

            # SQL query to insert data into the Employee table with the new column order
            insert_query = """
            INSERT INTO Employee (EmployeeID, "firstname", Surname, MiddleName, DateOfBirth, CommencementDate, EmailAddress, CompanyName)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """

            data_tuple = (EmployeeID, FirstName, Surname, MiddleName, DateOfBirth, CommencementDate, EmailAddress, CompanyName)
            
            # Print the query and data for debugging
            print("Insert Query:", insert_query)
            print("Data Tuple:", data_tuple)
            
            cursor.execute(insert_query, data_tuple)

            # Commit the transaction
            connection.commit()
            print("Transaction committed successfully")
        except (Exception, psycopg2.Error) as error:
            print(f"Error in insert_employee_data function: {error}")
            if connection:
                connection.rollback()
            raise error
        finally:
            # Close the cursor and connection
            if cursor:
                cursor.close()
            if connection:
                connection.close()
                print("Connection closed")



def fetch_employees_by_id(employee_id=None):
    connection = get_database_connection()
    if connection:
        try:
            # Create a cursor
            cursor = connection.cursor()

            # Check if a specific employee ID is given
            if employee_id:
                # Use parameterized query to fetch a specific employee
                cursor.execute("SELECT * FROM Employee WHERE EmployeeID = %s", (employee_id,))
            else:
                # Fetch all records
                cursor.execute("SELECT * FROM Employee")

            # Fetch the records
            employees = cursor.fetchall()
            return employees
        except (Exception, psycopg2.Error) as error:
            print(f"Error while fetching employees: {error}")
            return []
        finally:
            # Closing the cursor and connection
            if cursor:
                cursor.close()
            if connection:
                connection.close()


def fetch_all_employees():
    connection = get_database_connection()
    if connection:
        try:
            # Create a cursor
            cursor = connection.cursor()

            # Execute the query to fetch all employees
            cursor.execute("SELECT * FROM Employee")
            
            # Fetch all records
            employees = cursor.fetchall()
            return employees
        except (Exception, psycopg2.Error) as error:
            print(f"Error while fetching all employees: {error}")
            return []
        finally:
            # Closing the cursor and connection
            if cursor:
                cursor.close()
            if connection:
                connection.close()
