from flask import Flask
from flask_restful import Resource, Api
import speedtest


app = Flask(__name__)
api = Api(app)


class SpeedTest(Resource):
	def get(self):
		st = speedtest.Speedtest()

		st.get_servers()
		best = st.get_best_server()

		download = st.download()
		upload = st.upload()
		ping = st.results.ping

		return {
			"destination": f"{best['host']}",
			"country": f"{best['country']}",
			"download": f"{download:.2f}",
			"upload": f"{upload: .2f}",
			"ping": f"{ping: .2f}"
		}


api.add_resource(SpeedTest, '/')


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5002, debug=False)
