import psycopg2 

def get_database_connection():
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(
            user="kingsleyatuba",
            database="kingsleyatuba"
        )
        return connection
    except (Exception, psycopg2.Error) as error:
        print(f"Error while connecting to PostgreSQL: {error}")
        return None