def fetch_contact_information_by_id(connection, employee_id):
    print(f"Entered fetch_contact_information with employee_id: {employee_id}")  # Debug print

    try:
        if connection:
            print("Establishing cursor for database connection.")  # Debug print
            # Create a cursor
            cursor = connection.cursor()

            # Querying data from the ContactInformation table for a specific employee
            query = "SELECT * FROM ContactInformation WHERE EmployeeID = %s"
            print(f"Preparing to execute query: {query} with employee_id: {employee_id}")  # Debug print
            cursor.execute(query, (employee_id,))  # Using parameterized query for safety
            print("Query executed, fetching results.")  # Debug print
            result = cursor.fetchall()

            print("Query results fetched, closing cursor.")  # Debug print
            # Close the cursor
            cursor.close()

            print(f"Fetched data: {result}")  # Debug print

            # Return the query result
            return result
        else:
            print("No database connection in fetch_contact_information")  # Debug print
            return None
    except Exception as e:
        # Handle any exceptions (e.g., database query error)
        print(f"Error in fetch_contact_information: {str(e)}")  # Debug print
        return None


# Function to insert data into the ContactInformation table
def insert_contact_information(connection, telephone_number, telephone_number_description, national_insurance_number, passport_number, employee_id):
    try:
        if connection:
            # Create a cursor
            cursor = connection.cursor()

            # Example: Insert data into ContactInformation table
            insert_query = """
            INSERT INTO ContactInformation (TelephoneNumber, TelephoneNumberDescription, NationalInsuranceNumber, PassportNumber, EmployeeID)
            VALUES (%s, %s, %s, %s, %s)
            """
            data_tuple = (telephone_number, telephone_number_description, national_insurance_number, passport_number, employee_id)

            # Execute the insert query
            cursor.execute(insert_query, data_tuple)
            connection.commit()

            # Close the cursor
            cursor.close()

            # Data inserted successfully
            return True
        else:
            return False
    except Exception as e:
        # Handle any exceptions (e.g., database query error)
        return False

# Function to fetch data from the ContactInformation table
def fetch_contact_information(connection):
    try:
        if connection:
            # Create a cursor
            cursor = connection.cursor()

            # Example: Querying data from the ContactInformation table
            cursor.execute("SELECT * FROM ContactInformation")
            result = cursor.fetchall()

            # Close the cursor
            cursor.close()

            print("Fetched data:", result)  # Debug print

            # Return the query result (you can customize this)
            return result
        else:
            return None
    except Exception as e:
        # Handle any exceptions (e.g., database query error)
        print("Error:", str(e))  # Debug print
        return None