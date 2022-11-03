#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Day-24/222 Mail-Merge-Project-Start/Mail Merge Project Start/Input/Letters/starting_letter.txt","r+") as file:
    fh =file.read()
    with open("Day-24/222 Mail-Merge-Project-Start/Mail Merge Project Start/Input/Names/invited_names.txt",'r') as new_file:
        xxx =new_file.readlines()
        for i in xxx:
            x=fh.replace("[name]",i)
            
