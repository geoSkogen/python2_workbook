def break_phrase(stuff):
    words = stuff.split(' ')
    return words

def sort_words(words):
    return sorted(words)

def pop_word(words, num):
    index = int(num)
    word = words.pop(index)
    return word

def sort_sentence(sentence):
    words = break_phrase(sentence)
    return sort_words(words)
