n= int(input("how many bottles would you like on the wall"))# takes the input from the user and stores it as an integer for later recall 
while n>0: #loops until all the bottles fall off 
    print ((n),"green bottles Hanging on the wall Ten green bottles Hanging on the wall And if one green bottle Should accidentally fall There'll be"
           ,(n-1),"green bottles Hanging on the wall")
    # the print function displays the songs with the inbuilt math which allows for the numbers of bottles to change 
    n=n-1 # this math equation minus' one bottle 
