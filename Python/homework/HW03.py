"""HW03.py: Word Ladders"""
__author__ = "James Garrett"
__credits__ = ["Joe Snider"]
__email__ = "garretjb@mail.uc.edu"

def step(word):
    """
    >>> step("APPLE")
    ['ALEPPO', 'APPEAL', 'CAPPLE', 'DAPPLE', 'LAPPED', 'LAPPER', 'LAPPET', 'PALPED', 'PAPULE', 'RAPPEL', 'UPLEAP']
    """
    words = open('words.txt', encoding='ascii').read().upper().split()
    #print (len(words))

    compareString = '' #Create a separate string to store the word we think is an anagram
    outputList = [] #Create a separate list to store our anagrams
    for i in range(len(words)): #Loop through the entire dictionary
        if len(words[i]) == len(word) + 1: #Find words that are 1 letter longer than our inputted word
            compareString = words[i] #Set it as our compare string
            for j in range(len(word)): #Search through our inputted word for similar chars
                if compareString.find(word[j]) != -1: #Find a similar char, if it exists
                    index = compareString.find(word[j]) #If similar char exists, set our index equal to it
                    compareString = compareString[:index] + compareString[(index + 1):] #Delete the char from our compare string
            if len(compareString) == 1: #If only one character exists, then the word is what we're looking for
                outputList.append(words[i]) #Append the word to our output list
    return outputList

#Run
def _test():
    import doctest
    doctest.testmod(verbose=True)

if __name__ == '__main__':
    _test()
