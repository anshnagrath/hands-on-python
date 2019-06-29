import random
minimum = 100;
def generateRandomAndAssign():
    global minimum
    random_number = random.randint(0,100)
    print("random number generated is {}".format(random_number))
    if random_number <=  minimum:
         minimum = random_number
for index in range(100):
    generateRandomAndAssign();
print(minimum);      
