
#For a given string s find the character c (or C) 
#with longest consecutive repetition and return:
#(c, l)

#where l (or L) is the length of the repetition. 
#If there are two or more characters with the same l 
#return the first in order of appearance.

import pdb; 
print('Enter a string gamer: ')
chars = input()

def rep(chars):
	input_string = chars
	length = len(input_string)-1
	max_char = ''
	max_count = 0
	check_char = ''
	count = 0

    for i in input_string:

        #if it's not, make it the same, increment count
        if check_char != i:
            count = 0
            check_char = i
            count = count + 1

        #set return values if you find the max
        if count > max_count:
            max_char = check_char
            max_count = count

        #otherwise increment count
        count = count + 1

	print(f'{max_char}, {max_count}')
	return (max_char, max_count)

rep(chars)