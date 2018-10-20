#!/usr/bin/env python

import subprocess
import datetime
import sys

files = [
        'Left1.txt','Right1.txt',
        'Left2.txt','Right2.txt',
        'Left3.txt','Right3.txt',
        'Left4.txt','Right4.txt'
        ]

def readnameFromFile(filename):
    with open(filename) as f:
        return f.read().rstrip()

def renameUsingFiles(filenames):
    names = [ readnameFromFile(x) for x in filenames]
    newnames = "'" + "','".join(names) + "'"
    setCmd = "/usr/bin/gsettings set org.gnome.desktop.wm.preferences workspace-names \"[%s]\"" % newnames
    print setCmd
    subprocess.check_output(setCmd,shell=True)

def appendToFile(filename,text):
    with open(filename,'a+') as f:
        f.write(text + "\n")

def writeToFile(filename,text):
    with open(filename,'w') as f:
        f.write(text)

def identifyWorkspaceAndWrite(newname):
    info = subprocess.check_output("xprop -root -notype _NET_CURRENT_DESKTOP",shell=True)
    parts = info.split(' ') # split returned string into parts
    desktop_info = parts[2] # get '1\n' from array ['_NET_CURRENT_DESKTOP','=','1\n']
    desktop_num = desktop_info[0:-1] # get 1 from '1\n'
    filename = files[int(desktop_num)] # get the file that contains the name of the corresponding desktop
    print filename
    tobeClosed = readnameFromFile(filename)
    oldName = readnameFromFile(filename)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # If workspace has a real name, log that it is being closed
    if oldName and len(oldName) > 0 and oldName != "Empty":
        appendToFile("history.log","Stopped work on %s at time %s" % (oldName,timestamp))
    # If we're just emptying a workspace, don't log a new work session.
    if newname and len(newname) >= 0 and newname != "Empty": 
        appendToFile("history.log","Start work on %s at time %s" % (newname, timestamp))

    writeToFile(filename,newname)
    

#print files
#if len(sys.argv) == 2:
#    identifyWorkspaceAndWrite(sys.argv[1])
#else:
#    identifyWorkspaceAndWrite("Empty")

#renameUsingFiles(files)
