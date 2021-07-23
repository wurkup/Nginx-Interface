# Nginx-Interface
Nginx is a widely used reverse proxy.\
Most of the time developers are expected to `ssh to servers`, `manage the nginx` and `change the configuration` files which is a tad bit tedious. So, in-order to make life simpler `Wurkup` decided to build a UI that can help take care of Nginx management. We would love for you to use the tool and hit us back with some feedback!

## Features
- Manage existing configurations
- Able to create new folders and store new configurations

## Getting Started
- Download for Ubuntu 16 onwards
- Download for Mac OS Big Sur

### Run it local
- Make sure to have `python3`,`pip3` installed
- Create virtual env 
    - `python3 -m venv env`
- Activate virtual environment
    - `source env/bin/activate`
- `pip install -r requirements.txt`    
- `python3 server.py`

### See UI
- `http://localhost:5000`