from flask import Flask, request, jsonify
import sqlite3, logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('backend')

app = Flask(__name__)

@app.errorhandler(Exception)
def handle_exception(e):
    logger.error(f"An error occurred: {e}")
    return jsonify({'error': 'An internal error occurred'}), 500

def init_db():
    with sqlite3.connect("data.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, value1 TEXT, value2 TEXT)''')
        conn.commit()

@app.route('/api/data', methods=['POST'])
def add_data():
    try:
        data = request.get_json()
        value1 = data.get('value1')
        value2 = data.get('value2')
        if not value1 or not value2:
            raise ValueError("Both value1 and value2 are required")
        with sqlite3.connect("data.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO data (value1, value2) VALUES (?, ?)", (value1, value2))
            conn.commit()
        return jsonify({'message': 'Data inserted successfully!'}), 201
    except Exception as e:
        logger.error(f"Error inserting data: {e}")
        return handle_exception(e)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
