from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from fastapi_utils.guid_type import GUID


db = SQLAlchemy()
ma = Marshmallow()

class signal(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    signal_type = db.Column( db.String(50) )
    signal_message = db.Column( db.String(255) )



class SignalSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ("id", "signal_type", "signal_message")







  