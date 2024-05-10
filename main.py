import pandas as pd
import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="dbname",
    user="user",
    password="password",
    host="host",
    port="5432"
)
# SQL query to select specific columns
sql_query = "SELECT code, country FROM master"

# Execute the query and fetch the results
df = pd.read_sql(sql_query, conn)

# Export DataFrame to Excel
df.to_excel('output.xlsx', index=False)

# Close the connection
conn.close()
