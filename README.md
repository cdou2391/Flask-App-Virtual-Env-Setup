# Flask-App-Virtual-Env-Setup

This python based script will help you to create a virtual environment for a flask app.

What it does:
It creates 9 folders and 4 files, all under your main project folder and also install 2 phyton packages
    1. Your main folder where everything will reside under which it also created 2 files
        1. app.py
        2. models.py
    2. A log folder where you can store all your logs
    3. A static folder where your css, scripts and all static file can be stored and under the static folder, we have 3 folders 
        1. data
        2. style
        3. scripts
    4. A template folder where all your html templates can be stored. It all also creates to tempaltes 
        1. login.html
        2. base.html

    5. Install the venv python package
    6. Install the flask python package
    
To run the script:
python3 createFlaskAppEnv.py

This will prompt you to enter the of your application which it will in turn set as the main folder name
    
