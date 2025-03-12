import string
def minimumNumber(n, password):
    criteria_map={"digits":0,"lowercase":0,"uppercase":0,"specialchar":0}
    for element in password:
        if element.isdigit() is True:
            criteria_map["digits"]=criteria_map["digits"]+1
        if element.islower() is True:
            criteria_map["lowercase"]=criteria_map["lowercase"]+1
        if element.isupper() is True:
            criteria_map["uppercase"]=criteria_map["uppercase"]+1
        if element in string.punctuation:
            criteria_map["specialchar"]=criteria_map["specialchar"]+1
    count=0
    for value in criteria_map.values():
        if value==0: # that criteria is not met
            count=count+1
    if n+count<6: # If current password length + missing criteria count is still < 6
        extra_char=6-(n+count) # Extra characters needed to reach length 6
        return count+extra_char
    else: # length criteria met after adding count of missing criteria
        return count
        
if __name__ == '__main__':
    n = int(input().strip())
    password = input()
    answer = minimumNumber(n, password)
    print(answer)