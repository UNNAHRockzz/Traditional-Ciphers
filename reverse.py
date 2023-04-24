def reverse(string):
    l=[]
    l2=[]
    str=""
    l[:0]=string
    for i in l[::-1]:
        if(i==" "):
            l2.append(chr(32))
        else:
            l2.append(i)
    return (str.join(l2))

c=input("Enter the text to be encrypted :- ")
print("Encrypted Text is ")
print(reverse(c))