from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Assuming you're using 'root' or another predefined user
MYSQL_USER = 'root'  # Or another user if you have a specific one
MYSQL_PASSWORD = #os.getenv('MYSQL_ROOT_PASSWORD')  # Using the root password from an env variable

# Update your database URI with the appropriate user and password
# Be sure to replace 'your-database-url' and 'database-name' with your actual database host and database name
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@your-database-url/database-name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define your model (Example)
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<Item {self.name}>'

# Ensure the table exists
db.create_all()

@app.route('/add', methods=['POST'])
def add_item():
    # Example JSON payload: {"name": "Item Name"}
    item_data = request.json
    item = Item(name=item_data['name'])
    db.session.add(item)
    db.session.commit()
    return jsonify({'message': 'Item added', 'item': item.name}), 201

@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify({'items': [item.name for item in items]})

if __name__ == '__main__':
    app.run(debug=True,port=5001)
