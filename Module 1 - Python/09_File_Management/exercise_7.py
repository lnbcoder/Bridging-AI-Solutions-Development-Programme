# Goal: Combine readlines() + logic
# 1.Open notes.txt
# 2.Count how many lines are in the file
# 3.Print: "This file has X lines"

file = open("Text_Files/notes.txt", "r")
read_lines_file = file.readlines()
num_line = len(read_lines_file)
print(f"This file has {num_line} lines")
file.close()