import sys
print("produce a number")
n=int(input())
print("what would you like the limit to be")
limit=200

for i in range (1,n+1):
    
    x=(i**2)
    y=i
    
    if  limit>x :
     
        print ((y),(","),(x))
else:
  sys.exit("this is as many as i can find up to the limits provided") 


    
