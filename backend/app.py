from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb+srv://itsincognitos:LNChKq610Pr0tFoR@cluster0.zj0hz.mongodb.net/todo_db?retryWrites=true&w=majority"
mongo = PyMongo(app)

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    data = request.get_json()

    if not data or 'itemName' not in data or 'itemDescription' not in data:
        return jsonify({"error": "Invalid input"}), 400

    item = {
        "itemName": data['itemName'],
        "itemDescription": data['itemDescription']
    }

    # Insert into MongoDB
    mongo.db.todo_items.insert_one(item)

    return jsonify({"message": "To-Do item added successfully!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
