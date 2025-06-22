# player inputs 5 different numbers from 1 to 36 які не повторюються

number_one = int(input(' Choose five different numbers from 1 to 36. Number one  '))
number_two = int(input(' number two '))
number_three = int(input('number three ' ))
number_four = int(input('number four '))
number_five = int(input('number five '))
my_chance = {number_one, number_two, number_three, number_four, number_five}

print (my_chance)

import random
lottery_draw = random.sample(range(1, 36), 5)

# lottery_draw.sort()
lottery_results = set(lottery_draw)
print(lottery_results)


Lucky_numbers = my_chance.intersection(lottery_results)
print (Lucky_numbers)
prize_chamce = len(Lucky_numbers)
if prize_chamce <= 3:
    print ("sorry")
elif prize_chamce == 4:
    print ("small prize")
else:
    print ("Jackpot")