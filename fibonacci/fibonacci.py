#generate the first n numbers in the Fibonacci sequence
def fibonacci_series(n): #n=4, 0,1,1,2
    first=0
    second=1
    print(first)
    print(second)
    for _ in range(n-2):
        third=first+second
        print(third)
        first,second=second,third
fibonacci_series(4)
        
    