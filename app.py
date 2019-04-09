# -*- coding: utf-8 -*-
# import os
# os.chdir('/home/mike/Desktop/flask_starter_kit')
from flask import Flask, render_template, request, jsonify, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import numpy as np
import config as cfg

app = Flask(__name__)

# app.config['SECRET_KEY'] = cfg.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = cfg.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = cfg.SQLALCHEMY_TRACK_MODIFICATIONS
# app.config['MAX_CONTENT_LENGTH'] = 700 * 1024 * 1024 # originally set to 16 MB; now 700
# app.config['SECURITY_PASSWORD_SALT'] = cfg.SECURITY_PASSWORD_SALT

#error logging
# logfile = os.getcwd() + '/../logs_etc/app.log'

db = SQLAlchemy(app)

#classes for SQLAlchemy's ORM
# class Data(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     region = db.Column(db.String(10))
#     site = db.Column(db.String(50))
#     DateTime_UTC = db.Column(db.DateTime)
#     variable = db.Column(db.String(50))
#     value = db.Column(db.Float)
#     flag = db.Column(db.Integer)
#     upload_id = db.Column(db.Integer)
#
#     def __init__(self, region, site, DateTime_UTC, variable, value, flag, upid):
#         self.region = region
#         self.site = site
#         self.DateTime_UTC = DateTime_UTC
#         self.variable = variable
#         self.value = value
#         self.flag = flag
#         self.upload_id = upid
#
#     def __repr__(self):
#         return '<Data %r, %r, %r, %r, %r>' % (self.region, self.site,
#         self.DateTime_UTC, self.variable, self.upload_id)
#
# db.create_all()

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

    result = pd.read_sql("select id from table1 where col2 = '" + str(p1) +\
        "' and col3 > '" + str(p2) + "';", db.engine).id.tolist()

    return jsonify(response=result)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
