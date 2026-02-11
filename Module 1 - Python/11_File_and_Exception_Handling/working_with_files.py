# Task
#
# 1.Use try to:
#  - Open a file called config.txt in read mode
#  - Read its contents
#  - Convert the contents to an integer
#  - Print the number multiplied by 2
#
# 2.Handle these errors:
#  - FileNotFoundError → if the file doesn’t exist
#  - ValueError → if the file content is not a valid number
#
# 3.Use finally to:
#  - Close the file
#  - Print "File operation completed."

file = None

try:
    file = open("config.txt", "r")
    content = file.read()
    number = int(content)
    print(f"{number} multiplied by 2 is {number * 2}")

except FileNotFoundError:
    print("File does not exist.")

except ValueError:
    print("Content is not a valid number")

finally:
    if file:
        file.close()
    print("File operation completed.")