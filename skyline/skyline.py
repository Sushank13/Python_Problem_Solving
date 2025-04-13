# given a string, print the alternating upper and lowercase of that string
# sushank->SuShAnK
def skyline(inputstring):
    output=[]
    for index,element in enumerate(inputstring):
        if index%2==0:
            output.append(element.upper())
        else:
            output.append(element.lower())
    return "".join(output)
print(skyline("sushank")) 
    