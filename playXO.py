class playXO:
  # Поле
  pole = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
  ]

  # Чей ход 1 - ход крестиков 0 - ход ноликов
  hod = 1
  
  # Печать поля - создание поля
  def PrintPole(self):
    for i in range(0, 3, 1):
      row = self.pole[i] # i-тая Строка
      for j in range(0, 3, 1):
        print(row[j], end = " ") # Печатаю текущую клетку 
      print()

  # Очистка поля
  def Clear(self):
    self.pole = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
  ]

  # Ход, указав номер строки и столбца
  def play(self, row, column):
    if self.pole[row-1][column-1] == "_":
      if self.hod == 1:
        self.pole[row-1][column-1] = "X"
        self.hod = 0 # Следующий ход за ноликами
      else:
        self.pole[row-1][column-1] = "O"
        self.hod = 1 # Следующий ход за крестиками  
    else:
      print("Клетка занята!!!")


  # Команда проверки на победу
  def win(self):
    #  Проверяю каждую строку 
    for i in range(0, 3, 1):
      if self.pole[i] == ["X", "X", "X"]:
        print("победа за крестиками!!!")
      elif self.pole[i] == ["O", "O", "O"]:
        print("победа за ноликами!!!")
    # Проверяю столбцы
    # Проверяю нулевой столбец ПЕРВАЯ ЦИФРА в [] - номер строки; ВТОРАЯ - номер столбца
    if self.pole[0][0] == "X" and  self.pole[1][0] == "X" and self.pole[2][0] == "X":
      print("Победа крестиков")
    elif self.pole[0][0] == "O" and  self.pole[1][0] == "O" and self.pole[2][0] == "O":
      print("Победа крестиков")
    # Проверяю 1-ый столбец
    elif self.pole[0][1] == "O" and  self.pole[1][1] == "O" and self.pole[2][1] == "O":
      print("Победа крестиков") 
    elif self.pole[0][1] == "X" and  self.pole[1][1] == "X" and self.pole[2][1] == "X":
      print("Победа крестиков") 
    # Проверяю 2-ый столбец
    elif self.pole[0][2] == "O" and  self.pole[1][2] == "O" and self.pole[2][2] == "O":
      print("Победа крестиков") 
    elif self.pole[0][2] == "X" and  self.pole[1][2] == "X" and self.pole[2][2] == "X":
      print("Победа крестиков") 
    # Проверяю диагонали ДЗ!!!
    


play1 = playXO() # Создаю новую игру
play1.PrintPole() # Печатаю текущее состояние игры
play1.play(1, 2) # ход крестиков -  Поставить крестик в 1 строку 2 столбец
play1.play(2, 3) # ход ноликов
play1.play(1, 1) # ход крестиков
play1.play(2, 2) # ход ноликов
play1.play(1, 3) # ход крестиков
print()
play1.PrintPole() # Печать поля
play1.win() # Проверка на победу
