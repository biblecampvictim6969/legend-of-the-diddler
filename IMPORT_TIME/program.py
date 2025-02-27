import time 

def count(number):
    for i in range(21):
        print(i)
before=time.time()
result=count(5)
after=time.time()

cas= before-after

print("it delayed:" ,cas)