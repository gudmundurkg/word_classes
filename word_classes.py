'''
Höfundur: Guðmundur Kristján Guðnason (gudmundurkg20)
'''

import string


def get_file(a_file):
    ''' Reads a filename and returns the file object '''

    try:
        file_object = open(a_file, 'r',encoding="utf-8")    
        return file_object
    except FileNotFoundError:
        print(f"File {a_file} not found!")

def file_to_list(file_object):
    ''' Gathers all words from a file object and returns them in a single list '''

    my_list = []

    for line in file_object:
        line = line.split()
        for word in line:
            my_list.append(word)
    return my_list

def remove_punc(a_list):
    ''' Iterates through a list and removes all punctuations '''

    counter = -1
    temp_list = a_list[:]
    punc = string.punctuation

    for item in a_list:
        counter += 1
        if item in punc:
            del temp_list[counter] # Removes item at current index if it is a punctuation
            counter -= 1 # Counter reduced by 1 to account for the deleted index       
    return temp_list

def list_to_dict(a_list):
    ''' Creates and returns a dictionary from given list. Keys of dictionaries are word classes:
        (f=pronoun, s=verb, l=adjective, n=noun,  a=adverb/preposition, s=conjunction, t=numeral).
        Values are: words from given text file sorted into said word classes. '''
        
    my_dict = {}

    for item in range (1, len(a_list),2):
        tagged_key = a_list[item][0]
        if tagged_key not in my_dict:
            my_dict[tagged_key] = set([a_list[item- 1]]) #Convert to set() to remove duplicate values
        else:
            my_dict[tagged_key].add(a_list[item - 1])
    return my_dict

def get_longest(a_dict):
    ''' Iterates through a dictionary and returns the longest word for each key '''

    longest_dict = {}
    longest_word = ''
    
    for key,values in a_dict.items():
        for word in sorted(values):
            if len(word) > len(longest_word):
                longest_word = word
        longest_dict[key] = longest_word
        longest_word = '' 
    return longest_dict

def print_class_dict(a_dict):
    ''' Prints given dictionary with proper formatting if value pr. key is > 1 '''

    for keys,values in sorted(a_dict.items()):
        print(f"{keys}:")
        for i in sorted(values):
            print(f"{i:>20}")

def print_longest_dict(a_dict):
    ''' Prints given dictionary with proper formatting if value pr. key is == 1 '''

    for keys,values in sorted(a_dict.items()):
        print(f"{keys}:")
        print(f"{values:>20}")

def main():
    filename = input("Enter file name: ")
    file_obj = get_file(filename)
    print()
    list_a = file_to_list(file_obj)
    print(list_a)
    print()
    list_b = remove_punc(list_a)
    print(list_b)
    print()
    word_classes_dict = list_to_dict(list_b)
    print_class_dict(word_classes_dict)
    print()
    longest_dict = get_longest(word_classes_dict)
    print_longest_dict(longest_dict)
    
# Main program starts here
if __name__ == "__main__":
    main()

