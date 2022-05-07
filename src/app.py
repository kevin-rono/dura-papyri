import io
import mysql.connector
import os
from os.path import join, dirname, realpath
import pandas as pd

from flask import Flask, render_template, request, send_file, redirect, url_for

import secretkeys

app = Flask(__name__)

# enable debugging mode
app.config["DEBUG"] = True

# Upload folder
UPLOAD_FOLDER = '/Users/alinakramp/Desktop/yale/Digital\ Humanities/dura-papyri/raw' # Use path in your local machine to find /raw directory
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER

db = mysql.connector.connect(
    host = secretkeys.DB_HOST, 
    user = secretkeys.DB_USER, 
    passwd = secretkeys.DB_PASSWORD,
    database = secretkeys.DB_DATABASE
    )
cursor = db.cursor(dictionary = True)

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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


# doc_id, ID, Publication, Relation, Language, Date, Provenance, Findspot, Season, Wikidata_ID, content, name, subject, start, end, image_url, image, material, origin
