# Given an array of positive integers sorted in a strictly increasing 
# order, and an integer k. Return the kth missing positive integer missing from this array.
# Ex:[1,3,6,9,10], find 3rd missing postive integer
# 2-> 1st missing, 4->2nd missing, 5->3rd missing, return 5
#Note: the sorting of array does not really matter
# using while loop as I am not certain about the number of iterations
def find_missing(arr,k):
    # assume that 1 is the 1st missing positive integer
    missing=1
    counter=1
    # the above lines imply that 1 is the 1st missing positive integer
    integer_set=set(arr) # converting list to a set for O(1) lookups
    while(True):
        if missing not in integer_set: # found a missing positive integer
            if counter==k: # check if the missing is the kth positive integer
                return missing
            counter=counter+1 # increase counter if counter!=k
        missing=missing+1 # increment value in either case
print(find_missing([2,3,4,7,11],5)) # return 9
print(find_missing([1,2,3,4],2)) # return 6
print(find_missing([1,-3,3,5,-1,10],4)) # return 7             
        