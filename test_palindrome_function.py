def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for letter in input_string:
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
		if letter != " ":
			new_string += letter.lower() 
			reverse_string = letter.lower() + reverse_string
	# Compare the strings
	
	if new_string == reverse_string:
		return True
	return False