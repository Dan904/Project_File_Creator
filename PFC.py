# +--------------------------------------------------+
# |                                                  |
# |             Project Folder Creator               |
# |               January 7th, 2014                  |
# |                  Daniel Linge                    |
# |                                                  |
# +--------------------------------------------------+
#
# version 1.1

#!/usr/bin/python

import os

# Print program title
print
print "Project Folder Creator 2014"
print '---------------------------'
print




# Move to Home Folder
home = os.path.expanduser("~")
os.chdir(home)

# Check for Projects Folder
check = 0
homeList =[]
for homefolders in os.listdir(home):
    homeList.append(homefolders)
    check = homeList.count("Projects")
    if check == 1:
        os.chdir("Projects")
        break
    else:
        check == 0

# If no Project Folder in Home one is created
# or we change directories to user's Projects Folder
if check == 0:
    print
    print "No Project Folder Detected"
    print
    yes = set(['yes','y'])
    no = set(['no','n'])   
    while True:
        newproject = raw_input("Do you want to make a Main Projects folder, Yes or No?").lower()
        if newproject in yes:
            os.mkdir("Projects")
            os.chdir("Projects")
            break
        elif newproject in no:
            print
            print "We are in %s" % os.getcwd()
            dif = raw_input("Where is your Project Folder? (Full Path Please)")
            print "Moving to " + dif
            os.chdir(dif)
            break
        else:
            print "I'm sorry, I didn't understand. Please type 'Yes' or 'No'"
            print
            
# Ask for Client name
client = raw_input("What Client?")
print

# Ask for Project name
project = raw_input("What Project?")
print

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

# Going back to Projects
os.chdir('../')
if project != "only one":
    os.chdir('../')

# Ending Stats    
print '---------------------------'
print
print "For Client: %s" % client
if project != "only one":
    print "For Project: %s" % project
print
print "Folders Created in %s" % os.getcwd()
print
print '---------------------------'