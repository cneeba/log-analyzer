import re
from jinja2 import Template
import os
import datetime

class Job():
    def __init__(self, name="", start_time=0, end_time=0, status=0):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.status = status

    def get_start_time_obj(self):
        return datetime.datetime.strptime(self.start_time, '%Y-%m-%d.%H:%M:%S')
    def get_end_time_obj(self):
        return datetime.datetime.strptime(self.end_time, '%Y-%m-%d.%H:%M:%S')

def read_file(file_name):
    with open (file_name) as fd:
        content = fd.readlines()
    content = [x.strip() for x in content]
    return content

def parse_file_content(content_of_log_file):
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

def create_html_file(jobs_dict):
    template_file_name = ("log_template.html")
    with open(template_file_name) as html_src:
        html_template = html_src.read()
        template = Template(html_template)
        output_file_name = ("log.html")
        with open(output_file_name, 'w') as output_file:
            output_file.write(template.render(log_groupings = jobs_dict))

if __name__ == "__main__":
    content_of_log_file  = read_file("log_file.txt")
    jobs_dict = parse_file_content(content_of_log_file)
    create_html_file(jobs_dict)

