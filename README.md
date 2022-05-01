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

4. Execute the main script to run the web application.

   ```
   $ (venv) python app.py
   ```

## License

Release under the [MIT License](LICENSE).
