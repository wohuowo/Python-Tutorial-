c = [1, 2, 3]
d = c
print(d is c)
d[0] = 499
print(c)
noTwo = "Two"
noTwo[0:2] #zero is the index that is needed and 2 is the element i dont need in the string
print(noTwo[0:2])
print(noTwo[0:1])
print("wohu" * 7)# can multiply by string and integer, list and integer but not str & str , list & list
#loops and branches
#if checks if condition is true
if 10 < 29:
    print("10 is less tthan 20")

if 5 == 20:
    print("5 is equal to 20")

#elif --> else if executes only one logic

if "a" == "b":
    print("a is the same as b")
elif "a" != "b":
    print("a is not equal to b")
elif 100 < 200:
    print("100 is less than 200")
#else branches catches every condition , also doesnt accept    

our_flag = 500 == 1000

if our_flag:
    print("500 is not equal to 1000")
elif False:
    print("80 is greater than 90")
elif True:
    print("Running true block")
else:
    print("500 is equal to 1000")


#while loops
its_nighttime = True
hour_of_the_day = 0
while its_nighttime:
    print("The Hour of the day is " ,hour_of_the_day)
    if hour_of_the_day == 10:
        print("Waking up!!")
        break
    
    #keep sleeping
    hour_of_the_day = hour_of_the_day + 1
     
    print(hour_of_the_day)
    pass
#pass makes the interpreter ignore the empty code block
#wake up and start your day
#Word count program
user_sentence =user_sentence = input("Enter sentence: ")
user_sentence = user_sentence.split(" ")
no_of_words = len(user_sentence)
print(no_of_words)
#simple calc ctrl + c ends any python program
print("Welcome to Simple CLI Calculator")
is_running = True
while is_running:
    print("starting calculator process")
    user_operation = input("What operation would you like to perform?\nPick your choice ['+', '-', '*', '/'] : ")
    try:
        no1 = int(input("first number: "))
        no2 = int(input("second number: "))
    except:
        print("Failed not a number")
        continue

    if user_operation == "+":
        print(no1 + no2)
    elif user_operation == "-":
        print(no1 - no2)
    elif user_operation == "/":
        print(no1 / no2)
    elif user_operation == "*":
        print(no1 * no2)
    else:
        print("invalid operation entered Try again")
        
    choice = input("Would you like to run another operation. [y,n] ")
    if choice == "y":
        pass
    if choice == "n":
        is_running = False
print("Thanks for using the calculator")        

    

    
