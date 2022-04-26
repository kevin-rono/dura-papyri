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
UPLOAD_FOLDER = '../raw'
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
@app.route("/", methods=['POST'])
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
    col_names = ['id','tm_id','wikidata_id', 'content', 'name' , 'subject', 'date', 'image_url', 'material', 'origin', 'language', 'findspot', 'time_of_excavation', 'image']
    # Use Pandas to parse the CSV file
    csvData = pd.read_csv(filePath,names=col_names, header=None)
    # Loop through the Rows
    for i, row in csvData.iterrows():
        sql = "INSERT INTO addresses (id, tm_id, wikidata_id, content, name, subject, date, image_url, material, origin, language, findspot, time_of_excavation, image) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (int(row['id']), int(row['tm_id']), row['wikidata_id'], row['content'], row['name'], row['subject'], row['date'], row['image_url'], row['material'], row['origin'], row['language'], row['findspot'], row['time_of_excavation'], row['image'])

        cursor.execute(sql, values) # , if_exists='append'
        db.commit()
        
        print(i, row['id'], row['tm_id'], row['wikidata_id'], row['content'], row['name'], row['subject'], row['date'], row['image_url'], row['material'], row['origin'], row['language'], row['findspot'], row['time_of_excavation'], row['image'])


@app.route("/map")
def map():
    return render_template('map.html')

@app.route("/timeline")
def timeline():
    return render_template('timeline.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')