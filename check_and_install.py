import os
import subprocess
from termcolor import colored
import pyfiglet
import sys


def apt_get_file_check():
    try:
        print(colored("\nReading File apt_get_list.txt...","green"))
        apt_get_tool_list = []
        with open('apt_get_list.txt', 'r') as file:
            size = os.path.getsize('Tools_list.txt')
            if( size > 0):
                print(colored("\nChecking Status ... \n","green"))
                for line in file:
                    apt_get_tool_list.append(line.strip())
            else:
                sys.exit(1)              
    except:
        print(colored("\nError opening apt_get_list.txt or file may be empty !!","red"))
        sys.exit(1)
    return apt_get_tool_list


def git_clone_file_check():
    try:
        print(colored("\nReading File ...","green"))
        git_clone_tool_list = []
        with open('git_clone_list.txt', 'r') as file:
            size = os.path.getsize('Tools_list.txt')
            if( size > 0):
                print(colored("\nChecking Status ... \n","green"))
                for line in file:
                    git_clone_tool_list.append(line.strip())
            else:
                sys.exit(1)                
    except:
        print(colored("\nError opening git_clone_list.txt or file may be empty !!","red"))
        sys.exit(1)

    return git_clone_tool_list


def apt_get_tool_check():
    result = subprocess.call(['which', "nameoftool"], stdout=subprocess.DEVNULL)
    print("CHECK")
    #call apt_get_tool_install function


def git_clone_tool_check():
    print("CHECK")



def apt_get_tool_install():
    #install here
    print("INSTALL")


def git_clone_tool_install():
    print("INSTALL")




print("---------------------------------------------------------------------------------")
banner = pyfiglet.figlet_format("Tool Checklist :-)")
print(colored(banner, "green"))
print(colored("-cyberpands","red"))
print("---------------------------------------------------------------------------------")
      


while True:
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
                    print(apt_get_list)
                    print(git_clone_list)
                except:
                    print("\nError in checking status!!\n")

            elif (user_in == '2'):
                print("Exiting ... ")
                break

            else:
                print("Unknown number. Exiting program ...")
                break
    except:
        sys.exit(1)
