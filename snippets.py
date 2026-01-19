dog = {
"name":"Manny",
"age":5,
"breed":"pug",
"color":"fawn",
"favoriteFoods": ["bacon"],
}

print(dog["age"])
print(dog["breed"])
print(dog["favoriteFoods"])

dog["age"] +=1
dog["breed"] = dog["breed"].upper()
dog["favoriteFoods"].append("sausage")

print(dog["age"])
print(dog["breed"])
print(dog["favoriteFoods"])

for key in dog:
    print(key,"is", dog[key])

