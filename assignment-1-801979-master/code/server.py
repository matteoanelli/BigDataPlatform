from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'mysimbdp-coredms'
app.config['MONGO_URI'] = 'mongodb+srv://MatteoAnelli:bigdatama@mysimbdp-coredms-novzr.mongodb.net/test?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/test', methods=['GET'])
def get_all_tests():
    test = mongo.db.test

    output = []

    for q in test.find():
        output.append()

if __name__ == '__main__':
    app.run(debug=True)


