# dura-papyri
This repository contains the source code for the Dura Papyri project. This work was completed as part of CPSC 276/376: Introduction to Applications of Computer and Data Science for the Digital Humanities.

## Quick Start

1. Clone this repository.

   ```
   $ https://github.com/kevin-rono/dura-papyri
   ```

2. Create a Python virtual environment and install package requirements.

   ```
   $ cd src
   $ python -m venv venv
   $ source venv/bin/activate
   $ (venv) pip install -U pip wheel
   $ (venv) pip install -r requirements.txt
   ```

3. Create the SQL database. If you do not have MySQL installed locally, refer to the [official docs](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/).

   ```
   $ (venv) mysql -h localhost -u root -p < init.sql
   ```

   
4. Update path to raw in app.py and change password in secretkeys.py to your own MySQL password. Both files are found in src.
   
   ```
   UPLOAD_FOLDER = '/../dura-papyri/raw

   DB_PASSWORD = ''  # CHANGE TO YOUR PASSWORD
   ```
   
5. Execute the main script to run the web application. You should now be able to open the page on localhost:5000

   ```
   $ (venv) python app.py
   ```
   

## Data Preparation

An important component of this project involved collecting papyri metadata from disparate online sources and cleaning them into presentable format. This section details the process involved in data preparation and wrangling. 

### Data

All raw data files used to power the web application are located under [`raw`](raw). 

- [`xmls.json`](raw/xmls.json) is a JSON file containing all raw XMLs web scraped from [papyri.info](https://papyri.info). 
- [`data.csv`](raw/data.csv) is a CSV file containing metadata for each papyrus item, obtained by parsing and extensively cleaning [`xmls.json`](raw/xmls.json).
- [`embeddings.json`](raw/embeddings.json) is a JSON file containing two-dimensional vector representations of each papyrus item, obtained by using a pretrained language model and applying t-SNE dimensionality reduction on the resulting context vectors.

### Executables

All executable scripts are located under [`bin`](bin). To execute these scripts locally, `pip` install the dependencies listed in [`bin/requirements.txt`](bin/requirements.txt). 

- [`xml_scraper.ipynb`](bin/xml_scraper.ipynb) is a jupyter notebook used to scrape XML files to produce [`xmls.json`](raw/xmls.json) from [papyri.info](https://papyri.info), using [Trismegistos](https://www.trismegistos.org) as the gateway portal.
- [`make_csv.py`](bin/make_csv.py) is a Python script used to parse [`xmls.json`](raw/xmls.json) into [`data.csv`](raw/data.csv). Note that some manual parsing of the dates was performed to further clean the field.
- [`to_english.py`](bin/to_english.py) is a Python script used to further clean [`data.csv`](raw/data.csv) by removing any occurrences of non-English texts.
- [`embed.py`](bin/embed.py) is a Python script that processes each entry of [`data.csv`](raw/data.csv) to produce two-dimensional vector representations of each metadata, available in [`embeddings.json`](raw/embeddings.json).

All scripts can be invoked from the root of the repository as follows.

```
$ python bin/FILENAME.py
```

## License

Released under the [MIT License](LICENSE).
