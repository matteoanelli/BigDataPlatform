# Script to run the mongoDB Cluster

import pymongo

client = pymongo.MongoClient("mongodb+srv://MatteoAnelli:bigdatama@mysimbdp-coredms-novzr.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
