# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

leap_year = None

if year %4 != 0:
   
   leap_year = False

elif year %100 != 0 :
   
    leap_year = True

elif year %400 == 0:

    leap_year = True

else:
    leap_year = False

while leap_year:
    print('leap_year')

    break

else: print("Not a leap year ")