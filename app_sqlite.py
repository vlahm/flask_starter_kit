# -*- coding: utf-8 -*-
# import os
# os.chdir('/home/mike/Desktop/flask_starter_kit')
from flask import Flask, render_template, request, jsonify, url_for, redirect
# from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import numpy as np
import config as cfg
import sqlite3

app = Flask(__name__)

# app.config['SECRET_KEY'] = cfg.SECRET_KEY
# app.config['SQLALCHEMY_DATABASE_URI'] = cfg.SQLALCHEMY_DATABASE_URI
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = cfg.SQLALCHEMY_TRACK_MODIFICATIONS
# app.config['MAX_CONTENT_LENGTH'] = 700 * 1024 * 1024 # originally set to 16 MB; now 700
# app.config['SECURITY_PASSWORD_SALT'] = cfg.SECURITY_PASSWORD_SALT

#error logging
# logfile = os.getcwd() + '/../logs_etc/app.log'

# db = SQLAlchemy(app)

#render landing page template
@app.route('/', methods=['GET'])
def render_index_page():

    return render_template('index.html')

#return another page template
@app.route('/page1', methods=['GET'])
def render_page1():

    return render_template('page1.html')

#handle api requests
@app.route('/api')
def api():

    #pull in requests
    p1 = request.args.get('param1')
    p2 = request.args.get('param2')
    # p1='b'; p2=1

    with sqlite3.connect('/home/mike/Desktop/flask_starter_kit' +\
        '/sqlite_.d') as con:

        cur = con.cursor()

        result = cur.execute("select id from table1 where col2 = '" + str(p1) +\
            "' and col3 > '" + str(p2) + "';").fetchall()

    return jsonify(response=result)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
