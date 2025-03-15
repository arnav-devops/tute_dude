from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_pymongo import PyMongo


app = Flask(__name__)


app.config["MONGO_URI"] = "mongodb+srv://itsincognitos:LNChKq610Pr0tFoR@cluster0.zj0hz.mongodb.net/users?retryWrites=true&w=majority"
mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.json  
        name = data.get("name")
        age = data.get("age")

        if not name or not age:
            return jsonify({"error": "Name and age are required"}), 400

        mongo.db.users.insert_one({"name": name, "age": age})

        return jsonify({"success": "Data submitted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/get_users', methods=['GET'])
def get_users():
    try:
        users = list(mongo.db.users.find({}, {"_id": 0}))  # Exclude _id field
        return jsonify(users), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/success')
def success():
    return "Data submitted successfully!"


if __name__ == '__main__':
    app.run(debug=True)
