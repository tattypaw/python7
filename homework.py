""" Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
Поскольку разобраться в его кричалках не настолько просто, 
насколько легко он их придумывает, Вам стоит написать программу. 
Винни-Пух считает, что ритм есть, если число слогов (т.е. число 
гласных букв) в каждой фразе стихотворения одинаковое. Фраза может 
состоять из одного слова, если во фразе несколько слов, 
то они разделяются дефисами. Фразы отделяются друг от друга 
пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры.
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и 
“Пам парам”, если с ритмом все не в порядке """

def charFind(str, char):
  result = []
  nChar = 0
  for i in range(len(str)+1):
    if i == len(str) or str[i] == char: 
      result.append(str[nChar:i])
      nChar = i+1
  return result

def vowelCounter(str):
  result = 0
  vowel = 'ауеыоэяиюё'
  result = sum(1 for i in str if i in vowel) 
  return result

poem = input('Введите стихотворение: ')
#poem = 'пара-ра-рам рам-пам-папам па-ра-па-дам'

arrLines = charFind(poem, ' ')

arrCounter = [vowelCounter(i) for i in arrLines]

flag = True

for i in range(1,len(arrCounter)):
  if arrCounter[i-1] != arrCounter[i]: flag = False

if flag : 
  print('Парам пам-пам')
else:
  print('Пам парам') 

""" Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы 
(подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, 
у которой ровно два аргумента, как, например, у операции умножения. 
Ввод: print_operation_table(lambda x, y: x * y) 
Вывод:
1 2 3 4 5 6
2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36 """

def print_operation_table(operation, num_rows, num_columns):
    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            print(operation(i, j), end=" ")
        print('')
    return

num_rows = int(input("Введите число строк в таблице: "))
num_columns = int(input("Введите число столбцов в таблице: "))
print_operation_table(lambda x, y: x * y, num_rows, num_columns) 
