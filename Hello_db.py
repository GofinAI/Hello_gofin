from flask import Flask, jsonify
import mysql.connector as db

app = Flask(__name__)

mydb = db.connect(
    host = "",
    user = "",
    password = "",
    database = ""
)

@app.route('/')
def index():
    # Execute a SELECT query
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM S_GROUP_DESC")
    results = cursor.fetchall()

    # Return the query results as JSON
    return jsonify(results)

if __name__ == '__main__':
    app.run()
