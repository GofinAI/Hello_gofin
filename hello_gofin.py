from flask import Flask, render_template
import mysql.connector as db

app = Flask(__name__)

mydb = db.connect(
    host = "gofin-aurora-instance-1.ci0rkg2zgzsd.us-east-1.rds.amazonaws.com",
    user = "malikam",
    password = "Malika@98966",
    database = "usda"
)

@app.route('/')
def index():
    # Execute a SELECT query
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM S_GROUP_DESC")
    results = cursor.fetchall()
    
    # Render the webpage with the query results
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run()
