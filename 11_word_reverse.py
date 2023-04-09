# Напишите скрипт, который получает строку и переворачивает каждое слово в ней. 
# Все пробелы в строке должны быть сохранены.

# Например:
#   "This is an example!" ==> "sihT si na !elpmaxe"
#   "double  spaces"      ==> "elbuod  secaps"

def reverse_words(string):
  words = string.split(" ")
  reversed_words = [word[::-1] for word in words]
  return(reversed_words)
