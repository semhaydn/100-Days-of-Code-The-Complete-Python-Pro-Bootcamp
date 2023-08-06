fruits = [] 

fruit = None

while True:
    try:
        fruit= input('Which fruit you would like to have ?').lower()
        fruits.append(fruit)
    
    except ValueError:
        print('Enter a correct name')
    
    if fruit == 'none':
        break


for fruit in fruits:
    print(fruit)