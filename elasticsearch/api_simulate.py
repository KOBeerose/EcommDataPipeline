from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch
import mysql.connector
import os

app = Flask(__name__)
es = Elasticsearch(["http://localhost:9200"])

# Database Connection
db_config = {
    'host': 'localhost',
    'user': os.environ.get('db_user'),
    'password': os.environ.get('db_pwd'),
    'database': 'coding_challenge_data'
}
db_connection = mysql.connector.connect(**db_config)

@app.route('/create_order', methods=['POST'])
def create_order():
    order_data = request.json

    # Insert order into the database
    cursor = db_connection.cursor()
    insert_query = "INSERT INTO orders (type, store_id, created_at) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (order_data['type'], order_data['store_id'], order_data['created_at']))
    db_connection.commit()
    order_id = cursor.lastrowid
    cursor.close()

    # Sync with Elasticsearch
    es.index(index="orders", id=order_id, body=order_data)

    return jsonify({'message': 'Order created', 'order_id': order_id})

if __name__ == '__main__':
    app.run(debug=True)
