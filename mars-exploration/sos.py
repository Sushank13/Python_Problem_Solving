def marsExploration(s):
    list_of_sos_msgs=[s[i:i+3] for i in range(0,len(s),3)] # slicing a string using range()
    count=0
    for sos in list_of_sos_msgs:
            if sos[0]!="S":
                count=count+1 
            if sos[1]!="O":
                count=count+1 
            if sos[2]!="S":
                count=count+1
                
    return count
                    
if __name__ == '__main__':
    s = input()
    result = marsExploration(s)
    print(result)