#mistake: I was changing the input array and not the start & end
#in each recursive call. The input array has to be the same while 
# the start and end should change in each recurive call 
def binary_search(input_string,target):
    input_string.sort()
    print(f"input:{input_string}")
    start=0
    end=len(input_string)-1
    print(f"end={end}")
    mid=(start+end)//2
    print(f"mid:{mid}")
    print(f"middle element:{input_string[mid]}")
    if target==input_string[mid]:
        print(f"mid={mid}")
        return mid #halt/base condition
    elif target<input_string[mid]:
        end=mid-1
        print(f"end={end}")
        sub_list=input_string[start:end+1]
        print(f"sublist:{sub_list}")
        return binary_search(sub_list,target)
    elif target>input_string[mid]:
        start=mid+1
        print(f"start={start}")
        sub_list=input_string[start:end+1]
        print(f"sublist:{sub_list}")
        return binary_search(sub_list,target)
    else: # value does not exist
        return -1

print(binary_search([3,10,2,5,39,1],39)) # output: 5
#binary_search([3,10,2,5,39,1],10) # output: 4
        