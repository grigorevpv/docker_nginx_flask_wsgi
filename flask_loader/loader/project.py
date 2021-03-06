from statsd import StatsClient
from loader.services.CpuLoader import CpuLoader

from flask import Flask
application = Flask(__name__)

statsd = StatsClient(host='92.53.91.99',
                     port=8125,
                     prefix='web_server_one',
                     maxudpsize=512)


@application.route("/")
def hello():
    statsd.incr('get_request')

    loader = CpuLoader(3000)
    loader.load()

    return "<h1 style='color:blue'>Hello from backend one!</h1>"


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=80)

