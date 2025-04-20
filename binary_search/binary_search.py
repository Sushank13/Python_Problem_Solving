# input: [3,10,2,5,39,1], return index of 39 
# output: index of element 
# first sort the list [1,2,3,5,10,39]
# edge case-> element does not exist in the list
def binary_search(input_list,target):
    input_list.sort() # sort list in ascending order
    start,end=0,len(input_list)-1
    while(start<=end):
        middle=(start+end)//2
        if input_list[middle]==target:
            return middle
        elif target>input_list[middle]: # target is on the right side
            start=middle+1
        elif target<input_list[middle]:#target is on the left side
            end=middle-1 
    return -1 # element does not exist
print(binary_search([3,10,2,5,39,1],39)) # output: 5
print(binary_search([3,10,2,5,39,1],10)) # output: 4
print(binary_search([3,10,2,5,39,1],3)) # output: 2
print(binary_search([3,10,2,5,39,1],4)) # output: -1