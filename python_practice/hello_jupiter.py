import sys
import random

#GameStart

#init
sys.stdout.buffer.write(b'Challenge count is ... \n')
sys.stdout.flush()
count = int(sys.stdin.buffer.readline().decode('utf-8').strip())

while count > 0 :
    #user input
    sys.stdout.buffer.write(b'Please input here min number\n')
    sys.stdout.flush()
    min : int = int(sys.stdin.buffer.readline().decode('utf-8').strip())
    sys.stdout.buffer.write(b'is max?\n')
    sys.stdout.flush()
    max : int = int(sys.stdin.buffer.readline().decode('utf-8').strip())
    result = random.randint(min,max)

    sys.stdout.buffer.write(b'is Target Number\n')
    sys.stdout.flush()
    target :int = int(sys.stdin.buffer.readline().decode('utf-8').strip())

    #result
    if(min >= max) :print('入力が間違っています')
    else :
        print('Random int is {}. Select Number is {}.'.format(result,target))
        if result == target :
            print('Correct!!\n')
        else:
            print('ドンマイ！\n')

    #one more
    count -= 1

print('Thank you for playing!!\n')
