def factorial(num):
    if num==0 or num==1: #factorial of 0 and 1 is 1.
        return 1
    product=1
    for i in range(2,num+1):
      product=i*product
    return product
print(factorial(5))
print(factorial(3))
print(factorial(0))
     