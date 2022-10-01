
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
from api_query import receiveMessages
from api_commands import postMessages
from modelos import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///signal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'

app_context = app.app_context()
app_context.push()
db.init_app(app)
db.create_all()
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)


api.add_resource(receiveMessages, '/getSignals'),
#api.add_resource(validateMessageintoDB, '/getSignals/<string:message_id>')
api.add_resource(postMessages, '/postSignals')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5001)