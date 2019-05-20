from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Microwave(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    turned_on = db.Column(db.String(100))
    power = db.Column(db.String(100))
    volume = db.Column(db.String(100))
    weight = db.Column(db.String(100))
    purpose = db.Column(db.String(100))

    def __init__(self, name, turned_on,
                 power, volume, weight, purpose):
        self.name = name
        self.turned_on = turned_on
        self.power = power
        self.volume = volume
        self.weight = weight
        self.purpose = purpose


class MicrowaveSchema(ma.Schema):
    class Meta:
        fields = ('name', 'turned_on', 'power', 'volume', 'weight', 'purpose')


microwave_schema = MicrowaveSchema(strict=True)
microwaves_schema = MicrowaveSchema(many=True, strict=True)


@app.route("/microwave", methods=["POST"])
def add_microwave():
    name = request.json['name']
    turned_on = request.json['turned_on']
    power = request.json['power']
    volume = request.json['volume']
    weight = request.json['weight']
    purpose = request.json['purpose']

    new_microwave = Microwave(name, turned_on, power, volume, weight, purpose)

    db.session.add(new_microwave)
    db.session.commit()

    return microwave_schema.jsonify(new_microwave)


@app.route("/microwave", methods=["GET"])
def get_microwave():
    all_microwaves = Microwave.query.all()
    result = microwaves_schema.dump(all_microwaves)
    return jsonify(result.data)


@app.route("/microwave/<microwave_id>", methods=["GET"])
def microwave_detail(microwave_id):
    microwave = Microwave.query.get(microwave_id)
    return microwave_schema.jsonify(microwave)


@app.route("/microwave/<microwave_id>", methods=["POST"])
def microwave_update(microwave_id):
    microwave = Microwave.query.get(microwave_id)
    microwave.name = request.json['name']
    microwave.turned_on = request.json['turned_on']
    microwave.power = request.json['power']
    microwave.volume = request.json['volume']
    microwave.weight = request.json['weight']
    microwave.purpose = request.json['purpose']
    db.session.commit()
    return microwave_schema.jsonify(microwave)


@app.route("/microwave/<microwave_id>", methods=["DELETE"])
def microwave_delete(microwave_id):
    microwave = Microwave.query.get(microwave_id)
    db.session.delete(microwave)
    db.session.commit()
    return microwave_schema.jsonify(microwave_schema)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
