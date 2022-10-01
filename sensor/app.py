
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
from uuid import uuid4
from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required
from api_commands import SensorResource

app = Flask(__name__)
app_context = app.app_context()
app_context.push()
ma = Marshmallow(app)
app.config["JWT_SECRET_KEY"] = "secret-jwt"  # Change this!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False

jwt = JWTManager(app)


api = Api(app)

api.add_resource(SensorResource , '/signals')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5001,  ssl_context='adhoc')