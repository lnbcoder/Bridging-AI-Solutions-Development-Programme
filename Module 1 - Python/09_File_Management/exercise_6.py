# Goal: Understand file pointer movement
# 1.Open notes.txt using with
# 2.Call readline() three times
# 3.Print each result
# 4.Then call read()
# 5.Print what read() returns

# 🧠 Question:
# - Why doesn’t read() print the full file?

with open("Text_Files/notes_2.txt", "r") as file:
    readline_file = file.readline()
    print(readline_file)
    print(readline_file)
    print(readline_file)

    read_file = file.read()
    print(read_file)
