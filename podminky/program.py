import random


while True:
    print("1 = hrát, 2 = vypnout")
    a = int(input())

    if a == 2:
        print("bye bye")
        break

    if a == 1:
        pc = random.randint(1,6)
        print("pc hodil", pc)
        print("stiskni enter, abys hodil kostkou")
        input()
        you = random.randint(1,6)
        print("ty jsi hodil",you)

        if pc > you:
            print("prohrál jsi")

        if pc < you:
            print("vyhrál jsi")

