# WAP to find the pairs in a list for a given sum
# input: [4,3,6,7], 10
#output: (4,6) and (3,7) but not (6,4) and (7,3) as thats repition
# nested loop 
# for each number, calculate sum and compare with target sum
# if it is equal,add the pair in a set
def get_sum_pairs(input_list,sum):
    output=set()
    for i in input_list:
        for j in input_list:
            if i+j==sum:
                if i>j:
                    output.add((j,i))
                else:
                    output.add((i,j))
    return output

print(get_sum_pairs([4,3,6,7],10))
print(get_sum_pairs([1, 2, 3, 2, 4], 5))
print(get_sum_pairs([5, 1, 5], 10))
print(get_sum_pairs([1, 2, 3], 100))