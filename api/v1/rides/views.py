from flasgger import swag_from
from flask import Flask, jsonify, Blueprint
from flask_restful import reqparse
from .model import RidesModel

app = Flask(__name__)
rides = Blueprint('rides', __name__)


@rides.route('/api/v1/rides', methods=['GET'])
def returnAll():
    rides = RidesModel.returnAll()
    return jsonify({"rides": rides})

@rides.route('/api/v1/rides/<int:ride_id>', methods=['GET'])
def returnOne(ride_id):
    ride = RidesModel.returnOne(ride_id)
    return jsonify({"ride": ride})

@rides.route('/api/v1/rides/create', methods=['POST'])
def addOne():
    parser = reqparse.RequestParser()
    parser.add_argument("available_seats")
    parser.add_argument("date_and_time")
    parser.add_argument("from_")
    parser.add_argument("to")
    arguments = parser.parse_args()

    ride = RidesModel(arguments["available_seats"], arguments["date_and_time"], arguments["from_"],arguments["to"])
    new_ride = RidesModel.addOne(ride)
    return jsonify({"ride": new_ride})


@rides.route('/api/v1/rides/delete/<int:ride_id>', methods=['DELETE'])
def removeOne(ride_id):
    remaining_rides = RidesModel.removeOne(ride_id)
    return jsonify({'remaining_rides': remaining_rides})


