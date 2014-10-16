"""
Simple implementation of a shift cipher breaker (supports spurious keys, uses dictionary).
"""

import sys
import time
import ast

def find_spurious_keys(n, dictionary, output_file):
	""" Find (if any) at most n spurious keys using the given dictionary """
	cache_file = "cache.dat"
	cache = None
	cache_available = False
	min_length = 5
	shifts = {}
	try:
		shifts = ast.literal_eval("".join(open(cache_file, "r").readlines()).lower())
		cache_available = True
	except Exception as e:
		print "Cache not available (%s), rebuilding index of shifts" % e
		cache = open(cache_file, "w")
	if not cache_available:
		for w in dictionary:
			if len(w) >= min_length:
				try: # if exists
					shifts[w]
				except Exception: # else
					shifts[w] = []
				for k in xrange(0, 26):
					shifts[w].append(shift(w, k))
		cache.write(str(shifts))
	else:
		print len(shifts)
		for plain1, shifts1 in shifts.iteritems():
			for index1, scrambled1 in enumerate(shifts1):
				for plain2, shifts2 in shifts.iteritems():
					if len(plain1) != len(plain2) or plain1 == plain2:
						continue
					for index2, scrambled2 in enumerate(shifts2):
						if (scrambled1 == scrambled2):
							print "Spurious key found! " + str((plain1, index1, scrambled1, plain2, index2, scrambled2))





		# print "Focusing on " + w
		# if
		# for k in xrange(0, 26):
		# 	shifted_w = shift(w, k)
		# 	shifts[w].
		# 	for subk in xrange(0, 26):
		# 		for subw in dictionary:
		# 			# To return the same ciphertext they must have the same length, skip words already found
		# 			if len(subw) == len(w) and subw != w:
		# 				try:
		# 					found_subw.index(subw)
		# 				except Exception:
		# 					shifted_subw = shift(subw, subk)
		# 					# print "Using %s (%d) -> %s , %s (%d) -> %s\n" % (w, k, shifted_w, subw, subk, shifted_subw)
		# 					if shifted_subw == shifted_w:
		# 						found_subw.append(subw)
		# 						tupl = (w, shifted_w, k, subw, shifted_subw, subk)
		# 						spurious.append(tupl)
		# 						output_file.write(str(tupl))
		# 						print str(tupl)
		# 						if len(spurious) >= n:
		# 							return spurious
		
	# return spurious


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
		cur_word = shift(ciphertext, -k)
		# print "Testing " + ciphertext + " -> " + cur_word + " with key " + str(-k)
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
		dictionary[i] = dictionary[i].strip().lower().replace("'", "")
	if operation == "break":
		if len(args) < 5:
			print_usage_break(args[0])
			exit()
		ciphertext_file = args[4]
		ciphertext = "".join(open(ciphertext_file, "r").readlines()).strip()
		plaintexts = break_ciphertext(ciphertext, dictionary)
		output_file_obj.write(str(plaintexts))
	if operation == "spurious":
		if len(args) < 3:
			print_usage_findspurious(args[0])
			exit()
		spurious_keys = find_spurious_keys(100, dictionary, output_file_obj)
		
	output_file_obj.close()	



main(sys.argv)