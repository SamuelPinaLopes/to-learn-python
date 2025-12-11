# crie um programa que encripta mensagems

def removeNewLines(tupla):
    sentence = [tupla]
    for howmuch in sentence: # get the full sentence
        allsentence = str(howmuch).replace('\n', '') # transform it to a string and change \n character for nothing
    return allsentence

def encript(tupla):
    # / -> espaço
    # * -> número
    # - -> separa números
    # 0123456789... -> letras
    alphabet = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25, ' ':26, ',':27, "'":28, '/':29, '*':30, '-':31, '?':32, '!':33, '.':34, '': 000}
    sentence = [tupla]
    """
    for encript the message, I'm going to search the word in the dictionary and see what type of number returns,
    like if I've a and b, the searching for that numbers will return 0 and 1, because in the alphabet dictionary I
    create this characters are in that position.
     """
    # get the values in the list
    for valueslist in sentence:
        returning = str()
        # I need to knonw the character of the sentence
        for value in valueslist:
            returning += str(alphabet[str(value).lower()])    
    return returning.replace('26', '-')

# main program

from program001.save_here import savemessage, joinlines

with open("folder001/mensagems.txt", "r") as arquivo:
    messageencripted = ""
    for lines in arquivo:
        messageencripted = encript(removeNewLines(lines))
    savemessage(joinlines(messageencripted))