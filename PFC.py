# +--------------------------------------------------+
# |                                                  |
# |             Project Folder Creator               |
# |               January 7th, 2014                  |
# |                  Daniel Linge                    |
# |                                                  |
# +--------------------------------------------------+
#
# version 1.2

#!/usr/bin/python

import os, logging, time, sys

# Print program title
def title():
    print
    print "Project Folder Creator 2014"
    print '---------------------------'
    print
    
# Defining Variables
home = os.path.expanduser("~")
check = 0
homeList =[]
yes = set(['yes','y'])
no = set(['no','n'])  
clientList =[]
proFolder = str(home) + "/Projects"

# Delay printing to screen
def delay_print(s):
    for c in s:
        sys.stdout.write('%s' % c)
        sys.stdout.flush()
        time.sleep(0.25)
    return
    
# Ask for Client name
def clientInput():
    global client
    client = raw_input("What Client? ") 
    print
    return client
    
# Ask for Project name    
def projectInput():
    global project
    project = raw_input("What Project? ") 
    print
    return project
     

# Go to projects folder or Create if not there.
def projectCreate():
    os.chdir(home) # Move to Home Folder
    for homefolders in os.listdir(home): # Check for Projects Folder
        homeList.append(homefolders)
        check = homeList.count("Projects")
        if check == 1:
            os.chdir("Projects")
            break
        else:
            check == 0
    if check == 0: # If no Project Folder in Home one is created
        print
        print "No Project Folder Detected"
        print
        while True:  # or we change directories to user's Projects Folder
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
                
# Creates Client
def clientCreate(client):
    for clientfolders in os.listdir(proFolder): # See if Client Already Exists
        clientList.append(clientfolders)
        check = clientList.count(client)
        client_check = 0
        if clientfolders == client:
            os.chdir(client)
            client_check += 1
            break
        else:
            pass
    if client_check == 0:
        os.mkdir(client)
        os.chdir(client)
    else:
        os.chdir(client)

# Creates all Directors in Project         
def createFolders(project):
    if project == "0":
        pass
    else:
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
    os.mkdir("03_Scripts")
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
    return

# Ending Stats
def stats(client, project):    
    print '---------------------------'
    print
    print "Client: %s" % client
    if project != "0":
        print "Project: %s" % project
    print
    print "Folders Created in %s" % os.getcwd()
    print
    print '---------------------------'
    print
    logging.info("Client: %s" % client)
    logging.info("Project: %s" % project)
    logging.info("Folders Created in %s" % os.getcwd())
    if __name__ == "__main__":
        answer = raw_input("Do you want to make another project? ") # Restart Program
        print
        logging.info("restart?: %s" % answer)
        if answer in yes:
            print "Restarting"
            delay_print(". . . . . .")
            print
            print
            main()
            
#Program Running Order
def main():
    title()
    logging.basicConfig(filename='PFC.log',level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.warning('is when this event was logged.')
    logging.info("Started")
    clientInput()
    projectInput()
    projectCreate()
    clientCreate(client)
    createFolders(project)
    stats(client, project)
    logging.info("Finished")
    
#Running Program
if __name__ == "__main__":
    main()
        
        
            