# main application

# read the input data

import sys
import csv
import pymongo
from sourceIngestion import sourceIngestion

client = pymongo.MongoClient("mongodb+srv://MatteoAnelli:@mysimbdp-coredms-novzr.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_database('rooms')
records = db.documents

with open(sys.argv[1]) as f:
    reader = csv.reader(f)
    #next(reader) # skip header
    data = [r for r in reader]
insert = []
for i in data:
    line = sourceIngestion(*i)
    insert.append(line.map())

records.insert_many(insert)






