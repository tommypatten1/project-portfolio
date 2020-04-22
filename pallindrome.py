palindromea = input(str("what word do you think is a palindrome"))

# this section changes all the letters to lowercase 
palindromea = palindromea.lower()

# this section reverses the original string which is inputed by the user
palindrome = reversed(palindromea)

# this section contains an if function to allow or a check between the reversed and the original
if list(palindromea) == list(palindrome):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")
