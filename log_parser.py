import re
from jinja2 import Template
import os
import sys
import json 
from job import Job
from flask import Flask
from pymongo import MongoClient

class Mongodb:
    def __init__(self, url):        
        self.url = url
        self.mgdb = self.get_Connect()
    def get_Connect(self):
        return MongoClient(self.url)


def insert_data_to_db(file_name, jobs_dict):
    mongo_client =Mongodb("34.73.9.243:80")
    mongo_db = mongo_client.mgdb['log_analyzer']
    mongo_collection = mongo_db['analyzed_result']
    job_details_list = []
    record = {}
    for job_name in jobs_dict.keys():        
        job_details_list.append(jobs_dict[job_name].__dict__)

    record["_id"] = file_name
    record["job_details"] = job_details_list
    mongo_collection.insert_one(record)

def read_file(file_name):

    """
    Take input name of the file and return the content.
    param file_name: File name which has to be read
    return content: Content of log file as a list of string
    """

    with open (file_name) as fd:
        content = fd.readlines()
    content = [x.strip() for x in content]
    return content

def parse_file_content(content_of_log_file):

    """
    Parse the content of the log file and create a dictinary.
    param content_of_log_file: Content of log file as a list of string
    return jobs_dict: a dictionary with build name as key , build details as values
    """
    
    search_regex = re.compile('^=== \[(?P<process_time>.+)\] :(?P<process_state>.+): (?P<process_name>[^\s]+)\s*(?P<process_status>[0-9])*$')
    jobs_dict = {}
    for log_line in content_of_log_file:
        parsed_log_line = search_regex.search(log_line)
        if parsed_log_line is not None:
            process = parsed_log_line.group('process_name')
            if parsed_log_line.group('process_state') == "START" :                
                start_time = (parsed_log_line.group('process_time'))
                jobs_dict[process] = Job(name = process, start_time = start_time, end_time = None, status = None)
            elif parsed_log_line.group('process_state') == "END":
                end_time = parsed_log_line.group('process_time')
                if process in jobs_dict.keys():
                    jobs_dict[process].end_time = end_time
                else:
                    print("Start of the project is not present in the log file. Could not record end")
            if parsed_log_line.group('process_state') == "STATUS":
                if process in jobs_dict.keys():
                    jobs_dict[process].status = parsed_log_line.group('process_status')
                else:
                    print("Start of the project is not present in the log file. Could not record status")
    return jobs_dict

if __name__ == "__main__":
    if len(sys.argv) != 2:
        input_file = "input/log_file.txt"
        print("Did not receive input_file param. Using defaults ...")
    else:
        input_file = sys.argv[1]
    content_of_log_file  = read_file(input_file)
    jobs_dict = parse_file_content(content_of_log_file)
    insert_data_to_db("input_file", jobs_dict)
    print("Log file was parsed and data was persisted")

