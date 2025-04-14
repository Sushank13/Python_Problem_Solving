#assumptions: no duplicates in list, only one pair that is equal to target
# input: [3,2,4,7], 10 
# output: return indices of two numbers that add up to the target (0,3)
# nested loop -> for each number check the sum with other number 
# if sum= target sum -> return index of those numbers
def two_sum(input_list,sum):
    for i in input_list:
        for j in input_list:
            if i+j==sum:
                return (input_list.index(i),input_list.index(j))
print(two_sum([2, 7, 11, 15],9)) # (0, 1)
print(two_sum([-1, -2, -3, -4, -5],-8)) # (2,4)