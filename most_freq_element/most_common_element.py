# given a string, find the most common element(s) in it
# inputstring="This is a sample string!"
# output: elements with highest freq
# modify my input: lowercase->remove spaces+special characters
#generate a map-> element:freq
#list of values->sort->get highest value
# retrieve keys/elements with value=highest value
# possibility of more than one element with highest value
import string
from collections import Counter
def most_common_element(inputstring):
    inputstring=inputstring.lower()
    modified_string=remove_chars_spaces(inputstring)
    element_freq=dict(Counter(modified_string))
    list_of_values=list(element_freq.values())
    list_of_values.sort()
    highest_frequency=list_of_values[-1]
    output=[]
    for key,value in element_freq.items():
        if value==highest_frequency:
            output.append(key)
    return output
def remove_chars_spaces(inputstring):
    output=[]
    for element in inputstring:
        if element in string.punctuation:
            continue
        output.append(element)
    return "".join(output)
print(most_common_element("Abb acc!@cVb "))