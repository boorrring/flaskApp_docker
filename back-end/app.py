from flask import Flask, request
from dotenv import load_dotenv
import os
import pymongo

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')
print("MongoDB URI:", MONGO_URI)  # Debug print

client = pymongo.MongoClient(MONGO_URI)
db = client.test

collection = db['Flask_tut']


app = Flask(__name__)

@app.route('/')


@app.route('/submit', methods=['POST'])

def submit():
    #name = request.form.get('name','')
    #return 'Hello, '+ name + '!'
    form_data = dict(request.json)

    collection.insert_one(form_data)


    return 'Updated successfully'

@app.route('/view')
def view():
    data = collection.find()
    data = list(data)
    for item in data:
        print(item)
        del item['_id']
    
    data ={
        'data': data
        }
    return data


if __name__== '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)