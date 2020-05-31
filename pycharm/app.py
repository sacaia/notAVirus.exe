from flask import Flask, make_response, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to the Not a Virus Project!'

############################# UN STATS #############################

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

@app.route('/unstats/391')
def UNstats391():
    response = make_response(render_template('template.json'))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    response.headers['Access-Control-Allow-Origin'] = '*'

    r = requests.get('https://services7.arcgis.com/gp50Ao2knMlOM89z/arcgis/rest/services/SH_AAP_MORT_3_9_1_2019Q3G01/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json')
    response.data = filterUNstats(r.content)
    return response

@app.route('/unstats/392')
def UNstats392():
    response = make_response(render_template('template.json'))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    response.headers['Access-Control-Allow-Origin'] = '*'

    r = requests.get('https://services7.arcgis.com/gp50Ao2knMlOM89z/arcgis/rest/services/SH_STA_WASH_3_9_2_2019Q3G01/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json')
    response.data = filterUNstats(r.content)
    return response

@app.route('/unstats/352')
def UNstats352():
    response = make_response(render_template('template.json'))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    response.headers['Access-Control-Allow-Origin'] = '*'

    r = requests.get('https://services7.arcgis.com/gp50Ao2knMlOM89z/arcgis/rest/services/SH_ALC_CONSPT_3_5_2_2019Q3G01/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json')
    response.data = filterUNstats(r.content)
    return response

@app.route('/unstats/372')
def UNstats372():
    response = make_response(render_template('template.json'))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    response.headers['Access-Control-Allow-Origin'] = '*'

    r = requests.get('https://services7.arcgis.com/gp50Ao2knMlOM89z/arcgis/rest/services/SP_DYN_ADKL_3_7_2_2019Q3G01/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json')
    response.data = filterUNstats(r.content)
    return response

@app.route('/unstats/651')
def UNstats651():
    response = make_response(render_template('template.json'))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    response.headers['Access-Control-Allow-Origin'] = '*'

    r = requests.get('https://services7.arcgis.com/gp50Ao2knMlOM89z/arcgis/rest/services/ER_H2O_IWRMD_6_5_1_2019Q3G01/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json')
    response.data = filterUNstats(r.content)
    return response

@app.route('/unstats/642')
def UNstats642():
    response = make_response(render_template('template.json'))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    response.headers['Access-Control-Allow-Origin'] = '*'

    r = requests.get('https://services7.arcgis.com/gp50Ao2knMlOM89z/arcgis/rest/services/ER_H2O_STRESS_6_4_2_2019Q3G01/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json')
    response.data = filterUNstats(r.content)
    return response

@app.route('/unstats/641')
def UNstats641():
    response = make_response(render_template('template.json'))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    response.headers['Access-Control-Allow-Origin'] = '*'

    r = requests.get('https://services7.arcgis.com/gp50Ao2knMlOM89z/arcgis/rest/services/ER_H2O_WUEYST_6_4_1_2019Q3G01/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json')
    response.data = filterUNstats(r.content)
    return response

@app.route('/unstats/621')
def UNstats621():
    response = make_response(render_template('template.json'))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    response.headers['Access-Control-Allow-Origin'] = '*'

    r = requests.get('https://services7.arcgis.com/gp50Ao2knMlOM89z/arcgis/rest/services/SH_SAN_HNDWSH_6_2_1_2019Q3G01/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json')
    response.data = filterUNstats(r.content)
    return response

@app.route('/unstats/611')
def UNstats611():
    response = make_response(render_template('template.json'))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    response.headers['Access-Control-Allow-Origin'] = '*'

    r = requests.get('https://services7.arcgis.com/gp50Ao2knMlOM89z/arcgis/rest/services/SH_H2O_SAFE_6_1_1_2019Q3G01/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json')
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

if __name__ == '__main__':
    app.run()
