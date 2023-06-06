def filter_birds(birds, geese):
    filtered_birds = []
    for bird in birds:
        if bird not in geese:
            filtered_birds.append(bird)
    return filtered_birds


# Хорошо, но решение записано в виде функции. А это следующее задание.
# Кстати для функции надо добавить вызов, чтобы проверить работает ли данное решение или нет.

# Поэтому задание представить решение БЕЗ функции! 
# В отдельном файле и его надо закинуть в репозиторий с помощью git.
