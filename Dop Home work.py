#Доп.задание 3: The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

def GenerateWords(w):
    w = w.lower()
    result = ''
    for sym in word:
        if word.count(sym) > 1:
            result += ')'
        else:
            result += '('
    return result
OrigWord = (input('Введите строку: '))
