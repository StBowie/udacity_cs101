# 1 Gold Star

# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.


def split_string(source,splitlist):
	separators = []
	e = 0
	while e < len(splitlist):
		separators.append(splitlist[e])
		e = e + 1
	words = []
	start_position = 0
	end_position = 0
	while end_position < len(source):	
		while source[end_position] not in separators and end_position:
			end_position = end_position + 1
			if end_position == len(source) - 1:
				break
		words.append(source[start_position:end_position])
		if end_position == len(source) - 1:
			break
		start_position = end_position
		while source[start_position] in separators:
			start_position = start_position + 1
			if start_position == len(source) - 1:
				break
		end_position = start_position
	return words


out = split_string("This is a test-of the,string separation-code!"," ,!-")
print out
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print out
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print out
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']