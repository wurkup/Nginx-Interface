# Nginx-Interface
Nginx is a widely used reverse proxy.\
Most of the time developers are expected to <b>ssh to servers</b>, <b>manage the nginx</b> and <b>change the configuration</b> files which is a tad bit tedious. So, in-order to make life simpler <b>[Wurkup](https://github.com/wurkup)</b> decided to build a UI that can help take care of Nginx management. We would love for you to use the tool and hit us back with some feedback!

## Features
- Manage existing configurations
- Able to create new folders and store new configurations
- Test the configuration

## Getting Started
- Download for Ubuntu 18+ & python 3.6 onwards
    - Extract the tar file
    - run `./nginx-interface`
    Note: In some machines the nginx path `/etc/nginx` may not have root permissions , make sure to give root permissions to the nginx folder.
- Download for Mac OS Big Sur
    - Extract the tar file
    - run `./nginx-interface`
    Note: Mac identifies this as unknown software, so enable it in security & privacy under system preferences.

### Run it local
- Make sure to have `python3`,`pip3` installed
- Create virtual env 
    - `python3 -m venv env`
- Activate virtual environment
    - `source env/bin/activate`
- `pip install -r requirements.txt`    
- `python3 server.py`

### See UI
- [Open in Browser - http://localhost:5000](http://localhost:5000)