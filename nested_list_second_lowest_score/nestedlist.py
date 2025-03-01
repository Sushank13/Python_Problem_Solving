if __name__ == '__main__':
    records=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    scores=sorted(set([student[1] for student in records])) #using list comprehension instead of for loop to create list 
    # of scores only. Then typecasting with set() to get unique records.Then sorting the set. 
    second_lowest_score=scores[1]
    names=sorted([student[0] for student in records if student[1]==second_lowest_score]) # similarly 
    #using list comprehension here instead of for loop.
    for name in names:
        print(name)