import random

def gen_random_char(word_lenght, sentence_lenght):
    for _ in range(sentence_lenght):
        word = []
        for i in range(word_lenght):
            word.append(chr(random.randint(92, 122)))
        yield ''.join(word)

gen_chars = gen_random_char(5, 5)
print(gen_chars)
for el in gen_chars:
    print(el)