import os
# 0 - путь   1 - Папки  2 - Файлы
block = ["DataBase"]
# adress = "\\\\192.168.0.222\\public\\kino\\%s"
# adress = 'C:\\Users\\LexaNoN\\PycharmProjects\\Tele-MRWN\\%s'
adress = "C:\\Users\\ALEXEY\\PycharmProjects\\Tele-MRWN\\Kino\\test dir\\%s"
list = []
for y in next(os.walk(adress % ""))[1]:
    if block.count(y):
        continue
    z = next(os.walk(adress % y))[2]
    for f in z:
        form = [""]
        # form = [".avi", ".mkv", ".mp4"]
        if form.count(f[len(f)-len(form[0]):]): # Расчёт идёт на то, что формать в 4 символа. В теории, можно проверять на пробел
            list.append(f)
        # И списка элементов, прогоняем последние 4 символа формата, .mp4, .mkv . Если не имеет - по индесу удаляем
print(list)