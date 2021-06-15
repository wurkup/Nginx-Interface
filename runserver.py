from gevent import monkey
monkey.patch_all()
from gevent.pywsgi import WSGIServer
from server import app
import gevent.signal

print("Server started")
http_server = WSGIServer(('0.0.0.0', 5000), app)
http_server.serve_forever()