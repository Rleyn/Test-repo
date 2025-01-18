import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        q1 = int(entry_num1.get())
        q2 = int(entry_num2.get())
        operation = operation_var.get()

        if operation == "Сложение":
            result = q1 + q2
            operation_name = "сложения"
        elif operation == "Вычитание":
            result = q1 - q2
            operation_name = "вычитания"
        elif operation == "Деление":
            if q2 == 0:
                messagebox.showerror("Ошибка", "На ноль делить нельзя")
                return
            result = q1 / q2
            operation_name = "деления"
        elif operation == "Умножение":
            result = q1 * q2
            operation_name = "умножения"
        else:
            messagebox.showerror("Ошибка", "Выберите корректную операцию")
            return

        label_result.config(text=f"Результат {operation_name} = {result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа")

# Создание окна приложения
root = tk.Tk()
root.title("Калькулятор")

# Поля ввода чисел
label_num1 = tk.Label(root, text="Введите число 1:")
label_num1.pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Введите число 2:")
label_num2.pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

# Выбор операции
label_operation = tk.Label(root, text="Выберите операцию:")
label_operation.pack()

operation_var = tk.StringVar(value="Сложение")
operations = ["Сложение", "Вычитание", "Деление", "Умножение"]
for op in operations:
    rb = tk.Radiobutton(root, text=op, variable=operation_var, value=op)
    rb.pack(anchor="w")

# Кнопка для выполнения расчета
btn_calculate = tk.Button(root, text="Вычислить", command=calculate)
btn_calculate.pack()

# Поле для отображения результата
label_result = tk.Label(root, text="Результат появится здесь", font=("Arial", 12))
label_result.pack()

# Запуск основного цикла приложения
root.mainloop()