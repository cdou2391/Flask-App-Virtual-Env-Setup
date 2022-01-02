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
                fp = open(parentFolderName+"/template/base.html", 'w')
                fp = open(parentFolderName+"/template/home.html", 'w')
                fp.close()

            fp = open(parentFolderName+"/app.py", 'w')
            fp = open(parentFolderName+"/models.py", 'w')
            fp.close()
    
        # package installation
        wd = os.getcwd()
        print(wd)
        os.chdir(str(parentFolderName))
        wd = os.getcwd()
        print(wd)
        subprocess.check_call([sys.executable, '-m', 'venv', 'virtual'])
        proc = subprocess.Popen([".", "virtual/bin/activate"], stdout=subprocess.PIPE, shell=True)
        output=subprocess.check_output(". virtual/bin/activate", shell=True)
        print(output)
        subprocess.check_call([sys.executable, '-m', 'pip', 'install','flask'])


except NameError as error:
    print("Error: No name was provided. Enter project name")