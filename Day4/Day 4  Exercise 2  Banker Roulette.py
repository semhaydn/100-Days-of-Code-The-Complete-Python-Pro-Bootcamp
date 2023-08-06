# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# how_many_person = len(names)
# lucky_number = random.randint(0,how_many_person-1)

print(f'{random.choice(names)} is going to buy the meal today!')


