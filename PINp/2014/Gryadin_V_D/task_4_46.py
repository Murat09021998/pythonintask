#Задача 4. Вариант 48
#Напишите программу, которая выводит имя, под которым скрывается Чарльз Лютвидж 
#Доджсон. Дополнительно необходимо вывести область интересов указанной личности, место
#рождения, годы рождения и смерти (если человек умер), вычислить возраст на данный момент
#(или момент смерти). Для хранения всех необходимых данных требуется использовать
#переменные. После вывода информации программа должна дожидаться пока пользователь
#нажмет Enter для выхода.

#Gryadin V. D.

print("Чарльз Лютвидж Доджсон или Лью́ис Кэ́рролл")
print("Место рождения: деревня Дарсбери, графство Чешир ")
a = 1832
b = 1898
v = b-a
print("Год рождения: " + str(a))
print("Год смерти: " + str(b))
print('Возраст: ' + str(v))
print("Область интересов: английский писатель, математик, логик, философ, диакон и фотограф ")
input("\n\nНажмите Enter для выхода.")
