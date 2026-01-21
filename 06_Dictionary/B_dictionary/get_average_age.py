# Write a function `get_average_age` that accepts a **list of dictionaries**.
# Each dictionary represents a person and contains an `age` key.
# The function should return the **average age** of all people.

def get_average_age(people_list):
    average_age =  0
    sum_age = 0
    num_of_people = len(people_list)
    for dict in people_list:
        sum_age += dict["age"]
    average_age = sum_age / num_of_people
    return round(average_age, 2)

peeps = [
    {"name":"Lovelace","age":36,"born":"London, UK" },
    {"name":"Kleene","age":85,"born":"Connecticut, US" },
    {"name":"Turing","age":41,"born":"London, UK" },
    {"name":"Hopper","age":85,"born":"New York, US" },
]

print(get_average_age(peeps))
# 61.75


people = [
    {"name":"Orwell","age":46,"born":"Bihar, India" },
    {"name":"Bradbury","age":91,"born":"California, US" },
    {"name":"Huxley","age":69,"born":"California, US" },
]

print(get_average_age(people))
# 68.67
