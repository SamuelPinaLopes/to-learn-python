# first version of the program that let's you to rename a lot of folders with the same style
# this didn't work well, have a bug, when you Have more then one folder to rename within the same root folder

import os
import subprocess

# path to a directory to go inside and start change things
cwd = 'c:/test2'

# function used
def list_folder_inside_path(whatpath):
    # from what path the program was started
    cwd = os.getcwd()
    # changing the directory
    os.chdir(whatpath)
    # get the paths after change the directory
    allfolders = os.listdir()
    # change again to the cwd
    os.chdir(cwd)
    # return all folders and files finded
    return allfolders

def remove_files(pathtocheck, folder):
    newlist = list()
    for each in folder:
        if os.path.isdir(pathtocheck + "/" + each):
            newlist.append(each)
    return newlist        

def is_in_list(list1, list2, list_mode=True):
    if list_mode == True:
        for thing in list1:
            if thing in list2:
                return True
    else:
        return list1 in list2
    return False

def remove_space_and_others_things(sentence, things=''):
    # the sentence to change
    sentencereturn = f'{sentence}'.lower()
    # a list of other things you don't want in the final sentence (replace all to nothing)
    for each in things:
        sentencereturn = sentencereturn.replace(each, '')
    # return the final string
    return f'{sentencereturn}'.replace(' ', '_').replace('__', '_')

def remove_accents(sentence):
    list_accents = {'ã':'a', 'à':'a', 'á':'a', 'ç':'c', 'ò':'o', 'õ':'o', 'ó':'o', 'í':'i','ì': 'i', 'é':'e', 'è': 'e', 'ú': 'u', 'ù':'u'}

    frase = f'{sentence}'.lower()
    
    for accents_key, accents_value in list_accents.items():
        frase = f'{frase}'.replace(accents_key, accents_value)

    return frase

def remove_last_folder_own(path):
    sentence = f"{path}"
    return sentence[0:sentence.rfind('/')]

def the_same(first_thing, second_thing):
    if first_thing == second_thing:
        return True
    else:
        return False



""" main program """



# add folder name to path variable until you have any folder inside a directory
path_list = []
list_of_folders = []
path_visited = []
deleted_paths = 0
pathchanged = ''

# this will get the folders
while True:
    if len(path_list) > 0:
        # go inside each path if isn't in path_visited
        for index, path in enumerate(path_list):
            # do this only if that path isn't in path_visited
            if is_in_list(path, path_visited) == False:
                # find folders inside the path
                list_of_folders = remove_files(path, list_folder_inside_path(path))
                # add path to visited paths, because you don't need to go inside it again
                path_visited.append(path)
                # create new paths with finded folders

                for eachfolder in list_of_folders:
                    path_list.append(path + "/" + eachfolder)
                
            else:
                # remove that path
                path_list.pop(index - deleted_paths)
                deleted_paths += 1
        
    else:
        # get folders inside the first path
        list_of_folders = remove_files(cwd, list_folder_inside_path(cwd))
        # create the first new paths to folders inside the cwd passed
        for eachfolder in list_of_folders:
            path_list.append(cwd + "/" + eachfolder)    
        # if the path isn't in the list, go inside it
    # stop if the program can't find more paths
    if len(list_of_folders) == 0:
        break

path_visited.clear()
problems = list()

# this will rename that path to folders you getted
for path in path_list:
    # this set the path to remove the last folder
    pathchanged = remove_space_and_others_things(remove_accents(path), '-') # this is for you change the name and is going to be used to change the path name 
    original_path = path # this is for the windows can go inside each path you want to rename
    print(original_path)
    print(pathchanged)

    try:
        os.rename(
            original_path,
            pathchanged
        )
    except Exception as wrong:
        print("this path have a problem: {}".format(original_path))
        problems.append("the exception was this: {}".format(wrong))
    if path == path_list[-1]:
        break

""" this is how to remove double folder path, path inside other path """
# remove double folder path, to do that you should check the last folder if that 
# last folder is already inside another folder path, you should remove it, because
# you already go through that folder in the other path, you don't need to go through
# that folder twice.
