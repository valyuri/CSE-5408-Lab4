#Lab4 Part a
#Reverse a user inputted string 

#Code to reverse the string input by user
def reverse(string):
    string = "".join(reversed(string))
    return string

#User inputs word or phrase to reverse 
s = input("Enter word to reverse: ")

#Prints the results
print("Reversed: " , end="")
print(reverse(s))