from flask import Flask, make_response, render_template
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

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
