user_data = input("Do you have money? ")

if user_data == "yes"  or  user_data == "Yes":
    print("can you give me money?")
elif user_data == "no":
    print("Okay oo")
else:
    print("never mind")

user_name=input("What is your name?"  )
names =["Francis", "Mary",  "Folake", "Timi"]
if  user_name not  in names:
    print("Name already exists")
else:
    print(f"Welcome {user_name}")

if  user_name is "Frank":
    print("Name already exists")
else:
    print(f"Welcome {user_name}")

print(str("No") is  str("No"))

map = { "Name": "Frank",  "Age": 10}
for i in map.values():
     print(f"Welcome {i}")

for x in range(len(names)):
    print(names[x])
for p in range(1, 30):
    if p== 2:
        print("skipping 2")
        continue #skips
    if  p > 25:
       print("stop at  25")
       break#stop
    if  p %2 == 0:
        print(f"{p} is an even number")
newuser = input("What is your name?")
while newuser not in ( "exit", " Exit" ):
    if  newuser in names:
        print(f"Boss!! pick another name. \n  {newuser} already exist")
        newuser = str(input("Enter your username: "))
        continue
    print(f"Welcome! {newuser} to the program")
    break
x = True
while x:
    print(f"x is {x}")
    x = False
else:
    print(f"x is {x}")
