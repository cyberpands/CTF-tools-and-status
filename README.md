<img src="https://drive.google.com/file/d/1kqyeKA7WR5x91swGqHJyW_wswynTJr6c/view?usp=sharing">

# Description
A basic program that checks for all the tools present in the lists and, based on the results, tries to install them along with their location if a particular tool is not found or installed. These are the fundamental tools that can be utilised by a variety of people prior to performing CTFs.

# Working
The apt_get_list contains all the tools that can be installed directly with ```sudo apt-get -y install tool_name```. While git_clone_list contains the main script name (ex: LinEnum.sh) and its github link.

# Usage 
    python3 check_and_install.py

# Note
>You can add your tools name in apt_get_list and in git_clone_list you can add main script name and its github link seperated by comma. While running the script remember the keep the two list is the same directory.