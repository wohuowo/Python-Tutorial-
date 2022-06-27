#function is a reusable block of programming statements designed to perform a certain task
#def keyword represents functions
def new_func():
    print("hello!!")

new_func()
#attributes are infos we pass to the function
def new(x):
    return x*2
print(new(3))
#x is the attribute and 3 is the parameter
def get_input(user_input):
    user_input = input("what is your name \n")
    print(user_input)

get_input("hello")    

def your_name():
    name = input("what is your middle name?")
    print(name)

for i in range(3):
    your_name()
    


def  user_info(age,  name, country):
    print("This is the age of the use", age, "This is the name of the user", name, "this is also the country of the user", country)

user_info(7, "Tony", "France")
user_info(70, "Belarus", "Z")
def userz_info(country = "Nigeria"):
    print(country);
userz_info("namibia")
    #arbitary arguments are defined with the *args
#the keyword arguement are key = value **kwargs can
#we make use of them when we dont have a specific amount of attributes for our function
#kwargs is for dictionaries
def users_info(*args):
    print(args)
users_info("woahhh", 3) 
users_info("hello",  2)
def user_infoz(**kwargs):
    print(kwargs)

user_infoz( h = "happy", s = "sad", c = "cry")

def use_info(*args):
    for i in args:
        print(i)
use_info("hello","myname","is",12, 3.3, 3,)

def use_infoo(**kwargs):
    for i in kwargs:
        print(i)
use_infoo(h = "hope", f = "faith", c = "choice", d = "dare")     #prints out the keys


#writing a function to get user input
def userinfo():
    name = input("users name")
    age = input("users age")
    print(name,age)

userinfo()    
#simple calculator
def greater(firstno, secondno):
    if firstno > secondno:
        return True
    else:
        return False
print(greater(8, 2))
    


