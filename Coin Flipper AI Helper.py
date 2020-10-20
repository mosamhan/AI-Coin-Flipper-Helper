from random import randint
from time import sleep

print("Hello I am your personal coin flipper!")

heads = 0
tails = 0 
 
flip_coin = int(input("How many coins do you want me to flip? : "))

for i in range(flip_coin):
    result = randint(0, 1)
    sleep(1)
    #print(result)
    if result == 0:
        print("Heads")
        heads += 1
    else:
        print("Tails")
        tails += 1

print("The Results are:")
print("Heads:", heads)
print("Tails:", tails)

percentage = input("Do you want the percentage?: ")
heads_list = [heads]
tails_list = [tails]
tails_quotients = []
heads_quotients = []
total = heads + tails

for number in heads_list:
    heads_quotients.append(heads / total)
for number in tails_list:
    tails_quotients.append(tails / total) 

print("Heads Percentage:", heads_quotients)
print("Tails Percentage:", tails_quotients)

