from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
import json
from producer import producer

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'mysimbdp-coredms'
app.config['MONGO_URI'] = 'mongodb+srv://MatteoAnelli:zHgn9oe2DpM2AJNV@mysimbdp-coredms-novzr.mongodb.net/test?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/document/<partid>', methods=['GET'])
def get_one(partid):
    documents = mongo.db.documents

    query  = documents.find({'part_id': int(partid)})
    if query:
        results = []
        for q in query:
            data = {
                'part_id': q['part_id'],
                'ts_date': q['ts_date'],
                'ts_time': q['ts_time'],
                'room': q['room']
            }
            results.append(data)
    else:
        results = 'No results found'
    return jsonify({'result': results})

@app.route('/document',methods=['POST'])
def insert_one():
    part_id = request.json['part_id']
    ts_date = request.json['ts_date']
    ts_time = request.json['ts_time']
    room = request.json['room']

    new_record = {
                'part_id': int(part_id),
                'ts_date': int(ts_date),
                'ts_time': ts_time,
                'room': room
            }
    message = producer(json.dumps(new_record))
    print(message)

    return message


if __name__ == '__main__':
    app.run(debug=True)


#TODO CHANGE PASSWORD
# TODO fix get
# TODO test insert
# TODO create api for initial delivery
# TODO DEAMON
