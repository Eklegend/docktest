from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)


@app.route('/')
def index():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="uxSYj50rQT",
        database = "test"
       
    )
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS test_table (id INT AUTO_INCREMENT PRIMARY KEY, message VARCHAR(255))")

    cursor.execute("INSERT INTO test_table (message) VALUES ('Hello from Flask')")


    cursor.execute("SELECT * FROM test_table")
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(results=result)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
