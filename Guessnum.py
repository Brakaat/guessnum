import random
random_number = random.randint(1,20)
user_number = int(input('choose the number:\n'))
while True:
    if random_number == user_number:
        print('You are right, the number is : ',random_number)
        break
    elif random_number >= user_number:
        print('You are wrong, the number is bigger, try again')
        user_number = int(input('choose the number:\n'))
    else:
        print('You are wrong, the number is smaller, try again')
        user_number = int(input('choose the number:\n'))

