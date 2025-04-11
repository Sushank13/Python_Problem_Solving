# Reverse the order of words in a sentence
import string
def reverse_order(sentence):
    sentence_with_no_spcl_char=remove_special_char(sentence)
    list_of_words=sentence_with_no_spcl_char.split()
    list_of_words.reverse()
    return " ".join(list_of_words)
def remove_special_char(sentence):
    new_sentence=""
    for char in sentence:
        if char in string.punctuation:
            continue
        new_sentence=new_sentence+char
    return new_sentence
print(reverse_order("This is, a sample sentence!"))