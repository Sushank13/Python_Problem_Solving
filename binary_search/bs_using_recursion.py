def binary_search(input_string,target,start,end):
    if start>end: # whole, array traversed, value does not exist
        return -1
    mid=(start+end)//2
    if target==input_string[mid]:
        return mid #halt/base condition
    elif target<input_string[mid]:
        end=mid-1
        return binary_search(input_string,target,start,end)
    elif target>input_string[mid]:
        start=mid+1
        return binary_search(input_string,target,start,end)
    
input1=[3,10,2,5,39,1]
input1.sort()
print(binary_search(input1,39,0,len(input1)-1)) # output: 5
input2=[3,10,2,5,39,1]
input2.sort()
print(binary_search(input2,10,0,len(input2)-1)) # output: 4
input3=[3,10,2,5,39,1]
input3.sort()
print(binary_search(input3,4,0,len(input3)-1)) # output: -1