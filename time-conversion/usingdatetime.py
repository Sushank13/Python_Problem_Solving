from datetime import datetime
def timeConversion(s):
    return datetime.strptime(s,"%I:%M:%S%p").strftime("%H:%M:%S") # parse the string into datetime 12-hr format and then format datetime into string with 24-hr format 
if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    print(result)

