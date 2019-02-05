from os.path import join, dirname, realpath
import csv
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

airportsFile = join(dirname(realpath(__file__)), 'airports.csv')
airlineFile = join(dirname(realpath(__file__)), 'airlines.csv')



class start(Resource):
    def get(self):
        return 'It Works'


class GetAirportDetails(Resource):
    def get(self, APcode):
        csv_file = csv.reader(open(airportsFile, "r"), delimiter=",")
        for row in csv_file:
            if APcode == row[4]:
                return jsonify({'Airport ID': row[0], 'Name': row[1], 'City': row[2], 'Country': row[3], 'IATA': row[4], 'ICAO': row[5], 'Latitude': row[6], 'Longitude': row[7]})


class GetAirportName(Resource):
    def get(self, APcode):
        csv_file = csv.reader(open(airportsFile, "r"), delimiter=",")
        for row in csv_file:
            if APcode == row[4]:
                return jsonify({'Airport': row[1]})


class GetAirportLocation(Resource):
    def get(self, APcode):
        csv_file = csv.reader(open(airportsFile, "r"), delimiter=",")
        for row in csv_file:
            if APcode == row[4]:
                return jsonify({'Latitude': row[6], 'Longitude': row[7]})


class GetAirlineDetails(Resource):
    def get(self, IATA):
        csv_file = csv.reader(open(airlineFile, "r"), delimiter=",")
        for row in csv_file:
            if IATA == row[3]:
                return jsonify({'Airline ID': row[0], 'Name': row[1], 'Alias': row[2], 'IATA': row[3], 'ICAO': row[4], 'Callsign': row[5], 'Country': row[6], 'Active': row[7]})


class GetAirlineIATA(Resource):
    def get(self, AID):
        csv_file = csv.reader(open(airlineFile, "r"), delimiter=",")
        for row in csv_file:
            if AID == row[0]:
                return jsonify({'Name': row[1], 'IATA': row[3]})


api.add_resource(GetAirportDetails, '/airport/<string:APcode>')
api.add_resource(GetAirportName, '/airportname/<string:APcode>')
api.add_resource(GetAirportLocation, '/airportlocation/<string:APcode>')
api.add_resource(GetAirlineDetails, '/airline/<string:IATA>')
api.add_resource(GetAirlineIATA, '/airlinecode/<string:AID>')
api.add_resource(start, '/')


if __name__ == '__main__':
    app.run(debug=True)
