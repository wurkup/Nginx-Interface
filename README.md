# Nginx-Interface
The dashboard for managing Nginx configurations

## Features
- 1
- 2

# Getting Started
## Deploy using docker-compose
- There is a `docker-compose.yml` file in deploy/docker which deploys the latest docker instance
- Make sure to update `volumes` to your nginx path 
    - Ex:
        - `mac`: `/usr/local/etc/nginx:/usr/local/etc/nginx`
        - `linux` : `etc/nginx:/etc/nginx`
- `sudo docker-compose -f docker-compose.yml up -d`

## Running docker
`docker run -d --restart=always --name nginx-interface -v /usr/local/etc/nginx:/usr/local/etc/nginx -p 5000:5000 nginx-interface:latest`

## Run it local
- Make sure to have `python3`,`pip3` installed
- Clone the repository `https://github.com/nginxinc/nginx-plus-dashboard.git`
- Create virtual env 
    - `python3 -m venv env`
- Activate virtual environment
    - `source env/bin/activate`
- `python3 server.py`

# See UI
- `http://localhost:5000`