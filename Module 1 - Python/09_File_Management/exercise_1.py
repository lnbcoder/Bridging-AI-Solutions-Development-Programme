# Goal: Practice w + read()
#
# 1. Create a file called notes.txt
# 2. Write 3 lines of text into it
# 3. Close the file
# 4. Reopen the file in read mode
# 5. Print the entire content using read()
#
# Rules
# - Do NOT use with
# - You must call close()

file = open("Text_Files/notes.txt", "w")
file.write("Hello There!\n")
file.write("My name is Loveness.\n")
file.write("I am learning Python Programming.\n")
file.close()

file = open("Text_Files/notes.txt", "r")
read_file = file.read()
print(read_file)
file.close()