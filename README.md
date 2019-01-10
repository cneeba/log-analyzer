# log-analyzer

## Steps to run
### Env setup
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt 
mkdir -p output
```
### Run
```
python log_parser.py
open output/log.html
```
### Run with params
```
python log_parser.py input/log_file.txt output/log2.html
open output/log2.html
```

## Functionality

The log parser reads an input log file and creates objects that represent each process. This data is then represented as charts/tables using a Jinja 2 (http://jinja.pocoo.org/docs/2.10/) template. For charting, this repository uses Google Charts (https://developers.google.com/chart/interactive/docs/gallery/timeline).

### Screenshots

![Timeline View](https://user-images.githubusercontent.com/28618260/50991193-ef298080-14c8-11e9-8d12-6c0673976e66.png "Timeline View")

![Table View](https://user-images.githubusercontent.com/28618260/50991196-f0f34400-14c8-11e9-8f34-7cc13fde4989.png "Table View")
