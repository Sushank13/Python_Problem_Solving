if __name__ == '__main__':
    records=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    scores=[]
    for i in range(0,len(records)):
        scores.append(records[i][1])
    scores.sort()
    second_lowest_score=scores[1]
    names=[]
    for i in range(0,len(records)):
        if records[i][1]==second_lowest_score:
            names.append(records[i][0])
    names.sort()
    for name in names:
        print(name)