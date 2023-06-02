# Напишите скрипт, который получает строку и переворачивает каждое слово в ней. 
# Все пробелы в строке должны быть сохранены.

# Например:
#   "This is an example!" ==> "sihT si na !elpmaxe"
#   "double  spaces"      ==> "elbuod  secaps"

def reverse_words(string):
  words = string.split(" ")
  reversed_words = [word[::-1] for word in words]
  return(reversed_words)


# Хорошо, но решение записано в виде функции. А это следующее задание.
# Кстати для функции надо добавить вызов, чтобы проверить работает ли данное решение или нет.

# Поэтому задание представить решение БЕЗ функции! 
# В отдельном файле и его надо закинуть в репозиторий с помощью git.

string = "Hello World"
words = string.split(" ")
reversed_words = [word[::-1] for word in words]
print(reversed_words)

# Сделала решение без функции. Правильно ?)
