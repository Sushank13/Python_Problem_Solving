def timeConversion(s):
    hours=int(s[0:2]) # extract hours
    minutes=s[3:5] #extract minutes
    seconds=s[6:8]# extract seconds
    ampm=s[8:10]
    new_hours=0 
    if ampm=="AM": 
        if hours==12: 
            new_hours="00"
        else:
            new_hours=hours       
    if ampm=="PM":
        if hours!=12:
            new_hours=12+hours
        else:
            new_hours=hours
    if len(str(new_hours))!=2:
        new_hours="0"+str(new_hours)    
    return f"{str(new_hours)}:{minutes}:{seconds}"

if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    print(result)
