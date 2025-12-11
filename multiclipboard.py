# This script implements a multiclipboard that allows users to store and retrieve multiple text snippets

import sys
import pyperclip
import json 

"""data = pyperclip.paste()
print("Current clipboard data:", data)"""

MULTICLIPBOARD_FILE = 'clipboard.json'

# function to save the new data entered by the user into our json file
def save_data(filepath,data):
    with open(filepath, 'w') as file:
        json.dump(data, file)

# function to save the upload the json file into live memory 
def load_clipboard_data(filepath):
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# checking if the user properly executed the function : python3 multiclipboard.py save
if len(sys.argv) == 2:
    command = sys.argv[1] #second argument after multiclipboard.py
    data = load_clipboard_data(MULTICLIPBOARD_FILE) # loading the data json file into a variable
    if command =='save': # this one automatically saved the current copied text into the json file along with the provided key
        key = input("Enter a key to save clipboard data: ")
        data[key] = pyperclip.paste()
        save_data(MULTICLIPBOARD_FILE, data)
        print(f"Data saved under key '{key}'.")
    elif command == 'load': # this one gives the user the text related to that key (if existing)
        key = input("Please Provide a key: ")
        if key in data:
            pyperclip.copy(data[key])
            print("Data copied into clipboard")
        else:
            print("This key does not exist")
            
    elif command == 'list': # this one prints out all the texts and their keys
        print(data)
    else:
        print("Unknown command. Use 'save', 'load', or 'list'.")
else:
    print("Please provide exactly one command.")
    print("Usage: python multiclipboard.py [save|load|list]")
    