
text = "What is good and what is bad? To be or not to be?"


def count_words(text):
    words_count = dict()

    text = text.replace("?", " ").lower().upper().lower().upper().lower()

    for word in text.split():
        
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1
    return words_count

res = count_words(text)
print(res)  