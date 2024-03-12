from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Assuming you're using 'root' or another predefined user
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'uxSYj50rQT'
# Update your database URI with the appropriate user and password
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/my_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name):
        self.name = name

@app.route('/add', methods=['POST'])
def add_item():
    data = request.get_json()
    item = Item(name=data['name'])
    db.session.add(item)
    db.session.commit()
    return jsonify({'message': 'Item added successfully!'}), 201

@app.route('/items', methods=['GET'])
def get_items():
    items_list = Item.query.all()
    items = [{'id': item.id, 'name': item.name} for item in items_list]
    return jsonify({'items': items})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # This now runs within an application context
    app.run(debug=True, host='0.0.0.0', port=5000)
