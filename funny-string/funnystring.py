def funnyString(s):
    r=s[::-1] #string in reverse
    s_list=[]
    r_list=[]

    for i in range(len(s)-1):
        s_diff=abs(ord(s[i])-ord(s[i+1]))
        r_diff=abs(ord(r[i])-ord(r[i+1]))
        s_list.append(s_diff)
        r_list.append(r_diff)
    return "Funny" if s_list==r_list else  "Not Funny"

if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = funnyString(s)
        print(result)

