##for i in range(1,4):
##    j = i * 2
##    print(f"i is {i} and j is {j}")



def add_underscores(word):
    new_word = "_"
    for i in range(len(word)):
        new_word = new_word + word[i] + "_"
    return new_word

phrase = "Hello"
print(add_underscores(phrase))
