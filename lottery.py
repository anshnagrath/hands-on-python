import random
# generate random numbers for lottery;
def generate_random_number():
    numbers = set()
    while len(numbers) < 6:
        numbers.add(random.randint(0,20))
    return numbers
#get user input
def user_input():
    uservalues = input("Enter comma seperated value")
    userlist = uservalues.split(',')

    return {int(uservalues) for uservalues in userlist}  
 #finding intersection   
def finding_result(user_input,lotterynumbers):
    commonnumbers=lotterynumbers.intersection(user_input)
    print("you won ${}".format(100**len(commonnumbers)))
    
def startGame():
      userinput = user_input()
      lotterynumbers = generate_random_number()
      results = finding_result(userinput,lotterynumbers)
startGame()