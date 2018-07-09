def count_words(filename):
	""" Counts space separated words in a text file"""
	file = open(filename)

	count_dict = {}

	for line in file:
		line = line.rstrip()
		words = line.split(" ")
	
		# update dictionary line by line
		for word in words:
			count_dict[word] = count_dict.get(word, 0) + 1

	return count_dict


def print_dict_items(dictionary):
	""" Print key:value pairs of a dictionary."""
	for word, count in dictionary.items():
		print("{} {}".format(word, count))
	


# tests
print_dict_items(count_words('test.txt'))