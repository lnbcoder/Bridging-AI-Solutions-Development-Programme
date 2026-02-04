# Goal: Use append mode a
# 1.Open notes.txt in append mode
# 2.Add 2 new lines
# 3.Close the file
# 4.Reopen in read mode
# 5.Print the updated file using read()
# ⚠️ Make sure your appended text starts on a new line.

file = open("Text_Files/notes.txt","a")
file.write("So far I have covered alot of topics.\n")
file.write("I'm really enjoy learning python.\n")
file.close()

file_r = open("Text_Files/notes.txt","r")
read_file = file_r.read()
print(read_file)


