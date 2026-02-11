def find_char_positions(word, char):

    for i in range(len(word)):
        if char in word[i]:
           print(i)
        

find_char_positions("banana", "a")
# 1
# 3
# 5

