from flask import Flask
from flask import request
import json
import requests

app = Flask(__name__)

@app.route('/localtrader/<system_symbol>')
def create(system_symbol=None):

  marketplaces_url = "https://api.spacetraders.io/v2/systems/" + system_symbol + "/waypoints?traits=MARKETPLACE"

  r = requests.get(marketplaces_url)

  return r.text



