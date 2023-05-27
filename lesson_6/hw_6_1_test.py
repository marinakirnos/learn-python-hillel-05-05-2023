import string

words = input("Введіть звернення: ").lower()
words = words.split()  # разбиение по словам
new_words = list()
for word in words:
    word = word.strip(string.punctuation)  # убрать пунктуации
    if not word:  # если слово пустое
        continue  # прервать текущую итерацию и перейти к следующей
    new_words.append(word)
new_words_without_punctuation = ''.join(new_words)
new_words_without_punctuation_2 = new_words_without_punctuation[::-1]
# new_words.append(word.strip(string.punctuation))
if new_words_without_punctuation == new_words_without_punctuation_2:
    print('Строка є паліндромом')
else:
    print('Строка не є паліндромом')
print(new_words)
print(new_words_without_punctuation)
print(type(new_words_without_punctuation))
print(new_words_without_punctuation_2)
