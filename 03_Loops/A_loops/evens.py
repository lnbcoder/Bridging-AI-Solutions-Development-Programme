# Write a function `evens(max_num)` that prints all positive even numbers LESS than max_num.
def evens(max_num):
    for i in range(1, max_num):
        if i % 2 == 0 :
            print(i)

evens(11)
print("==============")
evens(8)

