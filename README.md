# Nginx-Interface
Nginx is a widely used reverse proxy. Most of the time we all have to ssh to the servers, manage the nginx and change the configuration files. So in-order to make life simpler we decided to build a UI that can take care of Nginx management. If you want to make nginx management simple do try out the application and I am looking forward to your feedback, pull requests and feature requests.

## Features
- 1
- 2

# Getting Started
## Deploy using docker-compose
- There is a `docker-compose.yml` file in deploy/docker which deploys the latest docker instance
- Make sure to update `volumes` to your nginx path 
    - Ex:
        - if you are running docker on `mac` then your volume must be - `/usr/local/etc/nginx:/etc/nginx`
        - if you are running docker on `linux` then your volume must be - `etc/nginx:/etc/nginx`
- `sudo docker-compose -f docker-compose.yml up -d`

## Running docker
`docker run -d --restart=always --name nginx-interface -v /usr/local/etc/nginx:/etc/nginx -p 5000:5000 nginx-interface:latest`
- make sure to update ` -v /etc/nginx:/etc/nginx ` to the path mentioned above based on your OS that you are running.

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