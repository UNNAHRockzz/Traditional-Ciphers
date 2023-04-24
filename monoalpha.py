def monoalphabetic(string):
    l=[]
    l2=[]
    str=""
    l[:0]=string
    for i in l:
        if(i==" "):
            l2.append(chr(32))
        else:
            if(i<='m' or i<='M'):
                l2.append(chr(ord(i)+13))
            else:
                l2.append(chr(ord(i)-13))
    return (str.join(l2))

c=input("Enter the text to be encrypted :- ")
print("Encrypted Text is ")
print(monoalphabetic(c))
