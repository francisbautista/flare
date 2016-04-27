#!/usr/bin/env python
"""Create a Flare project"""

__version__ = "0.0.1"

import os
import sys
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def new(path):
    root_path = "{}/{}".format(os.getcwd(), path)
    if not os.path.exists(root_path):
        logging.info('Creating %s', root_path)
        top_level_files = ["LICENSE", "README.md", "requirements.txt"]
        top_level_directories = ["data", "docs", "models", "notebooks", "ref", "reports", "src"]
        data_directories = ["raw", "temp", "prod"]
        src_directories = ["features", "models"]
        os.mkdir(root_path)
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

def error(): logging.info('Error on input')

def main():
    argument = sys.argv[1]
    path = sys.argv[2]
    switch(argument, path)

def switch(argument, path):
    options = {
    "new" : new}
    opt = options.get(argument, None)

    if opt != None:
        return opt(path)
    else:
        error()


if __name__ == '__main__':
    main()
