# 1. Напишите программу, удаляющую из 
# текста все слова содержащие "абв". В тексте используется разделитель пробел.
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

from random import sample

def list_words(count: int, alp: str = 'абв'):
    words_list = []
    for _ in range(count):
        my_text = sample(alp, len(alp))
        words_list.append("".join(my_text))
    return " ".join(words_list)

def exam(words: str) -> str:
    return " ".join(i for i in words.split() if i != "абв")

al_list = list_words(int(input("Number of words: ")))
print(al_list)
print(exam(al_list))