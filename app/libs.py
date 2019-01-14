import re
from jinja2 import Template
import os
import datetime
import sys
import json 

from flask import Flask
from pymongo import MongoClient
from log_parser import *
from job import Job


def read_data_from_db(file_id):
    """
    This API gets the data stored in database . 
    param key: Key for the stored file name
    :return: Data if the keyword is present or None

    """
    mongo_client =Mongodb("34.73.9.243:80")
    mongo_db = mongo_client.mgdb['log_analyzer']
    mongo_collection = mongo_db['analyzed_result']

    read_data = mongo_collection.find({'_id': file_id})
    output_data = read_data[0]["job_details"]
    jobs_dict = {}
    for output in output_data:
    	jobs_dict[output['name']] = Job( name = output['name'], start_time = output['start_time'], end_time = output['end_time'], status = output['status'] )
    return jobs_dict
    

def create_html(output_data):

    """
    Creates an output html file with graphical and tabular view.
    param jobs_dict: a dictionary with build name as key , build details as values
    return: None
    """

    template_file_name = ("resources/log_template.html")
    with open(template_file_name) as html_src:
        html_template = html_src.read()
        template = Template(html_template)
        return template.render(log_groupings = output_data)

def create_html_file(jobs_dict, output_file):

    """
    Creates an output html file with graphical and tabular view.
    param jobs_dict: a dictionary with build name as key , build details as values
    return: None
    """

    parsed_html = create_html(jobs_dict)
    output_file_name = (output_file)
    with open(output_file_name, 'w') as output_file:
        output_file.write(parsed_html)