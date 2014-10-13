"""
Simple implementation of a shift cipher breaker (supports spurious keys, uses dictionary).
"""

import sys

def find_spurious_keys(n, dictionary, output_file):
	""" Find (if any) at most n spurious keys using the given dictionary """
	spurious = []
	min_length = 5
	for w in dictionary:
		for k in xrange(1, 26):
			# Exclude short words
			if len(w) < min_length:
				continue
			# if w.index("river") == 0:
			shifted_w = shift(w, k)
			for subk in xrange(1, 26):
				for subw in dictionary:
					if len(subw) >= min_length and subw != w:
						# if subw.index("arena") == 0:
						shifted_subw = shift(subw, k)
						# print "Using %s (%d) -> %s , %s (%d) -> %s\n" % (w, k, shifted_w, subw, subk, shifted_subw)
						if (shifted_subw == shifted_w):
							tupl = (w, shifted_w, k, subw, shifted_subw, subk)
							spurious.append(tupl)
							output_file.write(str(tupl))
							output_file.flush()

						if len(spurious) >= n:
							break
	return spurious


def shift(text, key):
	shifted = ""
	for i in xrange(0, len(text)):
		shifted += chr((((ord(text[i]) - 97) + key) % 26) + 97)
	return shifted

def find_word(text, dictionary):
	# print "Looking for " + text + "..."
	for w in dictionary:
		if text == w:
			# print "Found! " + w
			return True
	return False

def break_ciphertext(ciphertext, dictionary):
	plaintexts = []
	cur_word = ""

	for k in xrange(0, 26):
		# Shift with the key
		cur_word = shift(ciphertext, k) 
		if find_word(cur_word, dictionary):
			plaintexts.append((cur_word, str(k)))
		cur_word = ""
	return plaintexts

def print_usage_break(name):
	print "Usage: " + name + " break path_to_dictionary path_to_resulting_plaintext path_to_ciphertext"

def print_usage_findspurious(name):
	print "Usage: " + name + " spurious path_to_dictionary path_to_dump_file"

def main(args):
	if (len(args) < 2):
		print_usage_break(args[0])
		print_usage_findspurious(args[0])
		exit()
	operation = args[1]
	dictionary_file = args[2]
	dictionary = open(dictionary_file, "r").readlines()
	ciphertext_file = None
	ciphertext = None
	output_file = args[3]
	output_file_obj = open(output_file, "w", 0)
	# Remove all whitespaces from the dictionary
	for i in xrange(0, len(dictionary)):
		dictionary[i] = dictionary[i].strip()

	if operation == "break":
		if len(args) < 5:
			print_usage_break(args[0])
			exit()
		ciphertext_file = args[4]
		ciphertext = "".join(open(ciphertext_file, "r").readlines())
		plaintexts = break_ciphertext(ciphertext, dictionary)
		output_file_obj.write(str(plaintexts))
	if operation == "spurious":
		if len(args) < 3:
			print_usage_findspurious(args[0])
			exit()
		spurious_keys = find_spurious_keys(3, dictionary, output_file)
		
	output_file_obj.close()	



main(sys.argv)