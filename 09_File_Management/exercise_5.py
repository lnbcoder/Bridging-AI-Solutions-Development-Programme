# Goal: Replace manual close() with with
# 1.Open notes.txt in write mode using with
# 2.Write 5 lines
# 3.Do NOT call close()
# 4.Open the file again using with
# 5.Print the entire content

# Think
# - Why don’t we need close() here?

with open("Text_Files/notes_2.txt","w") as file:
    file.write("line 1\n")
    file.write("line 2\n")
    file.write("line 3\n")
    file.write("line 4\n")
    file.write("line 5\n")

with open("Text_Files/notes_2.txt", "r") as file:
    print(file.read())