import sys

def count_words(filename):
	""" Counts space separated words in a text file"""
	file = open(filename)

	count_dict = {}

	for line in file:
		line = line.rstrip()
		words = line.split(" ")
	
		# update dictionary line by line
		for word in words:
			# make sure the word is letters only
			word = make_alpha(word)

			# add to dictionary or increment
			count_dict[word.lower()] = count_dict.get(word.lower(), 0) + 1

	return count_dict


def print_dict_items(dictionary):
	""" Print key:value pairs of a dictionary."""
	for word, count in dictionary.items():
		print("{} {}".format(word, count))
	

def make_alpha(word_candidate):
	""" Make sure the word is only letters.

	details here...
	"""
	if not word_candidate.isalpha():
		# word has a symbol
		word = word_candidate[:len(word_candidate) - 1]
		return word

	return word_candidate


# tests
print_dict_items(count_words(sys.argv[1]))