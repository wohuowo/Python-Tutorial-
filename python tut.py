
stuff = [ 'aa', 'bb', 'cc' ]
for items in stuff:
    print(items)
    
obj = { "aa": 1, "bb": 2, "cc": 3, "dd": 4 }
print(type(obj))
print(dir(obj))
value= "first string"
print(dir(value))
help(value.upper)
print(type(stuff))

input("what is your name: ")
#guessing game
target_no = 10 #stored number
user_guess = int(input("what is your number: ")) #user input

if (target_no == user_guess):
    print("you win! the number is " + str(user_guess))
elif (target_no > user_guess):
    print("your guess is too low")
elif (target_no < user_guess):
    print("your guess is too high")
    
#number checker

user_no = input("Enter a number: ")

try:
    user_no = int(user_no)
    print("success")
    if(user_no >= 0):
        print("Number is positive")
    elif (user_no < 0):
        print("false")

except:
    print("This aint no number")
    
 
