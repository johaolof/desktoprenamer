# gsettings set org.gnome.desktop.wm.preferences workspace-names ['Test','Again','Yada']
#!/usr/bin/python

import subprocess
import rename_desktops
from rename_desktops import namefiles 

def writeToFile(filename,newname):
    with open(filename) as f:
        f.write(newname)

info = subprocess.check_output("xprop -root -notype _NET_CURRENT_DESKTOP",shell=True)
parts = info.split(' ') # split returned string into parts
desktop_info = parts[2] # get '1\n' from array ['_NET_CURRENT_DESKTOP','=','1\n']
desktop_num = desktop_info[0:-1] # get 1 from '1\n'
filename = namefiles[int(desktop_num)] # get the file that contains the name of the corresponding desktop
print filename
if len(sys.argv) == 2:
    writeToFile(filename,sys.argv[1])
else:
    writeToFile(filename,"Empty")

