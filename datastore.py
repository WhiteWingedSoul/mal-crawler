from google.cloud import datastore
import os

client = datastore.Client()
kind = os.getenv('KIND_NAME')

def store_object(listobject): 
    with client.transaction() as tran:
        for obj in listobject:
            key = client.key(kind)
            entity = datastore.Entity(key)
            for attr in obj:
                entity[attr] = obj[attr]
            tran.put(entity)
        