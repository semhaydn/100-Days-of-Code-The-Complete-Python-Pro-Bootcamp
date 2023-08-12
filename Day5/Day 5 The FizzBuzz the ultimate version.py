def check_conditions(number):

    condition1 = number %3 ==0
    condition2 = number %5 == 0


    if condition1 and condition2:
        number ="FizzBuzz"
        

    elif condition1 :
        number = "Fizz"

    elif condition2:
        number = "Buzz"
    
    return number


def main(start, end):
    for number in range(start, end + 1):
        print(check_conditions(number))

# Call main to start this program.
if __name__ == "__main__":
    main(1, 100)