person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]     #value is a list
person["pets"] = {"dog": "Fido", "cat": "Sox"}      #value is a dictionary

print(person)

print(type(person['children']))

print(person['children'][1])        #name of child

print(person['pets']['cat'])        #name of cat

for child in person['children']:
    print(child)

for pet in person['pets']:          #pet becomes the key of the dictionary
    print(person['pets'][pet])