# Pretend command line text browser using string variables as site contents
# Update makes get requests top inputted url and print's text of response

import sys
import os
import requests
from bs4 import BeautifulSoup
import re
from colorama import init, Fore, Style
init(autoreset=True) 

# Create directory for saved pages
directory = sys.argv[1]
if not os.path.exists(directory):
    os.mkdir(directory)

# Initiate empty history folder
history = []
site_file_name = ''

while True:
    command = input()
    if command == 'exit':
        break
    elif command == 'back':
        # Do nothing if history is empty
        if len(history) == 0:
            continue
        # Pop history stack and display saved page file from directory
        else:
            with open(f'{directory}/{history.pop()}', 'r') as file:
                print(file.read())
                continue
    # Add previous page (if there is one) to history before navigating away            
    if site_file_name != '':
        history.append(site_file_name)

    # Format command into usable url and site file name
    if command[:7] != 'http://':
        url = 'http://' + command
        site_file_name = command[:command.rfind(".")].replace('/', '_')
    else:
        url = command
        site_file_name = url[7:url.rfind(".")].replace('/', '_')

    # If page visited before, just open saved version
    if os.path.exists(f'{directory}/{site_file_name}'):
        with open(f'{directory}/{site_file_name}', 'r') as file:
            print(file.read())

    # Get page from web
    else:
        # Make request to URL
        site_response = requests.get(url)
        if site_response:
            soup = BeautifulSoup(site_response.text, 'html.parser')
            for link in soup.find_all('a'):
                if link.string:
                    link.string.replace_with(Fore.BLUE + link.string + Fore.WHITE)
            text = soup.get_text('\n', strip=True)
            print(text)
            with open(f'{directory}/{site_file_name}', 'w') as file:
                file.writelines(text)

        else:
            print('Site error')
            continue