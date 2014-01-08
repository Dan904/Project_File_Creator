# +--------------------------------------------------+
# |                                                  |
# |             Project Folder Creator               |
# |               January 7th, 2014                  |
# |                  Daniel Linge                    |
# |                                                  |
# +--------------------------------------------------+
#
# version 1.0

#!/usr/bin/python

import os

# Make Project File
os.chdir("../")
if os.path.isdir("./Projects"):
    os.chdir("Projects")
else:
    os.mkdir("Projects")
    os.chdir("Projects")

# Ask for Client name
client = raw_input("What Client?")

# Ask for Project name
project = raw_input("What Project?")

if project == "only one":
    os.mkdir(client)
    os.chdir(client)
else:
    os.mkdir(client)
    os.chdir(client)
    os.mkdir(project)
    os.chdir(project)


# Add Main Folders
os.mkdir("00_Finals")
os.mkdir("01_Documents")
os.mkdir("02_RAWZ")
os.mkdir("03_Elements")
os.mkdir("04_Project_Files")

# Add Folders for Finals
os.chdir("00_Finals")
os.mkdir("00_Cuts")
os.chdir("../")

# Add Folders for Documents
os.chdir("01_Documents")
os.mkdir("01_Invoices")
os.mkdir("00_Contracts")
os.mkdir("02_Reciepts")
os.chdir("../")

# Add Folders for RAWZ
os.chdir("02_RAWZ")
os.mkdir("00_Client_Footage")
os.chdir("../")

# Add Folders for Elements
os.chdir("03_Elements")
os.mkdir("01_Brushes")
os.mkdir("02_Fonts")
os.mkdir("03_Logos")
os.mkdir("04_Overlays")
os.mkdir("05_Refrence")
os.mkdir("06_Textures")
os.mkdir("07_Titles")
os.mkdir("08_Audio")
os.chdir("../")

# Add Folders for Project Files
os.chdir("04_Project_Files")
os.mkdir("Backup Projects")
os.chdir("../")

