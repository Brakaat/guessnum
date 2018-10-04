import random
a = int(input('please select the Minimun'))
b = int(input('please select the Maximum'))
print('The random will between ', a,' and', b)
random_number = random.randint(a,b)
count = 0
while True:
    user_number = int(input('choose the number:\n'))
    count += 1
    if random_number == user_number:
        print('You are right, the number is : ',random_number)
        print('You have tried ', count, ' times.')
        break
    elif random_number >= user_number:
        print('You are wrong, the number is bigger, try again')
    else:
        print('You are wrong, the number is smaller, try again')
    print('This is ', count, 'times.')

