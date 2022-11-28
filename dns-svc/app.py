from flask import Flask
from flask_restful import Resource, Api
import requests


app = Flask(__name__)
api = Api(app)


class Dns(Resource):
	def get(self):
		res = requests.get("https://networkcalc.com/api/dns/lookup/example.com")
		return res.json()


api.add_resource(Dns, '/')


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5003, debug=False)
