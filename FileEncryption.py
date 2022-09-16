infile = open('info_security.txt','r')
outfile = open('encrypted.txt','w')

encryption = {'A':'3','a':'#','B':'1','b':'>','C':')','c':'(','D':'[','d':']','E':'@','e':'!','F':'-','f':'+','G':'{',
            'g':'0','H':'9','h':'5','G':'<','g':';','H':'}','h':':','I':'"','i':'|','J':'?','j':'/','K':'8','k':'4',
            'L':'%','l':'_','M':'3','m':'2','N':'6','n':'7','O':'&','o':'*','P':'^','p':'=','Q':',','q':'a','R':'`',
            'r':'~','S':'f','s':'e','T':'v','t':'p','U':'c','u':'b','V':'w','v':'.','W':'d','w':'O','X':'i','x':'q',
            'Y':'z','y':'A','Z':'u','z':'e',' ':' ','.':'.',':':':'}

text = infile.read()

for ch in text:
    code = encryption[ch]
    outfile.write(code)