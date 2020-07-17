# Pretend command line text browser using string variables as site contents

import sys
import os

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''
directory = sys.argv[1]
if not os.path.exists(directory):
    os.mkdir(directory)

saved_pages = []
history = []
site = ''

while True:
    command = input()
    if command == 'exit':
        break
    elif command == 'back':
        # Do nothing if history is empty
        if len(history) == 0:
            continue
        # Pop history stack and display page
        else:
            with open(f'{directory}/{history.pop()}', 'r') as file:
                print(file.read())
                continue
    # Add previous page to history before navigating away            
    if site != '':
        history.append(site)
    # If not a url
    if command.find('.') == -1:
        # If page visited before
        if command in saved_pages:
            site = command
            with open(f'{directory}/{site}', 'r') as file:
                print(file.read())
        else:
            print('Error: Incorrect URL')
    # If command looks like a url
    else:
        url = command
        # Site is everything before last '.'
        site = url[:url.rfind(".")]
        if url == 'bloomberg.com':
            print(bloomberg_com)
            if site not in saved_pages:
                with open(f'{directory}/{site}', 'w') as file:
                    file.writelines(bloomberg_com)
                saved_pages.append(site)
        elif url == 'nytimes.com':
            print(nytimes_com)
            if site not in saved_pages:
                with open(f'{directory}/{site}', 'w') as file:
                    file.writelines(nytimes_com)
                saved_pages.append(site)
        else:
            print('Error: Incorrect URL')