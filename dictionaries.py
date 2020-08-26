customer = {
    "name": "Sanusi Ibrahim",
    "age": 22,
    "is_verified": True
}

#We can access each item in the "dictionary" using square brackets
print(customer["name"])
print(customer["age"])
print(customer["is_verified"])

#Using the "get" method. Note: 1, Babarinde street is the default value
print(customer.get("address", "1, Babarinde street")) #None is an object that represents the absence of a value

customer["name"] = "Adeniran Rahmadan" #To update a name
print(customer["name"])
customer["favourite color"] = "white" #You can also add new key-value pairs
print(customer["favourite color"])

#Exercise
phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
     output += digits_mapping.get(ch, "!") + " "
print(output)