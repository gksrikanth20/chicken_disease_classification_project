#to create folders and files automatically


import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:') # setting up to see how the logging format should look like.

project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",#Constructor makes the project cnnClassifier has local package. Hence init is needed.
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml", #for MLOPS
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html" #for creating a web page


]

for filepath in list_of_files:
    filepath = Path(filepath) #this will automatically convert to windows path folder type. Because \ is used in windows and / is used in Linux.
    filedir, filename = os.path.split(filepath) #get directory and path

    if filedir != "":
        os.makedirs(filedir, exist_ok=True) # It will not create if already folder is there with that name in that path
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # just creating the file
            logging.info(f"Creating empty file: {filepath}")
        
    else:
        logging.info(f"{filename} is already exists")