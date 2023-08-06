# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

both_names = name1 + name2
both_names = both_names.lower()

t = both_names.count('t')
r = both_names.count('r')
u = both_names.count('u')
e = both_names.count('e')

l = both_names.count('l')
o = both_names.count('o')
v = both_names.count('v')

first_total = t+r+u+e

second_total = l+o+v+e

first_total= str(first_total)
second_total = str(second_total)

love_score = (first_total+second_total)

love_score = int(love_score)


if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")

elif love_score <50 and love_score > 40:
    print(f"Your score is {love_score}, you are alright together.")

else:
    print(f"Your score is {love_score}.")

