print("Введите стороны треугольника a, b, c: ")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
result = ""

if a + b < c or a + c < b or b + c < a:
    result = "Треугольник невозможен"
elif a == b and b == c:
    result = "Треугольник равносторонний"
elif a == b or a == c or b == c:
    result = "Треугольник равнобедренный"
elif a != b and b != c:
    result = "Треугольник разносторонний"

print(result)