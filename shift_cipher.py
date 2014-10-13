"""
Simple implementation of a shift cipher breaker (supports spurious keys, uses dictionary).
"""

import sys

def break_ciphertext(ciphertext, dictionary):
	plaintexts = []
	cur_word = ""

	print ciphertext

	for k in xrange(0, 26):
		# Shift with the key
		for i in xrange(0, len(ciphertext)):	
			cur_word += chr((((ord(ciphertext[i]) - 97) + k) % 26) + 97)
		try:
			dictionary.index(cur_word + "\n")
			plaintexts.append(cur_word)
		except Exception:
			pass
		cur_word = ""
	return plaintexts

def print_usage(name):
	print "Usage: " + name + " path_to_ciphertext path_to_dictionary"

def main(args):
	if (len(args) != 3):
		print_usage(args[0])
		exit()
	ciphertext_file = args[1]
	dictionary_file = args[2]
	ciphertext = "".join(open(args[1], "r").readlines())
	dictionary = open(args[2], "r").readlines()
	for l in dictionary:
		l = l.strip()
	# print dictionary
	plaintexts = break_ciphertext(ciphertext, dictionary)
	print plaintexts


main(sys.argv)