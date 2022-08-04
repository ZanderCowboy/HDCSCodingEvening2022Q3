# Create a function that, given a string with at least three characters, returns an array of its:
#
# Length.
# First character.
# Last character.
# Middle character, if the string has an odd number of characters.
# Middle TWO characters, if the string has an even number of characters.

# Index of the second occurrence of the second character in the format "@ index #" and "not found" if the second character
# doesn't occur again.
#
#
# Examples
# allAboutStrings("LASA") ➞ [4, "L", "A", "AS", "@ index 3"]
#
# allAboutStrings("Computer") ➞ [8, "C", "r", "pu", "not found"]
#
# allAboutStrings("Science") ➞ [7, "S", "e", "e", "@ index 5"]



# functions that gets length, first and last character, middle character(s) and index
def allAboutStrings(string):
	# initialization
	string_len = len(string)  # getting length of string
	new_array = []
	print("Printing string: " + string)


	# test whether the string is long enough
	if string_len < 3:
		print("The string given is not long enough. Exiting")
		exit()


	# getting first, last character and middle character(s)
	first_character = string[0]
	last_character = string[string_len - 1]

	if (string_len % 2 == 0): # even length string, returns middle two characters
		middle_len = int(string_len / 2)
		middle_character = string[middle_len] + string[middle_len+1]

	elif (string_len % 2 == 1): # odd length string, returns middle character
		middle_len = int(string_len / 2)
		middle_character = string[middle_len]


	# getting second character and getting index
	second_character = string[1]
	index_of_sec_occurrence = string.find(second_character, 2)


	# Appending to array all values
	new_array.append(string_len)
	new_array.append(first_character)
	new_array.append(last_character)
	new_array.append(middle_character)
	if (index_of_sec_occurrence == -1):
		new_array.append("not found")
	elif (index_of_sec_occurrence >= 0):
		at_index_append = "@ index " + str(index_of_sec_occurrence)
		new_array.append(at_index_append)

	# printing array
	print(new_array)



# calling function
allAboutStrings("LASA")
allAboutStrings("Computer")
allAboutStrings("Science")