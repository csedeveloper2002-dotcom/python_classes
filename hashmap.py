my_map = {
    "name": "Alice",
    "age": 20,
    "city": "New York"
}

print(my_map["name"])

my_map["country"] = "USA"
my_map["age"] = 21
del my_map["city"]

for key, value in my_map.items():
    print(key, ":", value)
