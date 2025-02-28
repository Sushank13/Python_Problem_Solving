from collections import defaultdict
if __name__=="__main__":
    integer_input=input()
    n,m=tuple(integer_input.split())
    group_a=defaultdict(list) # Group A would be a dictionary of list i.e. each key will have list values
    # can not typecast a list using normal dict but only default dict as default dict does not expect a key
    # it will simply assign an empty list [] to missing keys.
    group_b=[]
    for index in range(1,int(n)+1):
        word=input()
        group_a[word].append(index)
    #print(group_a)
    for _ in range(1,int(m)+1):
        word=input()
        group_b.append(word)
    #print(group_b)
    for word in group_b:
        if word in group_a.keys():# word in Group B appears in Group A
            output=""
            for index in group_a[word]:
                if len(output)>0:
                    output=output+" "+str(index)
                else:
                    output=output+str(index)
            print(output)
        else:
            print(-1)
