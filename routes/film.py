import psycopg2
from database import get_database_connection


def fetch_film_by_title(title):
    connection = get_database_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Film WHERE Title = %s", (title,))
            film = cursor.fetchone()
            return film
        except (Exception, psycopg2.Error) as error:
            print(f"Error while fetching film by title: {error}")
            return None
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()



def insert_film_data(MovieCode, Title, FirstReleaseYear):
    print("Connecting to the database to insert film data...")
    connection = get_database_connection()
    if connection:
        try:
            cursor = connection.cursor()

            # SQL query to insert film data
            insert_query = """
            INSERT INTO Film (MovieCode, Title, FirstReleaseYear)
            VALUES (%s, %s, %s)
            """
            data_tuple = (MovieCode, Title, FirstReleaseYear)

            # Debug prints to show the query and data
            print("Prepared Insert Query:", insert_query)
            print("Prepared Data Tuple:", data_tuple)

            # Execute the query
            print("Executing the insert statement...")
            cursor.execute(insert_query, data_tuple)
            connection.commit()
            print("Transaction committed successfully. Film data inserted.")
        except (Exception, psycopg2.Error) as error:
            print(f"Error in insert_film_data function: {error}")
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




def fetch_all_films():
    print("Connecting to the database to fetch all films...")
    connection = get_database_connection()
    if connection:
        try:
            cursor = connection.cursor()

            # SQL query to select all films
            cursor.execute("SELECT * FROM Film")

            # Fetch all the rows
            films = cursor.fetchall()
            print("Fetched all films successfully.")

            return films
        except (Exception, psycopg2.Error) as error:
            print(f"Error while fetching all films: {error}")
            return []
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
