getName = lambda student: student['Name']
getMark = lambda student: student['Mark']

students = []

with open('D:/Навчання Політех/Другий курс/Програмування/TP-KB-222-Serhii-Zozulia/topic_06/students.txt', 'r') as file:
    next(file)  # Пропускаємо перший рядок з заголовками
    for line in file:
        parts = line.strip().split(',')
        if len(parts) == 2:
            mark, name = parts  # Зміни порядок, так як дані в іншому порядку
            students.append({'Name': name, 'Mark': int(mark)})

sortName = sorted(students, key=getName)
sortMark = sorted(students, key=getMark)

print("Сортування за ім'ям:")
for student in sortName:
    print(f"Ім'я: {student['Name']}, Оцінка: {student['Mark']}")

print("\nСортування за оцінкою:")
for student in sortMark:
    print(f"Ім'я: {student['Name']}, Оцінка: {student['Mark']}")
