# Exercise 2 — Sequential File Analyzer
# Concept: blocking I/O
#
# Scenario
# You need to analyze log files one by one.
#
# Requirements
# 1. Create at least 2 text files
# 2. Write multiple lines into each
# 3. Create a function count_words(filename)
# 4. Return total number of words in the file
# 5. Process files sequentially
# 6. Print each file’s word count and the total
import time

def count_words(filename):
    with open(filename,"r") as file:
        print("Opening file...")
        content = len(file.read().split())
        print("Counting Words in file...")
        time.sleep(3)
        print(f"Number of words in file ({filename}): {content}")
        print("Closing file...\n")


count_words("Text_Files/intro.txt")
count_words("Text_Files/about.txt")