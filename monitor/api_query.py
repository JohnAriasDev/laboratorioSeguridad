from distutils.command.config import config
from email.message import Message
from logging import Logger
from queue import Empty
from re import M
from flask_restful import Resource
import json
import boto3
from botocore.config import Config
from modelos import signal , SignalSchema
from botocore.exceptions import ClientError
from api_commands import postMessages,postJson
import time

class receiveMessages(Resource):
    def get(self):
        control= True
        my_config = Config(region_name = 'us-east-1')
        sqs_resource = boto3.resource('sqs', config=my_config ,aws_access_key_id="AKIA3WRZG3QBCY3A7T6R",
                        aws_secret_access_key="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")
        queue = sqs_resource.get_queue_by_name(QueueName="MisoQueue")

  
        while(control):
        
            for message in queue.receive_messages(MessageAttributeNames=['id']):
                if message.message_attributes is not None:
                        id_text = message.message_attributes.get('id').get('StringValue')
                        registro_en_db = signal.query.filter(str(signal.id) == id_text).first()
                        if( registro_en_db is not None):
                            print("registrado en base de datos se elimina de la cola id=",id_text)
                      
                 #           message.delete()
                            time.sleep(1)
                        else :
                            
                            print("No registrado en base de datos inserta y se elimina de la cola id=",id_text)
                            postJson(message.body)
                  #          message.delete()
                    
                else:  
                    return ("message : Todos los mensajes han sido procesados")