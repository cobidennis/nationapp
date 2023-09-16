
from flask import Flask, request
import redis

app = Flask(__name__)
version = "1.7.1"

r = redis.Redis(host="cache-server", port=6379)

@app.route("/getregion", methods = ["GET"])
def getregion():
    value ='<h1>Not found</h1>'
    country = request.args.get("country")
    try:
        city = r.get (country)
        value = '''<h1> {} is in {} </h1> <p><a href= "http://54.217.138.104">home</a>'''.format(city.upper(), country.upper())
    except:
        pass
    return  value

@app.route("/version")
def getversion():
    return version

@app.route("/saveregion", methods = ["GET"])
def saveregion():
    value = "<h1> Failed to save</h1>"

    country = request.args.get("country")
    city = request.args.get("city")
 
    try:
        r.set(country,city)
        value = '''<h1> {} is in {} saved successfully </h1><p><a href= "http://54.217.138.104">home</a>'''.format(city.upper(), country.upper())
    except:
        pass
    return  value


