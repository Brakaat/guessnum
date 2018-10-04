import random
random_number = random.randint(1,20)

while True:
    user_number = int(input('choose the number:\n'))
    if random_number == user_number:
        print('You are right, the number is : ',random_number)
        break
    elif random_number >= user_number:
        print('You are wrong, the number is bigger, try again')
    else:
        print('You are wrong, the number is smaller, try again')

