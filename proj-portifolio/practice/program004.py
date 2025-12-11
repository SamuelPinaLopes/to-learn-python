# second version of "program002-renaming foldes"
# importing the things I need
import sys
import subprocess
import os

#       functions for the program
# get the folders inside a folder path
def get_folders_here(path_folder):
    return os.listdir(path_folder)

# checking if it is a folder
def is_it_folder(path_to_folder):
    return os.path.isdir(path_to_folder)

# create paths
def new_path(old_path, folder):
    return f"{old_path}\\{folder}"

# rename the folders to a standard way

# apply the changes

#       main program

# test area
cwd = "c:\\test2"
list_of_folders = get_folders_here(cwd)
for each in list_of_folders:
    if is_it_folder(cwd + "\\" + each) == True:
        print("this is a folder: {}".format(each))
    else:
        print("this is not a folder!\nthis: {}".format(each))