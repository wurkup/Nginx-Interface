from settings import *
import os,json
class Nginx:
    def __init__(self):
        pass

    def create(self,filename,content):
        '''
        Method to create a configuration file.
        '''
        try:
            conf_file = open(filename,"w")
            for each in content:
                conf_file.write("%s\n" % each)
            conf_file.close()
            return "ok"
        except Exception as e:
            print(e)
            return "error"
    def get_list(self):
        try:
            lis_files = os.listdir(NGINX_PATH[DEVICE])
            return lis_files
        except Exception as e:
            print(e)
    
    def get_conf(self,name):
        try:
            path = NGINX_PATH[DEVICE]+"{}{}".format("/",name)
            f = open(path,"r")
            content = f.read()
            return content
        except Exception as e:
            print(e)