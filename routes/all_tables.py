# Function to fetch all tables
def fetch_all_tables(connection):
    try:
        if connection:
            # Create a cursor
            cursor = connection.cursor()

            # Example: Querying data from a table named 'example_table'
            cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
            result = cursor.fetchall()

            # Close the cursor and connection when done
            cursor.close()

            # Return the query result (you can customize this)
            return result
        else:
            return None
    except Exception as e:
        # Handle any exceptions (e.g., database query error)
        return None