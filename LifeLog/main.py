#!/bin/pyton3

import json # Used for config file

def create_config():
    # TODO

def main():
    try:
        configFile = open("~/.config/lifelog/config.json", "w") # Open config file
    except FileNotFoundError: # If the file doesn't exist:
        create_config() # Call the create config function
