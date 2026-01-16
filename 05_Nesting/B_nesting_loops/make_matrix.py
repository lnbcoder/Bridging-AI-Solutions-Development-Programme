# Write a function `make_matrix(m, n, value)` that returns a 2D list of m rows and n columns
# filled with `value`.

def make_matrix(m, n, value):
    twoD_list = []

    for i in range(m):
        list = []
        for j in range(n):
          list.append(value)  # adds value in column
        twoD_list.append(list) # adds the list (column) to row
        
    return twoD_list

print(make_matrix(3, 5, None))
print(make_matrix(4, 2, "x"))
print(make_matrix(2, 2, 0))

'''
 Example [
 [None, None, None, None, None],
 [None, None, None, None, None],
 [None, None, None, None, None]
 ]
 '''

