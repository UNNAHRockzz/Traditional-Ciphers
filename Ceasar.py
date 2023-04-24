def ciesar(string):
    l=[]
    l2=[]
    str=""
    l[:0]=string
    for i in l:
        if(i==" "):
            l2.append(chr(32))
        else:
            l2.append(chr(ord(i)-3))
    return (str.join(l2))

c=input("Enter the text to be encrypted :- ")
print("Encrypted Text is ")
print(ciesar(c))

