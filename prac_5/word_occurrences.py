word_to_count = {}
text = input("Please enter a string: ").lower()
words = text.split()
for word in words:
    word_count = word_to_count.get(word, 0)
    word_to_count[word] = word_count + 1
words = list(word_to_count.keys())
words.sort()
max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, word_to_count[word]))

