# Goal: Master readline()
# 1.Open notes.txt
# 2.Read lines one by one using readline()
# 3.Stop when an empty string is returned
# 4.Print each line
# 💡 This mimics how files are read internally.

file = open("Text_Files/notes.txt","r")

while True:
    read_line = file.readline()
    if read_line == "":
        break
    print(read_line.strip())

file.close()

