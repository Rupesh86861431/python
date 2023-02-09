def max_words(sentences):
    max_words = 0
    for sentence in sentences:
        words = sentence.split()
        print(words)
        max_words = max(max_words, len(words))
    return max_words
sentences = input("Enter the sentences separated by comma: ").split(',')
print(sentences)
print("Maximum number of words in a sentence: ", max_words(sentences))

