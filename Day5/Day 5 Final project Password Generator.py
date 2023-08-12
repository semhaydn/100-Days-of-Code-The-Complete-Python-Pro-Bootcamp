import random

# Character sets
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def main():
    print("Welcome to the PyPassword Generator!")

    # Get user inputs for password composition
    nr_letters = get_user_input("How many letters would you like in your password? (Default: 12): ", default=12, min_value=1)
    nr_symbols = get_user_input("How many symbols would you like? (Default: 4): ", default=4, min_value=0)
    nr_numbers = get_user_input("How many numbers would you like? (Default: 4): ", default=4, min_value=0)

    # Generate password components
    my_letters = [select_letters() for _ in range(nr_letters)]
    my_numbers = [select_numbers() for _ in range(nr_numbers)]
    my_symbols = [select_symbols() for _ in range(nr_symbols)]

    # Create the password by shuffling components
    password_list = create_password(my_symbols, my_letters, my_numbers)
    password = ''.join(password_list)
    
    # Evaluate password strength and display results
    password_strength = evaluate_password_strength(password)
    
    print("Generated Password:", password)
    print("Password Strength:", password_strength)

def get_user_input(prompt, default=None, min_value=None):
    while True:
        user_input = input(prompt)
        if user_input == "":
            return default
        try:
            input_value = int(user_input)
            if min_value is not None and input_value < min_value:
                print(f"Please enter a value greater than or equal to {min_value}.")
            else:
                return input_value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def create_password(list1, list2, list3):
    combined_list = list1 + list2 + list3
    random.shuffle(combined_list)
    return combined_list

def select_letters():
    random_letter = random.choice(letters)
    return random_letter

def select_numbers():
    random_number = random.choice(numbers)
    return random_number

def select_symbols():
    random_symbol = random.choice(symbols)
    return random_symbol

def evaluate_password_strength(password):
    score = 0
    length = len(password)
    
    if any(char.isdigit() for char in password):
        score += 1
    
    if any(char.islower() for char in password):
        score += 1
    
    if any(char.isupper() for char in password):
        score += 1
    
    if any(char in symbols for char in password):
        score += 1
    
    if length >= 12:
        score += 1
    
    if length >= 16:
        score += 1
    
    if length >= 20:
        score += 1
    
    if length >= 24:
        score += 1
    
    if score <= 3:
        return "Weak"
    elif score <= 6:
        return "Moderate"
    else:
        return "Strong"

# Call main to start this program.
if __name__ == "__main__":
    main()
