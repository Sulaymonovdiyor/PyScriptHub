#вызываем графический модуль с окном для графики
import turtle
t - "будет у нас ручкой"
t=turtle.Pen()
#составляем список цветов (МОЖНО ДОБАВИТЬ И ДРУГИЕ СВЕТА)
colors=["red","yellow","blue","orange"]
#цикл, в котором будет повторятся ниженаписанный код
for x in range(50):
    #код для перебора цвета в ручке
    t.color(colors[x%4])
    #согласно циклу, значение x будет увеличивать на 1 
    t.circle(x)
    #поворот налево
    t.left(90)
