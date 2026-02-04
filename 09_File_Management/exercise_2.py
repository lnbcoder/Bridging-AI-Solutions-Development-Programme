# Goal: Use readline()
# 1. Open notes.txt in read mode
# 2. Read only the first line
# 3. Print it
# 4. Close the file
# 💡 Notice what happens if you call readline() again.

file = open("Text_Files/notes.txt","r")
read_file = file.readline()
print(read_file)
file.close()