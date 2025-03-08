def miniMaxSum(arr):
    list_of_sums=[] 
    for (index,item) in enumerate(arr):
        arr.remove(item) # removing the 1 of the 5 integer from the list
        total=sum(arr) # sum of 4 out of 5 integers
        list_of_sums.append(total) # appending the sum in a sperate list of sums
        arr.insert(index,item) # adding the removed item again at its correct index as changes in a Python List are in-place
        
    list_of_sums.sort()
    min=list_of_sums[0]
    max=list_of_sums[-1]
    print(str(min)+" "+str(max))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)