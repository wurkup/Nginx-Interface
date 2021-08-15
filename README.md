# Nginx-Interface
Nginx is a widely used reverse proxy.\
Most of the time developers are expected to <b>ssh to servers</b>, <b>manage the nginx</b> and <b>change the configuration</b> files which is a tad bit tedious. So, in-order to make life simpler <b>[Wurkup](https://github.com/wurkup)</b> decided to build a UI that can help take care of Nginx management. We would love for you to use the tool and hit us back with some feedback!

## Features
- Automatic reading of configuration files (supporting up to 1 level of nested structure)
- Creation of new files and folders
- Ability to modify and test the configurations
**Don't see a feature on this list?** Search our issue tracker if someone has already requested it and upvote it, or open a new issue if not. We prioritize our roadmap based on your feedback. 

## Getting Started
- Ubuntu 18+ & python 3.6 onwards
    - Extract the zip file
    - run `./server`
    Note: In some machines the nginx path `/etc/nginx` may not have root permissions , make sure to give root permissions to the nginx folder.
- Mac OS Big Sur
    - Extract the zip file
    - run `./server`
    Note: Mac identifies this as unknown software, so enable it in security & privacy under system preferences.
- Centos 8
    - Extract the zip file
    - run `./server`

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

## Contributing
We'd love to take all the help we can get! If you would like to get involved you can raise a PR or you can reach us at [Wurkup-co](https://www.linkedin.com/company/wurkup-co/)