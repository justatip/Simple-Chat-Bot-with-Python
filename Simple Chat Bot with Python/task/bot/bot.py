def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    # write your code here
    print("what's language you are learning", end='?\n')
    print("1. Cobra\n2. Python\n3. Giga\n4. Niga")
    answer = int(input())
    sad_message = "Please, try again."
    '''if answer == 2:
        print("Ok! Who's a bad boy", end='?\n')
        print("1. No bad boys\n2. i'am\n3. not me\n4. Trump")
        answer = int(input())
        if answer == 4:
            return
        else:
            print(sad_message)
            test()
    else:
        test()
        print(sad_message)'''
    print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


greet('Aid', '2020')  # change it as you need
remind_name()
guess_age()
count()
test()
end()
