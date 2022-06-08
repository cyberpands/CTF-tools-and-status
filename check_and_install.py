
import os
from queue import Empty
import subprocess
from unittest import result
from termcolor import colored
import pyfiglet
import sys

#------------------------------------Function to check apt_get file is present in the current directory--------------------------------#

def apt_get_file_check():
    apt_get_tool_list = []
    try:
        print(colored("\nReading File apt_get_list.txt...","green"))
        with open('apt_get_list.txt', 'r') as file:
            size = os.path.getsize('apt_get_list.txt')
            if( size > 0):
                #print(colored("\nChecking Status ... \n","green"))
                for line in file:
                    apt_get_tool_list.append(line.strip())
            else:
                sys.exit(1)              
    except:
        print(colored("\nError opening apt_get_list.txt or file may be empty !!","red"))
        sys.exit(1)
    return apt_get_tool_list

#------------------------------------Function to check git_clone file in present in the current directory--------------------------------#

def git_clone_file_check():
    git_clone_tool_list = []
    try:
        print(colored("\nReading File git_clone_list.txt...","green"))
        with open('git_clone_list.txt', 'r') as file:
            size = os.path.getsize('git_clone_list.txt')
            if( size > 0):
                #print(colored("\nChecking Status ... \n","green"))
                for line in file:
                    new_list = line.split(",")
                    git_clone_tool_list.append(new_list)
            else:
                sys.exit(1)                
    except:
        print(colored("\nError opening git_clone_list.txt or file may be empty !!","red"))
        sys.exit(1)

    return git_clone_tool_list

#------------------------------------Function to check whether the tools from the list are installed in the system if not then call apt_get_tool_install function--------------------------------#

def apt_get_tool_check(tool_name):
    try:
        for i in tool_name:
            result = subprocess.call(['which', i], stdout=subprocess.DEVNULL)
            if(result == 0):
                print(colored("\n[+] ","green") + i + " : " + colored("Installed", "green"))
            else:
                print(colored("\n[+] ","red") + i + " : " + colored("Not Installed", "red"))
                apt_get_tool_install(i)
    except:
        print(colored("\nError Checking status of tools","red"))

#------------------------------------Function to check whether the script from the list is found in the system and if not then call git_clone_tool_install function--------------------------------#

def git_clone_tool_check(tool_name):
    try:
        general_list = []
        for i in tool_name:
            cmd_to_locate = i[0].strip()
            #print(cmd_to_locate)
            cmd = ["locate", cmd_to_locate]
            result = subprocess.check_output(cmd)
            result_decode = result.decode()
            if result_decode != '':
                print(colored("\n[+] ","green") + cmd_to_locate + " : " + colored("Found", "green"))
                print(colored("[+] ","blue") + "Location" + " : " + colored(f"{result_decode}"))
            else:
                print(colored(f"\n{cmd_to_locate} : Not Found", "red"))
                git_clone_tool_install(i)
    except:
        print(colored("\nError in checking files ...","red"))

#------------------------------------Function to install the tool and check for its presence onece again--------------------------------#

def apt_get_tool_install(tool):
    try:
        print(colored(f"\nTrying to install {tool} ...","green"))
        subprocess.run(["sudo","apt-get", "-y", "install", tool])
        result = subprocess.call(["which", tool], stdout=subprocess.DEVNULL)
        if(result == 0):
            print(colored(f"\n{tool} : Installed Successfully","green"))
        else:
            print(colored(f"\n{tool} : Not Installed. Try checking the command","red"))
    except:
        print(colored(f"\nError Installing {tool}"))

#------------------------------------Function to install tools using git clone and check for its presence with after updating the system database--------------------------------#

def git_clone_tool_install(tool):
    try:
        print(colored(f"Downloading : {tool[0]}","green"))
        link = tool[1].strip()
        print(link)
        subprocess.run(["git", "clone", link])
        subprocess.run(["sudo", "updatedb"])  #---> used to update the system databse and that helps in locating the recent downloaded files or scripts
        cmd = ["locate", tool[0]]
        result = subprocess.check_output(cmd)
        result_decode = result.decode()
        if result_decode != '':
            print(colored("\n[+] ","green") + f"{tool[0]} : " + colored("Download Successful","green"))
            print(colored("[+] ","blue")  + f"Location : {result_decode}")
        else:
            print(colored(colored("\n[+] ","red") + f"{tool[0]} : " + colored("Download not successful. Check link and try again","red")))  

    except:
        print(colored(f"\nError downloading {tool[0]}","red"))


#------------------------------------Main Function--------------------------------#


while True:
    print("---------------------------------------------------------------------------------")
    banner = pyfiglet.figlet_format("Tool Checklist :-)")
    print(colored(banner, "green"))
    print(colored("-cyberpands","red"))
    print("---------------------------------------------------------------------------------")
      
    check_list_1 = print("\n1. Check status and install")
    check_list_3 = print("2. Exit")
    user_in = input("\nInput: ")

    try:
        if(user_in.isnumeric() is not True):
            print("\nOnly Integer Required!!\n")
            sys.exit(1)
        else:
            if (user_in == '1'):
                try:
                    apt_get_list = apt_get_file_check()
                    git_clone_list = git_clone_file_check()
                    print("Both File exists.")
                    print("Checking status and installing ...\n")
                    if((apt_get_list and git_clone_list) != ''):
                        apt_get_tool_check(apt_get_list)
                        git_clone_tool_check(git_clone_list)
                        
                    else:
                        print(colored("\nFile Empty","red"))
                        sys.exit(1)
                except:
                    print("\nError in checking status!!")

            elif (user_in == '2'):
                print(colored("\nExiting ...\n","red"))
                break

            else:
                print(colored("\nUnknown number. Exiting program ...\n","red"))
                break
    except:
        sys.exit(1)
