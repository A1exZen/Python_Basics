# Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и обще количество занятий по немеу.
# Вывести его на экран.
# Примеры строк файла(не менее 10 предметов): Информатика: 100(л)  50(пр)  20(лаб).
#                      Физика:  30(л)  10(лаб)
#                      Физкультура: 30(пр)
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


subjects = {}


with open("./Lab_3/3/File.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

for line in lines:
    parts = line.split(":")
    subject = parts[0].strip()
    info = parts[1].split()

    total_l = 0
    total_pr = 0
    total_lab = 0

    for item in info:
        if "(л)" in item:
            total_l += int(item.split("(л)")[0])
        elif "(пр)" in item:
            total_pr += int(item.split("(пр)")[0])
        elif "(лаб)" in item:
            total_lab += int(item.split("(лаб)")[0])

    total_classes = total_l + total_pr + total_lab
    subjects[subject] = total_classes

for subj, total in subjects.items():
    print(f"{subj}: {total}")
