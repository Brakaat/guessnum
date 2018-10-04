import random
while True:
    start = int(input('please select the Minimun\n'))
    end = int(input('please select the Maximum\n'))
    if start >= end:
        print('your Maximun is smaller than Minimum, please try again!!')
        continue
    else:
        print('The random will between', start,'and', end)
        random_number = random.randint(start,end)
        count = 0
        while True:
            user_number = int(input('choose the number:\n'))
            count += 1
            if random_number == user_number:
                print('You are right, the number is :', random_number)
                print('You have tried', count, 'times.')
                break
            elif random_number >= user_number:
                print('You are wrong, the number is bigger, try again')
            else:
                print('You are wrong, the number is smaller, try again')
            print('This is', count, 'times.')
    break

