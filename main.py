#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
import os
names_list = []
def make_new_letters(name):
    with open("./Input/Letters/starting_letter.txt", "r") as letter:
        read_letter = letter.read()
        fixed_letter = read_letter.replace("[name]", name)
        output_dir = "./Output/ReadyToSend/"
        filename = os.path.join(output_dir,f"{name}.txt")
        with open(filename,"w") as new_letter:
            new_letter.write(fixed_letter)

with open("./Input/Names/invited_names.txt") as invite_names:
    for name in invite_names:
        names_list.append(name[:-1])
       
for name in names_list:
    make_new_letters(name)


