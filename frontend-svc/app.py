from flask import Flask, render_template
from markupsafe import Markup
import requests
import os
import json


app = Flask(__name__, template_folder='./templates')


@app.route('/')
def index():
	ip_json = requests.get('http://backend-svc:5000/ip').json()
	speed_test = requests.get('http://backend-svc:5000/st').json()
	dns_json = requests.get('http://backend-svc:5000/dns').json()
	return render_template('index.html',
				ip_json=Markup(json.dumps(ip_json)),
				speed_test=Markup(json.dumps(speed_test)),
				dns_json=Markup(json.dumps(dns_json))
			      )


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=False)
