#Given a quote it generates the output as desired.

#The following quote is by John F. Kennedy, with some leading 
#and trailing spaces added.
quote = "   Man is still the most extraordinary computer of all.     "

#Print the quote and its length.
print("The given quote is:")
print(quote)
print("The length of the quote is:",len(quote))
print() #leave a blank line between output groups

#Print the quote and its length, without the leading blanks.
quote2 = quote.lstrip()
print("The quote without the leading blanks is:")
print(quote2)
print("The length of the quote is:",len(quote2))
print() #leave a blank line between output groups

#Print the quote and its length, without the leading and trailing blanks.
quote3 = quote.strip()
print("The quote without the leading and trailing blanks is:")
print(quote3)
print("The length of the quote is:",len(quote3))
print() #leave a blank line between output groups

#Print the quote without leading and trailing blanks and append the
#string " - John F. Kennedy" at the end.
print(quote3 + " - John F. Kennedy")
print() #leave a blank line between output groups

#Extract and print each word of the original quote from the string
#with leading and trailing blanks removed.
print("The list of words in the original quote are:")
print(quote.split())
