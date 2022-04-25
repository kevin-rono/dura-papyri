import io

from flask import Flask, render_template, request, send_file


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/map")
def map():
    return render_template('map.html')

@app.route("/timeline")
def timeline():
    return render_template('timeline.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')