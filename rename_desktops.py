# gsettings set org.gnome.desktop.wm.preferences workspace-names ['Test','Again','Yada']
#!/usr/bin/python

import subprocess

namefiles = [
        'Left1.txt','Right1.txt',
        'Left2.txt','Right2.txt',
        'Left3.txt','Right3.txt',
        'Left4.txt','Right4.txt'
        ]
#setCmd = "gsettings set org.gnome.desktop.wm.preferences workspace-names ['Test','Again','Yada']"
#print setCmd

def readnameFromFile(filename):
    with open(filename) as f:
        return f.read().rstrip()

names = [ readnameFromFile(x) for x in namefiles ]
newnames = "'" + "','".join(names) + "'"

setCmd = "/usr/bin/gsettings set org.gnome.desktop.wm.preferences workspace-names \"[%s]\"" % newnames
print setCmd

subprocess.check_output(setCmd,shell=True)
