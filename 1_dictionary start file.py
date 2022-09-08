import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}



print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)
print(type(phonebook))

phone = phonebook['Chris']

print(phone)

print(len(phonebook))

mydictionary = dict(m=8, n=9)  ##creating a dictionary

print(mydictionary)

mydict = {}       ##create empty dictionary
print(mydict)

print()
print('*****  end section 1 ********')
print()




print()
print('*****  start section 2 - search dictionary ********')
print()

name = 'Chri'

if name in phonebook:
    print(phonebook[name])
else:
    print(name,'not found')





print()
print('*****  end section 2 ********')
print()




print()
print('*****  start section 3 - edit/append dictionary ********')
print()

print(phonebook)
phonebook['Chris'] = '555-0123'     ##update value for chris
phonebook['Joe'] = '555-4444'       ## add joe to dictionary
print(phonebook)
                                    ## can't update the key... just updating it

print()
print('*****  end section 3 ********')
print()



print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

#del(phonebook['Chris'])
#print(phonebook)


print()
print('*****  end section 4 ********')
print()




print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()

for key in phonebook:       ##automatically iterates through the keys of a dictionary (defualt setting)
    print(key)
    print(phonebook[key])

for value in phonebook.values():        ##iterates through the values with this method
    print(value)

for k,v in phonebook.items():       ##items method allows you to access both key and value at the same time
    print('key:',k,'value: ',v)

for tuple in phonebook.items():     #tuple because of the parenthesis...immutible object
    print(tuple)


print()
print('*****  end section 5 ********')
print()




print()
print('*****  start section 6 - using get and clear ********')
print()

## get method avoids key error... doesnt break the program
phone = phonebook.get("Chris", "key not found")
print(phone)

##clear method clears out the dictionary... not deleting it
#phonebook.clear()
#print(phonebook)


print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()

## pop method allows you to remove key value pair
#remove = phonebook.pop('Chris','key not found')
#print(remove)       #assigns the value to the variable before removing
#print(phonebook)




print()
print('*****  end section 7 ********')
print()




print()
print('*****  start section 8 - using popitem ********')
print()

#picks a random key value pair to remove
##random part does not work.. picks the last element
#a = phonebook.popitem()

#print(a)
#print(phonebook)



print()
print('*****  end section 8 ********')
print()



print()
print('*****  start section 9 - using random and converting to list ********')
print()

list_of_keys = list(phonebook)      ##converting dictionary into a list
print(list_of_keys)     ##converts keys to list
random_key = random.choice(list_of_keys)
print(random_key)
print(phonebook[random_key])

print(phonebook[random.choice(list(phonebook))])    ##same as the above code

print()
print('*****  end section 9 ********')
print()







