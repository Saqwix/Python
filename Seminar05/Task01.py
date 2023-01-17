# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба
# in
# Number of words: 6
# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва
# in
# Number of words: -1
# out
# The data is incorrect

# text = input("Введите текст через пробел:\n")
# print(f"Исходный текст: {text}")
# find_text = "абв"
# list = [i for i in text.split() if find_text not in i]
# print(f'Результат: {" ".join(list)}')

import random

text = "абв"
print("Слово которое нужно удалить из текста: ", text)
num_word = (int(input("Number of words: ")))
list_word = []
print("Random text: ")
for x in range(num_word):
    random_text = random.sample(text, 3)
    list_word.append("".join(random_text))

print(" ".join(list_word))

print("Result: ")
list_word2 = list(filter(lambda x: text not in x, list_word))
print(" ".join(list_word2))