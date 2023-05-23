
def age_check(age):
    result = ("Значит, ты ребенок!" if age <= 12 else 
              "Значит, ты подросток!" if age <= 17 else 
              "Значит, ты взрослый!" if age <= 64 else 
              "Значит, ты пожилой человек!")
    return result

# Пример использования
age = 18
result = age_check(age)
print(result) # Output: "Значит, ты взрослый!"