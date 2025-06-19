def get_word_count(text):
    words = text.split()
    i = 0
    for word in words:
        i += 1
    return i

def get_letter_count(text):
    text = text.lower()
    letters = list(text) 
    letter_count = {}
    for letter in letters:
        if letter not in letter_count:
            letter_count[letter] = 0
        letter_count[letter] += 1
    return letter_count

def sort_on(dict):
    return dict["num"]

def sort_chars(letter_count):
    dicts = []
    for letter in letter_count:
        dicts.append({"char": letter, "num": letter_count[letter]})
    dicts.sort(reverse=True, key=sort_on)
    return dicts
