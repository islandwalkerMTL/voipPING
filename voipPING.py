import os
import datetime

now = datetime.datetime.now()
resultfile = "voiPing_log" + now.strftime("%Y-%m-%d-%H:%M") + ".txt"


def load_pingFile(filename):
    with open(filename,"r") as f:
        ping_data = f.read().splitlines()
    return ping_data

def loadServerlist(filename):
    with open(filename,"r") as f:
        serverline = f.read().splitlines()
    return serverline


def pingServer(servername):
    string = "ping -c 5 " + servername
    os.system(string + ">> " + resultfile)


def pingallservers(filename):
    serverlist = loadServerlist(filename)

    for servername in serverlist:
        print "Pinging %s..." % servername
        pingServer(servername)


def analyze(filename):
    i = 0
    lines = load_pingFile(filename)
    for line in lines:

        if line[0:3] == '---':
            print line.split(" ")[1] + ": " +lines[i+2].split("/")[4]
        i += 1

def menu():
    choices = [1,2,3,4]
    choice = 0
    while True:
        while choice not in choices:


            print('*********************************************')
            print("            _       _____ _____ _   _  _____ ")
            print("           (_)     |  __ \_   _| \ | |/ ____|")
            print("__   _____  _ _ __ | |__) || | |  \| | |  __ ")
            print("\ \ / / _ \| | '_ \|  ___/ | | | . ` | | |_ |")
            print(" \ V / (_) | | |_) | |    _| |_| |\  | |__| |")
            print("  \_/ \___/|_| .__/|_|   |_____|_| \_|\_____|")
            print("              | |                            ")
            print("              |_|                            ")
            print('          '+ u"\u00a9" +'ooellis@gmail.com 2017')
            print('*********************************************')
            print('                                             ')

            print('                                             ')
            print('***************Choose an option**************')
            print('                                             ')
            print('1: Ping all servers and analyze')
            print('2: Ping all servers')
            print('3: Analyze a file')
            print('4: Quit the program')

            choice = input('Choose an option and hit Enter --> ')

            if choice == 1:

                pingallservers("serverlist.txt")
                analyze(resultfile)


            elif choice == 2:
                pingallservers("serverlist.txt")



            elif choice == 3:
                ping_filename = raw_input('File name of the results to analyze --> ')
                print "Results:"
                analyze(ping_filename)



            elif choice == 4:
                exit()

            choice = 0


menu()
