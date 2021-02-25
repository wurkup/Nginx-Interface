from flask import Flask,render_template,request
import os,subprocess
from Nginx import Nginx
gui_dir = os.path.join(os.path.dirname(__file__), 'templates')
static_dir = os.path.join(os.path.dirname(__file__), 'static')
n = Nginx()
app = Flask(__name__, static_folder=static_dir, template_folder=gui_dir)

@app.route('/')
def landing():
    """
    Render index.html. Initialization is performed asynchronously in initialize() function
    """
    return render_template('index.html')

@app.route('/server-start')
def startserver():
    '''
    With exit code 0,127 we can see if nginx is installed or not 
    '''
    is_installed = subprocess.call(" nginx",shell=True)
    print("The exit code was: %s" % is_installed)

@app.route('/config/<name>',methods=["PUT"])
def create_config(name):
    data = request.json
    n.create(name,data['content'])
    return "ok"

# startserver()
app.run()

