# coding:utf-8
# 习题25，更多更多的联系

def break_words(stuff):
    words = stuff.split(' ')
    return words

def sort_words(words):
    return sorted(words)

def print_first_word(words):
    word = words[0]
    print(word)

def print_last_word(words):
    word = words[-1]
    print(word)

def sort_sentence(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words = sort_words(sentence)
    print_first_word(words)
    print_last_word(words)

# print_first_and_last_sorted("All good things come to those who wait.")

# sentence = "All good things come to those who wait."
sentence = ['bob', 'about', 'Zoo', 'Credit']
# words1 = break_words(sentence)
# print(words1)
# sort_words1 = sort_words(words1)
# print(sort_words1)
# print_first_word(sort_words1)
# print_last_word(words1)
# print(words1)
# print_first_word(words1)
# print_last_word(words1)
print_first_and_last_sorted(sentence)
print(sentence)