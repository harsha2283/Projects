from os import remove, rename, mkdir, makedirs, path

#creating a file 
def creating_file(file_name):
    try: 
        with open(file_name,"a+") as f:
            f.write("/*This file is created using the function creating_file(file_name)*/\n")
        f.close()
    except:
        print("Error: Could not create the file with name"+ file_name +" using the function creating_file(file_name)")
    
#deleting a file 
def deleting_file(path):
    try:
        if os.path.exist(path):
            os.remove(path)
        else:
            print("The file mentioned doesnot exist in the path u mentioned")
    except:
        print("Error: could not delete the file"+ path +"using the function deleting_file(path)")
    
#Renaming the file 
def renaming_the_file(existing_name,New_name):
    try:
        os.rename(existing_name,New_name)
        print(f"The file {existing_name} is renamed as follows {New_name}")
    except:
        print(f"Error: Could not rename the {existing_name} file to {New_name}")


#read the contents of the file 
def read_the_file(file_name):
    try:
        with open(file_name,"r") as f:
            contents = f.read()
            print(contents)
    except:
        print(f"Error: Could not read the file {file_name}")


#function executions starts from here 
read_the_file("new_file.txt")