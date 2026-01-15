# 14.	Connect a Flask application to an SQLite database and implement functionality to insert and retrieve user records.
from flask import Flask, request, jsonify #type:ignore
import sqlite3

app = Flask(__name__)
DATABASE = 'users.db'


# 🔹 Create database and table
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


# 🔹 Insert a new user
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (name, email) VALUES (?, ?)",
        (name, email)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "User added successfully"}), 201


# 🔹 Retrieve all users
@app.route('/users', methods=['GET'])
def get_users():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()

    users = []
    for row in rows:
        users.append({
            "id": row[0],
            "name": row[1],
            "email": row[2]
        })

    return jsonify(users), 200


if __name__ == "__main__":
    init_db()
    app.run(debug=True)

