# log-analyzer

## Steps to run
### Env setup
```
python3 -m virtualenv env
source env/bin/activate
pip install -r requirements.txt 
```
### Run
```
python log_parser.py 
open output/log.html
```

## Functionality

The log parser reads an input log file and creates objects that represent each process. This data is then represented as charts/tables using a Jinja 2 (http://jinja.pocoo.org/docs/2.10/) template. For charting, this repository uses Google Charts.
