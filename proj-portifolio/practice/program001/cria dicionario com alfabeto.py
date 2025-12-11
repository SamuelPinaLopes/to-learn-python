alphabet = 'abcdefghijklmnopqrstuvwxyz'

# alphabet_position_dict = {char: i for i, char in enumerate(alphabet)}

alphabet_position_dict = dict()

for i, char in enumerate(alphabet):
    alphabet_position_dict[char] = i

print(alphabet_position_dict)