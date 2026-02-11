# Write a function `element_quantities` that accepts a dictionary where:
# - keys are elements
# - values are quantities
# Return a list containing each element repeated according to its quantity.

def element_quantities(quantities):
    quantity_list = []
    for element, quantity in quantities.items():
        quantity_list.extend([element] * quantity)
    return quantity_list

quantities1 = {"cat":3,"bird":1,"dog":2 }
print(element_quantities(quantities1))
# ['cat', 'cat', 'cat', 'bird', 'dog', 'dog']

quantities2 = {"blue":3,"brown":1 }
print(element_quantities(quantities2))
# ['blue', 'blue', 'blue', 'brown']

