#Write a function that takes in a string of one or more words, and returns the same string, 
#but with all five or more letter words reversed (Just like the name of this Kata). 
#Strings passed in will consist of only letters and spaces. Spaces will be included
#only when more than one word is present.
#Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
#spinWords( "This is a test") => returns "This is a test" 
#spinWords( "This is another test" )=> returns "This is rehtona test"
def spin_words(sentence):

    #splitting the string into a list
    sentence = list(sentence.split())
    flipped = ''

    #checking every list item to flip it based on length
    #and concatenate the new string
    for i in sentence:
        if len(i) >= 5:
            flipped = flipped + i [::-1] + ' '
        else:
            flipped = flipped + i + ' '

    #trimming the excess space off the string's last character
    flipped = flipped[:-1]

    return flipped 