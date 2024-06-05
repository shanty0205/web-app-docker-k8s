# backend/app.py
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    with sqlite3.connect("data.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, value1 TEXT, value2 TEXT)''')
        conn.commit()

@app.route('/api/data', methods=['POST'])
def add_data():
    data = request.get_json()
    value1 = data.get('value1')
    value2 = data.get('value2')
    with sqlite3.connect("data.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO data (value1, value2) VALUES (?, ?)", (value1, value2))
        conn.commit()
    return jsonify({'message': 'Data inserted successfully!'}), 201

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
