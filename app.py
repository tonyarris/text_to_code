from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/query',methods=['POST'])
def query():
    query = request.form.to_dict()
    print("Your query was ".format(query))
    response = query(query)
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)