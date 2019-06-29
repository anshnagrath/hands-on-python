import random
magic_nums = [random.randint(0,9),random.randint(0,9)]
chances = 3
for attempt in range(3):                             # range would creat a list ie range(chances) is [0,1,2]
    print("This is your {} attempt".format(attempt+1))
    user_number = int(input("Enter a number between 0 and 9:"))
    if user_number not in magic_nums:
        print("You missed")
    else:
        print("You got it right")    