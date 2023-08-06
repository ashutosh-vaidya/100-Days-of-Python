# Read the existing files

# when we use with then we do not have to worry of closing the file
# By default open() opens the file in read "r" mode 

with open("my_file.txt") as file:
    data = file.read()
    print(data)
    
# Writing to the file
with open("my_file.txt", mode="w") as file:
    file.write("This will overwrite everthing present in the file earlier.")
    
# Writing to the file without overwriting it
with open("my_file.txt", mode="a") as file:
    file.write("\nThis will not overwrite everthing present, the new text will be at the end of file")
    
#Opening a File that doesn't exit in write mode will create it from scratch

with open("file_that_doesnt_exist.txt", mode="w") as file:
    file.write("This file is created from our program")