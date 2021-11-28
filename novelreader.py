# Words in The Great Gatsby

#Read text of TGG and count unique words
#perhaps later find phrases
#as compared to modern dictionary

import string


fname = input("Enter file name: ")
try:
    if len(fname) < 1 : fname = "gatsby_short.txt"
    handle = open(fname, encoding="utf-8")
except:
    print("Error, please enter a file name")
    quit()

wordList = list() # a list of values whereas str is a sequence of characters
newList = list()

count = 0
for line in handle:
    # print(len(wordsLinesCharacter))
    # print(wordsLinesCharacter[:20])
    wordList = line.split()
    for word in wordList: # split into list of words
        count += 1
        if word not in newList:
            newList.append(word)
            newList.sort()
print(newList)
print(count)
