import io
import mysql.connector
import os
from os.path import join, dirname, realpath
import pandas as pd
import json
import datetime
import base64

from flask import Flask, render_template, request, send_file, redirect, url_for

import secretkeys

app = Flask(__name__)

# enable debugging mode
app.config["DEBUG"] = True

# Upload folder
UPLOAD_FOLDER = '/Users/kevinrono/Yale Drive/Classes/Senior year/Spring 2022/CS 276/dura-papyri/raw' # Use path in your local machine to find /raw directory
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER

db = mysql.connector.connect(
    host = secretkeys.DB_HOST, 
    user = secretkeys.DB_USER, 
    passwd = secretkeys.DB_PASSWORD,
    database = secretkeys.DB_DATABASE
    )
cursor = db.cursor(dictionary = True)

def object_converter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

@app.route("/")
def index():
    return render_template('index.html')

# Get the uploaded files
# https://medevel.com/flask-tutorial-upload-csv-file-and-insert-rows-into-the-database/
@app.route("/upload", methods=['POST'])
def uploadFiles():
    # get the uploaded file
    uploaded_file = request.files['data']

    if uploaded_file.filename != '':
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)

        # set the file path
        uploaded_file.save(file_path)

        parseCSV(file_path)
        # save the file
    return redirect(url_for('index'))


def parseCSV(filePath):

    # Use Pandas to parse the CSV file
    csvData = pd.read_csv(filePath, header=0)

    # Loop through the Rows
    for i, row in csvData.fillna("---").iterrows():
        sql = "INSERT INTO information (ID, Publication, Relation, Language, Date, Provenance, Findspot, Season, Wikidata_ID, content, name, subject, start, end, image_url, image, material, origin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (row['ID'], row['Publication'], row['Relation'], row['Language'], row['Date'], row['Provenance'], row['Findspot'], row['Season'], row['Wikidata_ID'], row['content'], row['name'], row['subject'], row['start'], row['end'], row['image_url'], row['image'], row['material'], row['origin'])

        cursor.execute(sql, values) # , if_exists='append'
        db.commit()
        
        print("Values inserted!")


@app.route("/map", methods=['GET', 'POST'])
def map():
    return render_template('map.html')

@app.route("/timeline", methods=['GET', 'POST'])
def timeline():
    return render_template('timeline.html')

@app.route("/results")
def results():
    return render_template('results.html')

@app.route("/display_results",  methods=['GET'])
def display_results():
    result = None

    return json.dumps({"success": True, "data": result}, default = object_converter), 200, {"ContentType": "application/json"}


@app.route("/show_timeline",  methods=['POST'])
def show_timeline():
    start = request.form.get("start")
    end = request.form.get("end")

    query = "SELECT * FROM information WHERE start >= %s AND end <= %s ORDER BY start ASC" #  ORDER BY start ASC
    vals = (start, end)

    cursor.execute(query, vals)
    result = cursor.fetchall()

    # result[0]["image"] = base64.b64decode(result[0]["image"])
        
    return json.dumps({"success": True, "data": result}, default = object_converter), 200, {"ContentType": "application/json"}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


# doc_id, ID, Publication, Relation, Language, Date, Provenance, Findspot, Season, Wikidata_ID, content, name, subject, start, end, image_url, image, material, origin
