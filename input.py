with open("input.txt","r") as f:
    s=a.readline()
    e=0
    f=0
    g=0
    h =0
    for x in s:
    if ord(x) in range(65,91):
    e+=1
with open("litereA.txt","w") as f:
    a.write(str(e))
    for x in s:
    if ord(x) in range(97,123):
     f+=1
with open("litereB.txt","w") as f:
    a.write(str(f))
    for x in s:
    if ord(x) in range(49,58):
     g+=1
with open("cifre.txt","w")as f:
    a.write(str(g))
    for x in s:
    if ord(x) in range(33,42):
        h+=1
with open("caractere.txt","w")as f:
    a.write(str(h))
     
        
    
         
    
    