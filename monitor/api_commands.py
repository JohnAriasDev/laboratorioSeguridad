from hashlib import new
import json
from re import S
from flask import request
from flask_restful import Resource
from modelos import db, signal, SignalSchema

signal_schema = SignalSchema()
signals_schema = SignalSchema(many = True)

class postMessages(Resource):
    def post(self):

        new_signal = signal(
            id = str(request.json['id']),
            signal_type=str(request.json['signal_type']),
            signal_message=str(request.json['signal_message']),
       )
        db.session.add(new_signal)
        db.session.commit()
        return signal_schema.dump(new_signal)



def postJson(datos):
      datos_dict = json.loads(datos)
      new_signal = signal(
                id = datos_dict['id'],
                signal_type=datos_dict['signal_type'],
                signal_message=datos_dict['signal_message'],
        )
      db.session.add(new_signal)
      db.session.commit()
      return signal_schema.dump(new_signal)