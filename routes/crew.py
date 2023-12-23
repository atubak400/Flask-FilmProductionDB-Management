import psycopg2
from database import get_database_connection

def insert_crew_data(Role, RoleDescription, Bonus, EmployeeID, MovieCode):
    print("Connecting to the database...")

    # Print the received data and their types
    print(f"Received data - Role: {Role} (Type: {type(Role)}), "
          f"RoleDescription: {RoleDescription} (Type: {type(RoleDescription)}), "
          f"Bonus: {Bonus} (Type: {type(Bonus)}), "
          f"EmployeeID: {EmployeeID} (Type: {type(EmployeeID)}), "
          f"MovieCode: {MovieCode} (Type: {type(MovieCode)})")

    connection = get_database_connection()
    if connection:
        try:
            cursor = connection.cursor()

            # Notice that CrewID is not included in the columns list and the values
            insert_query = """
            INSERT INTO Crew (Role, RoleDescription, Bonus, EmployeeID, MovieCode)
            VALUES (%s, %s, %s, %s, %s)
            """
            data_tuple = (Role, RoleDescription, Bonus, EmployeeID, MovieCode)

            # Debug print the query and data
            print("Prepared Insert Query:", insert_query)
            print("Prepared Data Tuple:", data_tuple)

            # Execute the query
            print("Executing the insert statement...")
            cursor.execute(insert_query, data_tuple)
            connection.commit()
            print("Transaction committed successfully.")
        except (Exception, psycopg2.Error) as error:
            print(f"Error in insert_crew_data function: {error}")
            if connection:
                print("Transaction failed. Rolling back...")
                connection.rollback()
            raise error
        finally:
            # Close cursor and connection
            if cursor:
                cursor.close()
                print("Cursor closed.")
            if connection:
                connection.close()
                print("Database connection closed.")
    else:
        print("Failed to connect to the database.")




def fetch_crew_by_id(crew_id=None):
    connection = get_database_connection()
    if connection:
        try:
            cursor = connection.cursor()
            if crew_id:
                cursor.execute("SELECT * FROM Crew WHERE CrewID = %s", (crew_id,))
            else:
                cursor.execute("SELECT * FROM Crew")

            crew_members = cursor.fetchall()
            return crew_members
        except (Exception, psycopg2.Error) as error:
            print(f"Error while fetching crew: {error}")
            return []
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()


def fetch_all_crew():
    print("Attempting to connect to the database...")
    connection = get_database_connection()

    if connection:
        print("Successfully connected to the database.")
        try:
            cursor = connection.cursor()
            print("Cursor created.")

            print("Executing query to fetch all crew members...")
            cursor.execute("SELECT * FROM Crew")

            crew_members = cursor.fetchall()
            print(f"Fetched crew members: {crew_members}")

            return crew_members

        except (Exception, psycopg2.Error) as error:
            print(f"Error while fetching all crew members: {error}")
            return []

        finally:
            if cursor:
                print("Closing cursor.")
                cursor.close()
            if connection:
                print("Closing database connection.")
                connection.close()
    else:
        print("Failed to connect to the database.")

