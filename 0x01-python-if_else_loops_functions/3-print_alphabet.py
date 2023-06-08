#!/usr/bin/python3
# Author - Ezra Akankwasa
for letter in range(97, 123):
    if chr(letter) != 'q' and chr(letter) != 'e':
        print("{}".format(chr(letter)), end="")
