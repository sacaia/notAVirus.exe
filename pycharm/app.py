from flask import Flask, make_response, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test')
def test():
    response = make_response(render_template('template.json'))
    response.headers['Access-Control-Allow-Origin'] = '*'
    print(response)
    return response


if __name__ == '__main__':
    app.run()
