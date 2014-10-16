# Shift Cipher

This program has two usages:
- Break a ciphertext encrypted with a shift cipher using a dictionary (only lowercase, no space English text)
- Find a given number of spurious keys by scanning a given dictionary

## Usage

Must have python interpreter installed.

From a terminal:

- To break: `shift_cipher.py break path_to_dictionary path_to_resulting_plaintext path_to_ciphertext`
- To find spurious keys: `shift_cipher.py spurious path_to_dictionary path_to_dump_file`

In the first case the resulting plaintext is written to the given path.
In the second case the spurious keys are output on the standard output. Since the execution scans the whole dictionary multiple times it may take a while (depending on which system you are executing it on). To speed things up a cache is built if no valid `cache.dat` file is available (`cache.dat` contains a Python dictionary with all the words from the dictionary and the respective shifts for keys from 0 to 25).