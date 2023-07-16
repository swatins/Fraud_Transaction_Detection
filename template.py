import os
from pathlib import Path
import logging

while True:
    project_name=input("Enter your project Name : ") #"Fraud Transaction Detection"
    if project_name !='':
        break
    
list_of_files= [
    
    f"{project_name}/__init.py__",
    f"{project_name}/components/",
    f"{project_name}/config/__init.yaml",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/logger.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/utils/utils.py",
    f"config/config.yaml",
    "schema.yaml",
    "requirements.txt",
    "setup.py",
    "main.py",
]
    
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating a new directory at: {filedir} for {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating a new file:{filename} for path {filepath}")
    else : 
        logging.info(f"File is already present at :{filepath}")