#!/usr/bin/env python
"""Create a Flare project"""

__version__ = "0.0.1"

import os
import sys
import logging
import subprocess

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    argument = sys.argv[1]
    path = sys.argv[2]
    switch(argument, path)

def switch(argument, path):
    options = {
    "new" : new,
    "start": start,
    "stop": stop,
    "remove": remove,
    "--help": docs
    }
    if argument in options:
        if argument == "new":
            return options[argument](path)
        else:
            return options[argument]()
    else:
        error()

def new(path):
    root_path = "{}/{}".format(os.getcwd(), path)
    if not os.path.exists(root_path):
        create(root_path)
        logging.info('Creating %s', root_path)
        top_level_files = ["LICENSE", "README.md", "requirements.txt"]
        top_level_directories = ["data", "docs", "models", "notebooks", "ref", "reports", "src"]
        data_directories = ["raw", "temp", "prod"]
        src_directories = ["features", "models"]
        for f in top_level_files:
            open(f, 'a').close()
        for directory in top_level_directories:
            os.mkdir(os.path.join(root_path, directory))
        for directory in data_directories:
            os.mkdir(os.path.join("{}/data/".format(root_path), directory))
        for directory in src_directories:
            os.mkdir(os.path.join("{}/src/".format(root_path), directory))
    else:
        logging.info('Directory %s already exists', path)

def error():
    logging.info('Input is not recognized. Try --help to see documentation.')

def update():
    subprocess.call(["pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | \
    xargs -n1 pip install -U"], shell=True)

def docs():
    print("""
    Run "flare new <project-name> to create a new Flare project with a venv"
    Run "flare start to start the venv"
    Run "flare stop to stop the venv"
    Run "flare update to update the Pip packages within the venv"
    Run "flare remove to remove the venv"
    """)

def create(path):
    subprocess.call(["virtualenv {}/venv".format(path)], shell=True)

def remove():
    subprocess.call(["rm -rf venv"], shell=True)

def start():
    subprocess.call(["source venv/bin/activate"], shell=True)

def stop():
    subprocess.call(["deactivate"], shell=True)

if __name__ == '__main__':
    main()
