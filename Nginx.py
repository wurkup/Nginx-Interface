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

    def get_folder_files(self,folder_name):
        try:
            path = NGINX_PATH[DEVICE]+"{}{}".format("/",folder_name)
            lis_files =[ y for y in os.listdir(path) if not os.path.isdir(y) ]
            return lis_files
        except Exception as e:
            print(e)

    def get_file_list(self):
        try:
            lis_files =[ y for y in os.listdir(NGINX_PATH[DEVICE]) if not os.path.isdir(NGINX_PATH[DEVICE]+"{}{}".format("/",y)) ]
            return lis_files
        except Exception as e:
            print(e)

    def get_folder_list(self):
        try:
            lis_folder =[ y for y in os.listdir(NGINX_PATH[DEVICE]) if os.path.isdir(NGINX_PATH[DEVICE]+"{}{}".format("/",y)) ]
            lis_folder.insert(0,"/")
            return lis_folder
        except Exception as e:
            print(e)
    
    def get_conf(self,folder_name,file_name):
        try:
            path = NGINX_PATH[DEVICE]+"{}{}".format("/",file_name)
            if folder_name:
                path = NGINX_PATH[DEVICE]+"{}{}{}{}".format("/",folder_name,"/",file_name)
            print(path,folder_name)
            f = open(path,"r")
            content = f.read()
            return content
        except Exception as e:
            print(e)
    
    def modified_conf(self,file_name,folder_name,data):
        try:
            path = NGINX_PATH[DEVICE]+"{}{}".format("/",file_name)
            if folder_name:
                path = NGINX_PATH[DEVICE]+"{}{}{}{}".format("/",folder_name,"/",file_name)
                folder_path = NGINX_PATH[DEVICE]+"{}{}".format("/",folder_name)
                if not os.path.exists(folder_path):
                    os.makedir(folder_path)
            conf_file = open(path,"w")
            for each in data:
                conf_file.write("%s\n" % each)
            return "ok"
        except Exception as e:
            print(e)

    def delete_conf(self,file_name,folder_name):
        try:
            path = NGINX_PATH[DEVICE]+"{}{}".format("/",file_name)
            if folder_name:
                path = NGINX_PATH[DEVICE]+"{}{}{}{}".format("/",folder_name,"/",file_name)
            os.remove(path)
            return True
        except Exception as e:
            print(e)
            return False