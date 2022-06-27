#file manipulation
#read access mode
#open_file = open("./text.txt",  "r")
with  open("./text.txt", "r") as open_file:
    readtext = open_file.read()#reads files
    print(readtext)
    print("this file is true")
    
#print(open_file)
def readfile(filename):
    with open("./text.txt", "r") as file:
        read_file =  file.read()
        print(read_file)
        print("This file is valid")
    return  read_file 

def countword():
    text = readfile("./text.txt")
    print(text)
    split_text = text.split()# splitsall the words in the file into a list
    #print(split_text)
    count ={}# makes it an empty dictionary
    for i in split_text:
        if i in count:
            count[i] +=1
        else:
            count[i] = 1
    return count
print(countword())    
#write access mode allows you write in a file whilst creating a new file or overwriting what you wrote
#while append allows you write upon an existing file
#new_file = open("zuri.txt", "w")
#w = write r= read a =append
#write_file = "This is file manipulation"
#new_doc = new_file.write(write_file)
#new_file.close()
#read_file = new_file.read()
#print(new_doc)
#append
app_file = open("zuri.txt", "a")
#w = write r= read a =append
write_file = "woahhhhhh"
new_text = app_file.write(write_file)
app_file.close()



def read_file(file_name):
    open_file = open("text.txt", "r")
    read_file = open_file.read()
    print(read_file)

    


