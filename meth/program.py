import random 

b= random.randint(0,100)
c=random.randint(0,100)

a= random.choise (["+", "-", "/", "*",])

print(f"kolik je {b} {a} {c}")

d=int(input())
 
if d == b+c:   
    print("máš pravdu ")


else:
    print("jseš kokot")