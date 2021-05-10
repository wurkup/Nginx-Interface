from sys import platform
NGINX_PATH={}
LOG_PATH={}
if platform == "darwin":
    DEVICE="mac"
    NGINX_PATH[DEVICE] = "/usr/local/etc/nginx"
    LOG_PATH[DEVICE] = "/usr/local/var/log/nginx"
elif platform == "linux":
    DEVICE="ubuntu"
    NGINX_PATH[DEVICE] = "/etc/nginx"
    LOG_PATH[DEVICE] = "/var/log/nginx"