infile = open('sometext.txt','r')

dict = dict()

text = infile.read()
words = text.split(' ')

print(words)

for word in words:
    if word in list(dict()):
        dict[word] += 1
    else:
        dict[word] = 1

for k,v in dict.items():
    print(k+': ',v)
