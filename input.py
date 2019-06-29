age = input("Please Enter your age:")
if type(age) == int:
 print(("You have lived for {} secounds.This corresponds to {} years").format(int(age)*365*24*60*60,age))
else:
   print("Please enter a valid integer")    
numbers = [1,2,3,4,5,6] 
print(len(numbers))
print(numbers[len(numbers)-1])  
numbers.append(234)
numbers.remove(2)
ext = [1,34,54]
numbers.extend(ext)
print(numbers)
for number in numbers:
    print(number)


user_Num = 2
magic_Number = [1,2,3,4]
if user_Num in magic_Number:
    print("You got it right")
else:
    print("You falied here")    
