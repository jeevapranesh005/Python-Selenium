def access_name(person):
    try:
        return person["name"]
    except KeyError:
        print("Error: Key not found!")
print(access_name({"name": "Alice", "age": 30}))
access_name({"age": 30})
