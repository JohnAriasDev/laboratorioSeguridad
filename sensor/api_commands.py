from hashlib import new
import json
import re
from urllib.error import HTTPError
from flask import request
from flask_restful import Resource
import uuid
import boto3
from botocore.exceptions import ClientError
import requests
from flask_api import status
from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required

sendQueueUrl='https://sqs.us-east-1.amazonaws.com/804352613378/MisoQueue'
sqs_client =boto3.client('sqs', region_name='us-east-1',
                                aws_access_key_id="AKIA3WRZG3QBCY3A7T6R",
                                aws_secret_access_key="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")


class SensorResource(Resource):
    @jwt_required()
    def post(self):
        myuuid = uuid.uuid4()
        class new_signal: 
            id = str(myuuid) ,
            signal_type=request.json['signal_type'],
            signal_message=request.json['signal_message'],
        
   #     send_queue_message(new_signal)
        
        print("aca llega ", new_signal.id)
        try:
         response_notification = requests.post(f"http://127.0.0.1:5000/postSignals", json={"id": new_signal.id , "signal_type": new_signal.signal_type , "signal_message": new_signal.signal_message }, headers={"Content-Type":"application/json"})
         response_notification.raise_for_status()
        except :
         return ("message : Existe problema intentando conectar con servicio monitor",status.HTTP_503_SERVICE_UNAVAILABLE)
     
       
        if response_notification.ok:
            print(response_notification.json())
        else :
            print('error al estabelcer conexión con servicio monitor  status_code ', response_notification.status_code )
    



def send_queue_message(new_signal) :
    try:
        messageBody = {
            "id":str(new_signal.id),
            "signal_type":str(new_signal.signal_type),
            "signal_message": str(new_signal.signal_message)
        }
      

        response = sqs_client.send_message(QueueUrl=sendQueueUrl,
                                            MessageBody = json.dumps(messageBody),
                                            MessageAttributes = {
                                                'id' :{ 'DataType': 'String',
                                                        'StringValue': str(new_signal.id)
                                                }})
    except ClientError:
        raise
    else:
        return response

