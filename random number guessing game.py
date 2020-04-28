import random #allows for the random function to be used 
a=int(input("what is the lowest number you would like it to be"))#stimulates a response from the user to create the lowest number for the range
b=int(input("what is the highest number you would like"))# stimulates a response from the user to create the biggest number for the range
c=random.randint(a,b)# assigns a random integer from the range to the variable c

turns=0 #sets the turn count to 0
x=1 #allows the loops to fuction (using as if an on switch)

while x==1:# allows for the loop to keep functioning until the number is found 
    guess= int(input("what is your guess"))#asks for a guess from the user
    turns=turns+1#adds one guess to the turn count
    if guess== c: # checks the guess against the random integer
        print("you have guessed the number",) #prints a message if the randint matches the guess
        print("turns=",(turns))#tells the user how many turns they have used
        x=0 #terminates the program
    if guess > c:#checks the guess against the randint
        print ("guess is too high") #prints the guess is too high if the loop criteria is met
    if guess<c:#checks the guess against the randint
         print   ("guess is too low")#prints the guess is too low if the loop criteria is met
