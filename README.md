# Shift Cipher

This program breaks a given (shift) ciphertext by using a bruteforce attack and comparing words with a given dictionary. It supports spurious keys (i.e. two or more keys that lead to the same ciphertext for two or more different plaintexts).

## Usage

Must have python interpreter installed.

From a terminal:

`python shift_cipher.py path_to_ciphertext path_to_dictionary path_to_resulting_plaintext`

The output is a list of tuples. Each tuple contains the corresponding plaintext and the related key.

For example the following list is returned for the ciphertext `bsfob`: `[('river', '16'), ('arena', '25')]`

__Note__: since every attempt is matched against a big dictionary (the given one contains ~300000 words) the execution might takes some time.