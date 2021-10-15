'''
1. Les orðin og mörkin inn í lista og prentar hann út
2. Fjarlægir greinarmerkin úr listanum með því að nota string.punctuation og prentar breyttan listann út.
3. Býr til uppflettitöflu þar sem:
        orðflokkar eru lyklar og gildin eru mengi af orðum sem tilheyra viðkomandi orðflokkum. 
4. Býr til uppflettitöflu þar sem:
        orðflokkar eru lyklar og gildin eru lengsta orðið (strengur) sem tilheyrir viðkomandi orðflokkum.
        Ef tvö orð eru jafn löng þá er lengsta orðið það sem kemur fyrr í stafrófinu. 
5. Prentar út gögnin úr uppflettitöflunni í lið 3 á ákveðin máta sem fram kemur í dæmi hér fyrir neðan.
        Bæði orðflokkarnir og orðin sem tilheyra sérhverjum orðflokki eru prentuð út í stafrófsröð.  
        Orðin eru prentuð út í hægri jöfnuðu svæði sem er 20 stafir að breidd.
6. Prentar út gögnin úr uppflettitöflunni í lið 4 á ákveðin máta sem fram kemur í dæmi hér fyrir neðan.
        Orðflokkarnir eru prentaðir út í stafrófsröð og lengsta orðið sem tilheyrir sérhverjum orðflokki er prentað út
        í hægri jöfnuðu svæði sem er 20 stafir að breidd.
'''
import string


def get_file(a_file):
    ''' Reads a filename and returns the file object '''
    try:
        file_object = open(a_file, 'r')
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
    ''' Creates and returns a dictionary from given list.
        Keys are words from previously given text file. Keys are corresponding tagged counterparts '''
    my_dict = {}
    keys_list = []
    values_list = []
    counter = 0

    for item in a_list:
        if counter % 2 == 0:
            keys_list.append(item)
            counter += 1
        else:
            values_list.append(item)
            counter += 1
    
    my_dict = dict(zip(keys_list,values_list))
    return my_dict

def sort_dict(a_dict):
    ''' Sorts the keys from a given dictionary into a new dictionary based on their values.
       (f=pronoun, s=verb, l=adjective, n=noun,  a=adverb/preposition, s=conjunction, t=numeral)'''
    f, s, l, n, c, a = [],[],[],[],[],[]
    my_dict = {}
    
    for key,value in a_dict.items():
        letter = value[0]
        if letter == "f":
            f.append(key)
            if 'f' in my_dict:
                my_dict['f'].append(key)
            else:
                my_dict['f'] = [key]
        elif letter == "s":
            s.append(key)
            if 's' in my_dict:
                my_dict['s'].append(key)
            else:
                my_dict['s'] = [key]
        elif letter == "l":
            l.append(key)
            if 'l' in my_dict:
                my_dict['l'].append(key)
            else:
                my_dict['l'] = [key]
        elif letter == "n":
            n.append(key)
            if 'n' in my_dict:
                    my_dict['n'].append(key)
            else:
                my_dict['n'] = [key]
        elif letter == "c":
            c.append(key)
            if 'c' in my_dict:
                    my_dict['c'].append(key)
            else:
                my_dict['c'] = [key]
        elif letter == "a":
            a.append(key)
            if 'a' in my_dict:
                    my_dict['a'].append(key)
            else:
                my_dict['a'] = [key]
    #return sorted(f), sorted(s), sorted(l), sorted(n), sorted(c), sorted(a)
    return my_dict

def get_longest(a_list):
    ''' Iterates through a list and returns only the longest word inside given list '''
    longest_word = ''
    for item in (a_list):
        if len(item) > len(longest_word):
            longest_word = item
    return longest_word

def main():
    filename = input("Enter file name: ")
    file_obj = get_file(filename)
    list_a = file_to_list(file_obj)
    print(list_a)
    print()
    list_b = remove_punc(list_a)
    print(list_b)
    print()
    dict_a = list_to_dict(list_b)
    print(dict_a)
    print()
    print()
    #f, s, l, n, c, a = sort_dict(dict_a)
    new_dict = sort_dict(dict_a)
    print(new_dict)
    
    #lf,ls,ll = get_longest(f),get_longest(s),get_longest(l)
    #ln,lc,la = get_longest(n),get_longest(c),get_longest(a)


# Main program starts here
if __name__ == "__main__":
    main()

''' Creates a dictionary from given list.
        Keys are word categories. Values are sets of words which belong to corresponding category '''