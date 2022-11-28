from flask import Flask
from flask_restful import Resource, Api
import requests


app = Flask(__name__)
api = Api(app)


class Ip(Resource):
	def get(self):
		res = requests.get('http://ip-svc:5001/ipv4')
		return res.json()


class Speedtest(Resource):
	def get(self):
		res = requests.get('http://speedtest-svc:5002/')
		return res.json()


class Dns(Resource):
	def get(self):
		res = requests.get('http://dns-svc:5003/')
		return res.json()


api.add_resource(Ip, '/ip')
api.add_resource(Speedtest, '/st')
api.add_resource(Dns, '/dns')


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=False)
