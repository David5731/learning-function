import string
alphabets =  "abcdefghijklmnopqrstvwxyz "
sentence = input("enter sentence: ")
def my_function():
    finally1 = 1
    for letter in alphabets:
        if letter in sentence :
            finally1 *= 1
        if letter not in sentence:
            finally1 *= 0
    return finally1

p = my_function()
if p == 1 :
    print(sentence, "is a Pangram")
if p == 0:
    print(sentence,"Not pangram")


            
