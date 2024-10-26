"""Написать программу, которая:
- Запрашивает у пользователя строку для поиска.
- Находит и выводит все строки, которые содержат искомую подстроку, а также их количество из следующего файла.
- Сортирует найденные строки в порядке их длины (от самой короткой к самой длинной) и выводит их."""
searchStr=input("Введите искомую строку: ")
with open('text.txt', 'r', encoding="Windows 1251") as text:
    lines=text.readlines()

listOfStr=[]
for line in lines:
    if searchStr in line:
        listOfStr.append(line.strip())
strLength=len(listOfStr)
print("Кол-во строк с искомой подстрокой: ", strLength)

for line in sorted(listOfStr, key=len):
    print(line)