# Consumer Deamon that listen from rabbit and ingest data
import pika, os, json
import pymongo

client = pymongo.MongoClient("mongodb+srv://MatteoAnelli:zHgn9oe2DpM2AJNV@mysimbdp-coredms-novzr.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_database('test')
records = db.documents

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqp://lglizjgp:ZHTrNmxKUo5sjiTgux_OOvmvSfnJUvao@moose.rmq.cloudamqp.com/lglizjgp')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='user') # Declare a queue
def callback(ch, method, properties, body):
    data = json.loads(body)
    records.insert(data)

channel.basic_consume('user',
                      callback,
                      auto_ack=True)
print(' [*] Waiting for messages:')
channel.start_consuming()

# TODO set global variable or parameters