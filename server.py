from flask import Flask,render_template,request
import os,subprocess
from subprocess import check_output
from Nginx import Nginx
from gevent import monkey
monkey.patch_all()
from gevent.pywsgi import WSGIServer
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
    if is_installed == 127:
        return {"code":is_installed,"msg":"Nginx not found,Please install Nginx"},404
    return {"code":200,"msg":"Nginx available"}

@app.route('/config/<_type>/<field>',methods=["GET"])
@app.route('/config/<_type>',methods=["GET"])
def field_config(_type,field=None):
    '''
    returns list of configs,details of a particular config.
    '''
    folder_name = request.args.get("folder_name",None)
    if _type =="list":
        if field == "file":
            if folder_name:
                return {"code":200,"files":n.get_folder_files(folder_name)}
            return {"code":200,"files":n.get_file_list()}
        if field == "folder":
            return {"code":200,"folders":n.get_folder_list()}
    elif _type == "test":
        exitcode = subprocess.call("nginx -t",shell=True)
        if exitcode == 1:
            process = subprocess.Popen('nginx -t', shell= True,stderr=subprocess.PIPE)
            out_msg = process.stderr.read()
            return {"code":403,"msg":out_msg.decode("utf-8")}
        elif exitcode == 127:
            return {"code":127,"msg":"nginx not found"}
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
    folder_name = request.args.get('folder_name',None)
    conf_content=n.get_conf(folder_name,fname)
    return conf_content

@app.route('/config/i/<fname>',methods=["PUT"])
def modified_config(fname):
    '''
    Function to write the modified contents of conf file
    '''
    foldername = request.args.get('folder_name',None)
    data = request.json
    conf_content=n.modified_conf(fname,foldername,data['content'])
    return conf_content

@app.route('/config/i/<fname>',methods=["DELETE"])
def delete_config(fname):
    '''
    Function to delete the conf file
    '''
    foldername = request.args.get('folder_name',None)
    resp=n.delete_conf(fname, foldername)
    if resp:
        return "ok"
    else:
        return "error",500

print("Server started, Running on port 5000")
http_server = WSGIServer(('0.0.0.0', 5000), app)
http_server.serve_forever()

