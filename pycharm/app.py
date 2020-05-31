from flask import Flask, make_response, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/SDG3/airpolution')
def airpolution():
    response = make_response(render_template('template.json'))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    response.headers['Access-Control-Allow-Origin'] = '*'

    r = requests.get('https://services7.arcgis.com/gp50Ao2knMlOM89z/arcgis/rest/services/SH_AAP_MORT_3_9_1_2019Q3G01/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json')

    response.data = filterUNstats(r.content)

    return response

@app.route('/test')
def test():
    response = make_response(render_template('template.json'))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    response.headers['Access-Control-Allow-Origin'] = '*'

    r = requests.get('https://ghoapi.azureedge.net/api/WHS9_92')
    response.data = r.content

    return response

def filterUNstats(text):
    ret = []

    j = json.loads(text)
    print(j)
    for i in range(len(j["features"])):
        dic = {}
        dic["Country"] = j["features"][i]["attributes"]["geoAreaName"]
        dic["Year"] = j["features"][i]["attributes"]["latest_year"]
        dic["Value"] = j["features"][i]["attributes"]["value_latest_year"]
        ret.append(dic)

    ret = json.dumps(ret)
    return ret

if __name__ == '__main__':
    app.run()
