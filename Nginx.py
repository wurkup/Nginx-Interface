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

    def get_file_list(self):
        try:
            lis_files = os.listdir(NGINX_PATH[DEVICE])
            return lis_files
        except Exception as e:
            print(e)

    def get_folder_list(self):
        try:
            lis_folder =[ y for y in os.listdir(NGINX_PATH[DEVICE]) if os.path.isdir(NGINX_PATH[DEVICE]+"{}{}".format("/",y)) ]
            return lis_folder
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
    
    def modified_conf(self,name,data):
        try:
            path = NGINX_PATH[DEVICE]+"{}{}".format("/",name)
            conf_file = open(path,"w")
            for each in data:
                conf_file.write("%s\n" % each)
            return "ok"
        except Exception as e:
            print(e)