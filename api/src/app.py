# @author: Alejandro Bejarano Gómez.

from os import environ, sys
import json
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.inspection import inspect
from flask_caching import Cache

## Prepare flask environment

app = Flask(__name__)
environ['FLASK_ENV'] = "development"
app.config['JSON_SORT_KEYS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("PSQL_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["CACHE_TYPE"] = 'redis'
app.config["CACHE_REDIS_URL"] = environ.get("REDIS_URI")
cache = Cache(app)
db = SQLAlchemy(app)


if app.config['SQLALCHEMY_DATABASE_URI'] == None:
    print ("Need database config")
    sys.exit(1)

## Serializer class to convert table view to jsonizable object
class Serializer(object):

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]

## Model used by SQLAlchemy to query database
class AirQ(db.Model):
    __tablename__ = 'air_quality'
    timestamp = db.Column('timeinstant', db.String, primary_key=True)
    id_entity = db.Column('id_entity', db.String)
    so2 = db.Column('so2', db.Float)
    no2 = db.Column('no2', db.Float)
    co = db.Column('co', db.Float)
    o3 = db.Column('o3', db.Float)
    pm10 = db.Column('pm10', db.Float)
    pm2_5 = db.Column('pm2_5', db.Float)

    def __init__(self, timestamp, id_entity, so2, no2, co, o3, pm10, pm2_5):
        self.timestamp = timestamp
        self.id_entity = id_entity
        self.so2 = so2
        self.no2 = no2
        self.co = co
        self.o3 = o3
        self.pm10 = pm10
        self.pm2_5 = pm2_5
    
    def serialize(self):
        return Serializer.serialize(self)

    def serialize_list(self):
        return Serializer.serialize_list(self)

    
@app.route("/air_quality")
@cache.cached(timeout=300)
def air_quality():
    air_quality = AirQ.query.all()
    return jsonify(AirQ.serialize_list(air_quality))
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False, port=8080)