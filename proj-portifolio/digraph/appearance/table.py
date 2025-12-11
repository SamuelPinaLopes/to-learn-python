# recieve a dictionary
# dictionary structure -> {'A':numberofsomething, 'B':numberofsomething}
def show_graph(numbers, whatconextion):
    # variable area
    dictionary = dict(numbers)
    indexofcoluns = dict()
    
    # for the coluns (keys coluns)
    print("|", spaces(2), end='|')
    for number, thing in enumerate(dictionary.keys()):
    
        # the coluns
        if number < len(dictionary) - 1:
            # printing colum
            print(spaces(1), thing, end=spaces(2) + "|")
            # guardando a posição de cada letra
            indexofcoluns[thing] = number
        
        else:
            indexofcoluns[thing] = number
            print(spaces(1), thing, " |")


    # for the lines (vertical keys)
    for thing in dictionary.keys():
        # vertical keys
        print("|", thing, end=" |")
    
        # put space in front of the hand lyric
        number_to_multiple = indexofcoluns[ # get number of spaces
            whatconextion[thing] # get a conextion of a current lyric
        ]
        # put the spaces on the screen
        for value in range(number_to_multiple):
            print(end=spaces(5) + f"|")
        print(spaces(1), dictionary[thing], spaces(1) + "|")
        # completting other spaces after put a number

# function only to fit spaces between things
def spaces(howmuch):
    return " " * howmuch



# print(dictionary)
# for chave in dictionary.keys():
#     print("this is the value -> {}".format(chave))
    
# for thing in dictionary.values():
#     print(f"each hand lyric -> {thing}")

# for itemtuple in dictionary.items():
#     print(f"this is each item in dictionary -> {itemtuple}", end='')
#     print(itemtuple[0], itemtuple[1])
# print(dictionary.keys())
# print(dictionary.values())
# print(dictionary.items())
