from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello from backend one!</h1>"

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=80)