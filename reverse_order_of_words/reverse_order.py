# Reverse the order of words in a sentence
def reverse_order(sentence):
    list_of_words=sentence.split()
    list_of_words.reverse()
    return " ".join(list_of_words)
print(reverse_order("This is, a sample sentence!"))