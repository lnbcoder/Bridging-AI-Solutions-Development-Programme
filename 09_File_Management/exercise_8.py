# Goal: Append dynamic data
# 1.Ask the user to enter a sentence
# 2.Append that sentence to notes.txt
# 3.Reopen the file
# 4.Print the full content

sentence = input("Enter sentence: ")

with open("Text_Files/notes.txt","a") as append_file:
    append_file.write(sentence + "\n")

with open("Text_Files/notes.txt","r") as file:
    read_file = file.read()
    print(read_file)
