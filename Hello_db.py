import mysql.connector as db

# Establish a connection to the database
cnx = db.connect(
    host = "gofin-aurora-instance-1.ci0rkg2zgzsd.us-east-1.rds.amazonaws.com",
    user = "malikam",
    password = "Malika@98966",
    database = "usda"
)

# Create a cursor object to execute queries
cursor = cnx.cursor()

# Execute a query
query = "SELECT * FROM S_GROUP_DESC"
cursor.execute(query)

# Fetch the result
result = cursor.fetchall()

# Print the result
for row in result:
    print(row)

# Close the cursor and the connection
cursor.close()
cnx.close()
