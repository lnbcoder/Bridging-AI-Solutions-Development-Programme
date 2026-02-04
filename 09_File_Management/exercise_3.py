# Goal: Use readlines()
# 1.Open notes.txt
# 2.Store all lines in a variable
# 3.Print the list
# 4.Print each line one by one (without extra blank lines)
# 5.Close the file
#
# Question to think about
# - What is the data type returned by readlines()?

file = open("Text_Files/notes.txt","r")
read_file = file.readlines()
for line in read_file:
    print(line.strip())
file.close()