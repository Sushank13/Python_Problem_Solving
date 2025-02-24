#n = int(input())
#if n in range(1,21):
    #for i in list(map(lambda n: n**2,range(0,n))): # i have used lambda+map()+for loop instead of simply using a for loop
        #print(i)
        
n = int(input())
if n in range(1,21):
    for i in range(0,n):
        print(i**2)
        