from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    if request.method == 'GET':
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)