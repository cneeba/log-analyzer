# log-analyzer

## Steps to run
### Env setup
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt 
mkdir -p output
export PYTHON_PATH=$(pwd)
```
### Run parser to parse build log files
```
python log_parser.py
```
### Alternate: Run parser with params to parse build log files
```
python log_parser.py input/log_file.txt
```
### Start API server
```
export FLASK_APP=app/routes.py
python -m flask run --port=50100
```
### Retrieve build details from API server
#### JSON format
http://localhost:50100/builds/<file_name>

- Example: http://localhost:50100/builds/test_log.txt
#### HTML format
http://localhost:50100/builds/<file_name>?format=html

- Example: http://localhost:50100/builds/test_log.txt?format=html

## Functionality

- The log parser reads an input log file and creates objects that represent each process. This data is stored into a database (mongodb)
- An API server built using Flask enables retrieval of this parsed data 
- When provided with the build id, the API represents the parsed build data from Mongo DB as charts/tables using a Jinja 2 (http://jinja.pocoo.org/docs/2.10/) template. For charting, this repository uses Google Charts (https://developers.google.com/chart/interactive/docs/gallery/timeline).

### Screenshots from API response

![Timeline View](https://user-images.githubusercontent.com/28618260/50991193-ef298080-14c8-11e9-8d12-6c0673976e66.png "Timeline View")

![Table View](https://user-images.githubusercontent.com/28618260/50991196-f0f34400-14c8-11e9-8f34-7cc13fde4989.png "Table View")
