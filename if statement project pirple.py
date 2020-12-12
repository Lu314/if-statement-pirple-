

#declaring global variables to test function 
num_1 = 1
num_2 = "1"  #string for bonus question
num_3 = 3
#num_1 = 4   < ---- un-comment to get "false" result output, obviously comment out the first num_1 to test!



#defining function that will check for equality amongst the values with the given parameters 
def checksForEqual(num_1,num_2,num_3):
    #bonus string to int comparison
    if int(num_1) == int(num_2) or int(num_2) == int(num_3) or int(num_3) == int(num_1):
        print ("True")
    else:
        print("False")
        return
#calling function
checksForEqual(num_1,num_2,num_3)