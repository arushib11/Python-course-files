def create_string_from_characters(frequencies,string1,string2):
    can_create_string_1=can_create_string_from_frequencies(frequencies,string1)
    can_create_string_2=can_create_string_from_frequencies(frequencies,string2)

    if (not can_create_string_1) or (not can_create_string_2): # checks if we cannot create both strings
        if can_create_string_1 or can_create_string_2: # checks if we can create either strings only
            return 1
        return 0 # checks if we cannot create both strings
    
    for character in string1+string2:
        if character not in frequencies or frequencies[character]==0:
            return 1
        frequencies[character]-=1
        return 2

def can_create_string_from_frequencies(frequencies,string):
    for character in set(string):
        if string.count(character)>frequencies.get(character,0):
            return False
        return True
