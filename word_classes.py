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
            counter -= 1 # Counter deducected by 1 to account for the deleted index
            
    return temp_list


def main():
    filename = input("Enter file name: ")
    file_obj = get_file(filename)
    word_list = file_to_list(file_obj)
    print(word_list)
    new_list = remove_punc(word_list)
    print(new_list)



# Main program starts here
if __name__ == "__main__":
    main()
