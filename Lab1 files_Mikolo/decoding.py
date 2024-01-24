#This program extracts the coded word from the given string and prints, on 
#one line, the word in all uppercase, all lowercase and in reverse.

encoded = "abshpstekyhlpwop"

#Extract every 4th character from the string to form the 4 letter word
decoded = encoded[3::4]
wordAllUpper = decoded.upper()
wordAllLower = decoded.lower()
wordReverse = decoded[::-1]
print(wordAllUpper, wordAllLower, wordReverse)
