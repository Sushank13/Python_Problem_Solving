# WAP to remove duplicates from a list preserving the order.
#[b,c,c,a,c,b,a]->[b,c,a]
# iterate the list-> add elements in a list after checking if element does not exist in set
def remove_duplicates(input_list):
    tracker=set() # using set() as time complexity of lookups is O(1)
    output=[] # need list as order is to be preserved
    for item in input_list:
        if item not in tracker:
            tracker.add(item)
            output.append(item)
    return output 
print(remove_duplicates(["1", 1, "1", 2, 2, "2"]))
print(remove_duplicates(["A", "a", "A", "a"]))
print(remove_duplicates([1, 2, 2, 3, 1, 4]))
print(remove_duplicates(["b", "c", "c", "a", "c", "b", "a"]))
