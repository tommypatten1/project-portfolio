y=int(input("what is the number you would like to start from")) # allows the user to input any given whole value
z=int(input("what number would you like next"))#allows the user to input a second value 
c=input("what function would you like") # allows the user to input a function using the common used symbols
if c==("/"): #checks for the symbol inputed
        x= y/z
        
if c==("*"):#checks for the symbol inputted
      x= y*z #does the maths function
 
if c== ("+"):#checks for the symbol inputted
        x=y+z#does the maths function

if c== ("-"):#checks for the symbol inputted
        x=y-z#does the maths function
if c==("^"):#checks for the symbol inputted
    x=y**z#does the maths function
print ((y),(c),(z),("="),(x))# prints the equation you have performed 
n=open("file.txt","w") #opens a file to write to
n.write(str(y)) # writes the value of y to the file 
n.write(str(c))# writes the value of c to the file 
n.write(str(z)) #writes the value of z to the ile 
n.write ("=") # writes = to the file (purley aesthetic)
n.write(str(x)) #writes the value of x to the file 
n.close() #closes and saves the file 

