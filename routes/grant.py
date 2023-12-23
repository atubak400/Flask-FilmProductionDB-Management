import psycopg2
from database import get_database_connection

def insert_grant_data(GrantTitle, FundingOrganization, MaxMonetaryValue, DeadlineForSubmission):
    connection = get_database_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            'INSERT INTO "Grant" (GrantTitle, FundingOrganization, MaxMonetaryValue, DeadlineForSubmission) VALUES (%s, %s, %s, %s)',
            (GrantTitle, FundingOrganization, MaxMonetaryValue, DeadlineForSubmission)
        )
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print(f"Error in insert_grant_data operation: {error}")
    finally:
        if connection:
            cursor.close()
            connection.close()


def fetch_grant_by_title(title):
    connection = get_database_connection()
    cursor = connection.cursor()
    grant_data = None

    try:
        cursor.execute('SELECT * FROM "Grant" WHERE GrantTitle = %s', (title,))
        grant_data = cursor.fetchone()
    except (Exception, psycopg2.Error) as error:
        print(f"Error in fetch_grant_by_title operation: {error}")
    finally:
        if connection:
            cursor.close()
            connection.close()

    return grant_data



def fetch_all_grants():
    print("fetch_all_grants: Establishing database connection...")
    connection = get_database_connection()
    cursor = connection.cursor()
    grants_data = []

    try:
        print("fetch_all_grants: Executing SQL query to fetch all grants...")
        cursor.execute('SELECT * FROM "Grant"')
        grants_data = cursor.fetchall()
        print(f"fetch_all_grants: Fetched {len(grants_data)} grants.")
    except (Exception, psycopg2.Error) as error:
        print(f"Error in fetch_all_grants operation: {error}")
    finally:
        if connection:
            print("fetch_all_grants: Closing cursor and connection...")
            cursor.close()
            connection.close()

    print("fetch_all_grants: Returning grants data...")
    return grants_data

