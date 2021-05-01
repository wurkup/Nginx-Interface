from sys import platform
NGINX_PATH={}

if platform == "darwin":
    DEVICE="mac"
    NGINX_PATH[DEVICE] = "/usr/local/etc/nginx"
elif platform == "linux":
    DEVICE="ubuntu"
    NGINX_PATH[DEVICE] = "/etc/nginx"