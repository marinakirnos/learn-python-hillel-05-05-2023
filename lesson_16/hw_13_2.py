"""
Написати генератор, який приймає параметром строку s та при кожному запиті видає наступне слово зі строки s.
Тобто, при використанні генератора:
for word in word_gen('i am generating words from text'):
    print(word)
"""


def str_generator(data_str: str):
    words = data_str.split()
    for word in words:
        yield word


if __name__ == '__main__':
    word_gen = str_generator('i am generating words from text')
    for i in word_gen:
        print(i)
