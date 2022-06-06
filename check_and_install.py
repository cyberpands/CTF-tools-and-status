import os
import subprocess
from termcolor import colored
import pyfiglet
import sys

list_of_tools = []

def file_check():
    try:
        print(colored("\nReading File ...","green"))
        with open('Tools_list.txt', 'r') as file:
            size = os.path.getsize('Tools_list.txt')
            if( size > 0):
                print(colored("\nChecking Status ... \n","green"))
                for line in file:
                    list_of_tools.append(line.strip())
            else:
                sys.exit(1)                
    except:
        print(colored("\nError opening Tools_list.txt or file may be empty !!","red"))
        sys.exit(1)
        

def install_tools(tool_name):
    try:
        cmd = ["sudo","apt-get","install",tool_name]
        result = subprocess.call(cmd)
        res_new = subprocess.call(["which", tool_name])
        if (res_new == 0):
            print("WOWOWOWOWOWOWO")
        else:
            print("NOOOOOOOOOOOOOOOOs")
        print("\n")




    except:
        print("Error")
    
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
                    file_check()
                    for i in list_of_tools:
                        result = subprocess.call(['which', i], stdout=subprocess.DEVNULL)
                        if (result == 0):
                            print(i + " : " + colored("Installed","green") + "\n")
                        else:
                            print(i + " : " + colored("Not Installed","red"))
                            install_tools(i)
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
