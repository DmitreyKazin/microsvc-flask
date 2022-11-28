from flask import Flask
from flask_restful import Resource, Api
import socket
import requests


app = Flask(__name__)
api = Api(app)


class IpV4(Resource):
	def get(self):
		res = requests.get('https://api.ipify.org?format=json')
		ipv4 = res.json()['ip']
		return {
			'hostname': socket.gethostname(),
			'ipv4': ipv4
		}


api.add_resource(IpV4, '/ipv4')


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5001, debug=False)
