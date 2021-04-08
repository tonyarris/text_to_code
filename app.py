from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
from main import gpt

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    # try:
    req = request.form['req']
    #print(req)
    response = gpt(req)
    #print(response)
    #print(jsonify(response))
    print(response)
    return jsonify(response)

    # except Exception as e:
    #     return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)