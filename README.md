# Nginx-Interface
Nginx is a widely used reverse proxy.\
Most of the time developers are expected to `ssh to servers`, `manage the nginx` and `change the configuration` files which is a tad bit tedious. So, in-order to make life simpler `Wurkup` decided to build a UI that can help take care of Nginx management. We would love for you to use the tool and hit us back with some feedback!

## Features
- Manage existing configurations
- Able to create new folders and store new configurations

## Getting Started

- You can find the latest docker image at [DockerHub](https://hub.docker.com/repository/docker/wurkup/nginx-interface)

### Deploy using docker-compose
- There exists a `docker-compose.yml` file in `deploy/docker` which deploys the latest docker instance
- Make sure to update `volumes` to your nginx path 
    - Ex:
        - if you are running nginx on `mac` then your volume must be - `/usr/local/etc/nginx:/etc/nginx`
        - if you are running nginx on `linux` then your volume must be - `/etc/nginx:/etc/nginx`
- ```sudo docker-compose -f docker-compose.yml up -d```

### Running docker
- ```docker run -d --restart=always --name nginx-interface:<tag> -v <source-volume>:/etc/nginx -p 5000:5000 nginx-interface:latest```
- make sure to update `<source-volume>` to the path mentioned above based on the OS that you are running.

### Run it local
- Make sure to have `python3`,`pip3` installed
- Clone the repository `https://github.com/nginxinc/nginx-plus-dashboard.git`
- Create virtual env 
    - `python3 -m venv env`
- Activate virtual environment
    - `source env/bin/activate`
- `python3 server.py`

### See UI
- `http://localhost:5000`