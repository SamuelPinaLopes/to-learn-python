# function for saving thing in a file and check if that isn't already there
from datetime import date

def checkifisthere(message):
    messagelist = [message]

    with open('encripted-messages.txt', 'r+') as file:
        pass

def savemessage(message):
    messagelist = [message]
    dateoftoday = date.today()
    formated = ""
    with open("program001/encripted-messages.txt", 'r+') as file:
        file.write(f'{dateoftoday}' + '{' + f'{messagelist[0]}' + '}')
    

def joinlines(listofsentences):
    reallist = [listofsentences]
    # transform it in a single line
    pass