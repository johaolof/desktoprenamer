
#!/usr/bin/env python

import rename_this_desktop
from rename_this_desktop import files,identifyWorkspaceAndWrite, renameUsingFiles
from Tkinter import *

master = Tk()
Label(master, text="New name").grid(row=0)

e1 = Entry(master)

e1.grid(row=0, column=1)

def do_rename(event):
    newname = e1.get()
    if not newname or len(newname) == 0:
        identifyWorkspaceAndWrite("Empty")
    else:
        identifyWorkspaceAndWrite(newname)
    renameUsingFiles(files)
    master.destroy()

master.bind('<Return>', do_rename);
e1.focus_force()
mainloop( )
