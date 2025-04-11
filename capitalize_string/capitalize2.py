# WAP to capitalize each word of the string 
def capitalize_each_word(sentence):
    capitalized_words=[]
    for word in sentence.split():
        capitalized_words.append(word.capitalize())
    return " ".join(capitalized_words)
        
print(capitalize_each_word("This is a sample string"))