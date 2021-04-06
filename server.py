from flask import Flask,render_template,request
import os,subprocess
from subprocess import check_output
from Nginx import Nginx
gui_dir = os.path.join(os.path.dirname(__file__), 'templates')
static_dir = os.path.join(os.path.dirname(__file__), 'static')
n = Nginx()
app = Flask(__name__, static_folder=static_dir, template_folder=gui_dir)
app.config['TEMPLATES_AUTO_RELOAD'] = True
@app.route('/')
def landing():
    """
    Render index.html. Initialization is performed asynchronously in initialize() function
    """
    return render_template('index.html')

@app.route('/server-status',methods=["GET"])
def statusserver():
    '''
    With exit code 0,127 we can see if nginx is installed or not 
    '''
    is_installed = subprocess.call("nginx -ver",shell=True)
    print("The exit code was: %s" % is_installed)
    if is_installed == 127:
        return {"code":is_installed,"msg":"Nginx not found,Please install Nginx"}
    return {"code":200,"msg":"Nginx available"}

@app.route('/config/<field>',methods=["GET"])
def field_config(field):
    '''
    returns list of configs,details of a particular config.
    '''
    if field =="list":
        return {"code":200,"files":n.get_list()}
    elif field == "test":
        exitcode = subprocess.call("nginx -t",shell=True)
        if exitcode == 1:
            process = subprocess.Popen('nginx -t', shell= True,stderr=subprocess.PIPE)
            out_msg = process.stderr.read()
            return {"code":403,"msg":out_msg.decode("utf-8")}
        return {"code":200,"msg":"nginx configuration test success"}

@app.route('/config/<name>',methods=["PUT"])
def create_config(name):
    '''
    Function to write the contents of conf to a file
    '''
    data = request.json
    n.create(name,data['content'])
    return "ok"

@app.route('/config/i/<fname>',methods=["GET"])
def get_config(fname):
    '''
    Function to get the contents of conf file
    '''
    conf_content=n.get_conf(fname)
    return conf_content

@app.route('/config/i/<fname>',methods=["PUT"])
def modified_config(fname):
    '''
    Function to write the modified contents of conf file
    '''
    data = request.json
    conf_content=n.modified_conf(fname,data['content'])
    return conf_content

app.run()

