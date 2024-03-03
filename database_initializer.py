import psycopg2
import os
connection = psycopg2.connect(
    user=os.environ.get('DB_USER'),
    password=os.environ.get('DB_PASSWORD'),
    host=os.environ.get('DB_HOST'),
    port=os.environ.get('DB_PORT'),
    database=os.environ.get('DB_NAME')
)

# Create a cursor object
cursor = connection.cursor()

# SQL query to create a table
create_table_query = ''' '''

# Execute the SQL query
cursor.execute(create_table_query)

# Commit the changes
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
