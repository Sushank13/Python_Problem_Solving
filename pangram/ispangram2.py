# check if a string is pangram or not 
# pangram is a string that has every alphabet of the english letters
def is_pangram(sentence):
    new_sentence=sentence.lower().replace(" ","")
    return True if len(set(new_sentence))==26 else False
print(is_pangram("We promptly judged antique ivory buckles for the next prize"))
print(is_pangram("We promptly judged antique ivory buckles for the prize"))