import re
from jinja2 import Template
import os
import datetime
import sys
import json
# import requests 

from flask import Flask, request
from pymongo import MongoClient
from libs import read_data_from_db, create_html


app = Flask(__name__)

@app.route('/')
def index():
    """
    Index page for log-analyzer page. 
    :return: None
    """
    return 'Welcome to log-analyzer page'

@app.route('/builds/<build_id>')
def builds(build_id):
    """
    This API gets the data stored in database . 
    param build_id: Key for the stored file name
    :return: Data if the build_id is in the database

    """
    format = request.args.get("format")
    jobs_dict = read_data_from_db(build_id)
    if format == "html":
        return create_html(jobs_dict)
    else:
        job_details_list = []
        record = {}
        for job_name in jobs_dict.keys():        
            job_details_list.append(jobs_dict[job_name].__dict__)        
        return json.dumps(job_details_list)
