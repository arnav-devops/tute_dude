from flask import Flask, jsonify # type: ignore
import json

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def get_data():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)  
        return jsonify(data) 
    except Exception as e:
        return jsonify({"error": str(e)}), 500  
    
if __name__ == '__main__':
    app.run(debug=True)