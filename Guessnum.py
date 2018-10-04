import random
random_number = random.randint(1,20)
count = 0
while True:
    user_number = int(input('choose the number:\n'))
    count += 1
    if random_number == user_number:
        print('You are right, the number is : ',random_number)
        print('You have tried ',count,' times.')
        break
    elif random_number >= user_number:
        print('You are wrong, the number is bigger, try again')
    else:
        print('You are wrong, the number is smaller, try again')

