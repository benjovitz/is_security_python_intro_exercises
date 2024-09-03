#!/usr/bin/python

file = open("myFile.txt", "r")
search_word = input("enter search word: ")
i = 0

for line in file:
    i += 1
    if search_word in line:
        print(f"line {i}: {line}")
