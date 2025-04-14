# WAP to reverse a list without using reverse indexing or reverse()
# [b,a,c]->[c,a,b]
# iterate the list, insert the items at index 0 in a new list
def reverse_list(input_list):
    output=[]
    for item in input_list:
        output.insert(0,item)
    return output
print(reverse_list(["b","a","c"]))
print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list([1, "a", True, 3.14]))