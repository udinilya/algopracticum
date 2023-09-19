# Дано расписание уроков. Нужно составить оптимальное расписание и провести как можно больше уроков

n = int(input()) # количество уроков
shedule = [input().split() for i in range(n)] # начало и конец уроков

ends = []
double_beginnings = []
sort_shedule = []

while shedule:
    for i in shedule:
        ends.append(float(i[-1]))

    min_ends = min(ends, key=lambda i: float(i)) # находим урок который раньше всех заканчивается
    ends.clear()

    # если есть уроки с одинаковым миним окончанием и разным началом добавляем которы раньше из них начинается
    for i in shedule:
        if float(i[-1]) == min_ends:
            double_beginnings.append(float(i[0]))

    min_double_beginnings = min(double_beginnings, key=lambda i: float(i))
    for i in shedule:
        if float(i[0]) == min_double_beginnings:
            sort_shedule.append(i)
    double_beginnings.clear()

    # удаляем из расписания все уроки, которые уже закончились по времени (пересекающиеся)
    i = 0
    while i < len(shedule):
        if float(shedule[i][0]) < min_ends:
            del shedule[i]
        elif float(shedule[i][0]) == float(shedule[i][-1]) and float(shedule[i][0]) == min_ends:
            del shedule[i]
        else:
            i += 1

print(sort_shedule)
