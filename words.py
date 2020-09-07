def print_upper_words(words, start):
    for word in words:
        for char in start:
            if word[0] == char:
                print(word.upper())

print_upper_words(["james", "maria", "oliver", 'eric'], ['e', 'o'])
