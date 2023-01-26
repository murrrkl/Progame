from tkinter import *

# Создание и настройка окна
window = Tk()
window.geometry("300x400")
window.title("Моё первое окно")
window["bg"] = "GreenYellow"

# Функции

# Создание элементов экрана
l1 = Label(window, text="Введите первое число:")
e1 = Entry(window)
l2 = Label(window, text="Введите второе число:")
e2 = Entry(window)
b_plus = Button(window, text = "+")
l3 = Label(window, text = "0")

# Добавление элементов на экран
l1.pack()
e1.pack()
l2.pack()
e2.pack()
b_plus.pack()
l3.pack()


window.mainloop()
