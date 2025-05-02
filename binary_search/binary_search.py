# input: [3,10,2,5,39,1] unsorted array, return index of 39 
# output: index of element 
# first sort the list [1,2,3,5,10,39]
# input validation->empty list is provided
# edge case-> element does not exist in the list
def binary_search(input_list,target):
    if not input_list:
        return "Empty Input List"
    input_list.sort() # sort the array
    start=0
    end=len(input_list)-1
    while(start<=end):
        mid =(start+end)//2
        if target<input_list[mid]: # value is in left side
            end=mid-1
        elif target>input_list[mid]: # value is in right side
            start=mid+1
        else: # match found
            return mid
    return -1 # value does not exist 
print(binary_search([],2))
print(binary_search([3,10,2,5,39,1],39)) # output: 5
print(binary_search([3,10,2,5,39,1],10)) # output: 4
print(binary_search([3,10,2,5,39,1],3)) # output: 2
print(binary_search([3,10,2,5,39,1],4)) # output: -1