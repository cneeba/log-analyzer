import re
from jinja2 import Template
import os
import datetime
import sys
import json
# import requests 

from flask import Flask, request
from pymongo import MongoClient
from libs import read_data_from_db, create_html_file


app = Flask(__name__)

@app.route('/')
def index():
    """
    Index page for log-analyzer page. 
    :return: None
    """
    return 'Welcome to log-analyzer page'

@app.route('/record/')
def route():
    """
    This API gets the data stored in database . 
    param key: Key for the stored file name
    :return: Data if the keyword is present or None

    """
    file_id = request.args.get("id")
    print("Reached in record")
    file_id = "input_file"
    jobs_dict = read_data_from_db(file_id)
    print("Got jobs dict")
    print(jobs_dict)
    create_html_file(jobs_dict, "output1.html")

    return 'Welcome to log-analyzer page'
