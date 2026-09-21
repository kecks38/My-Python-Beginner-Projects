try:
    first_value = float(input("Первое число: "))
    second_value = float(input("Второе число: "))
    choice = int(input("Выберите операцию с числами: ""\n1 - сложение\n""\n2 - разность\n"
                   "\n3 - умножение\n""\n4 - деление\n"))
except ValueError:
    print("Ошибка ввода, нужно ввести число. Ожидание перезапуска программы")
    exit()

def delenie():
        if second_value == 0:
            print("Делить на ноль нельзя")
        else :
            result_division = first_value / second_value
            return result_division
if choice == 1:
    result = first_value + second_value
    print(f"Результат сложения: {result}")
elif choice == 2:
    result = first_value - second_value
    print(f"Результат разности: {result}")
elif choice == 3:
    result = first_value * second_value
    print(f"Результат умножения: {result}")
elif choice == 4:
    print(f"Результат деления: { delenie() }")
else :
     print("Ошибка выбора функции")
    
