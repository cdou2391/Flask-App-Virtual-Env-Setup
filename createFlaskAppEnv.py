import os
import sys
import subprocess
 

try:
    # folders and file creation
    parentFolderName = input("Enter application name : ")
    if not os.path.exists(parentFolderName):
        os.makedirs(parentFolderName)
        if os.path.exists(parentFolderName):
            os.makedirs(parentFolderName+"/logs")
            os.makedirs(parentFolderName+"/static")
            os.makedirs(parentFolderName+"/template")
            if os.path.exists (parentFolderName+"/static"):
                os.makedirs(parentFolderName+"/static/data")
                os.makedirs(parentFolderName+"/static/scripts")
                os.makedirs(parentFolderName+"/static/style")

            if os.path.exists (parentFolderName+"/template"):
                fp = open(parentFolderName+"/template/login.html", 'w')
                fp = open(parentFolderName+"/template/home.html", 'w')
                fp.close()

            fp = open(parentFolderName+"/app.py", 'w')
            fp = open(parentFolderName+"/models.py", 'w')
            fp.close()
    
        # package installation
        subprocess.call('cd ' + parentFolderName, shell=True)
        subprocess.check_call([sys.executable, '-m', 'venv', 'virtual'])
        subprocess.check_call([sys.executable, '-m', 'pip', 'install','flask'])


except NameError as error:
    print("Error: No name was provided. Enter project name")