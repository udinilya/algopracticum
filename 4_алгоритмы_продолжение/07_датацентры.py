# В массиве указана вместимость датацентров по хранению фото
# Нецелесообразно хранить две копии одного фото в одном датацентре
# Нужно вывести максимальное число фото, которые можно хранить в этих датацентрах с учетом их вместимости

data = [8, 7, 7, 6, 5]

count = 0


def solution(data, count):
    if len(data) <= 1:
        return count
    else:
        new_data = sorted(data, reverse=True)
        count += 1
        new_el_big, new_el_small = new_data[0] - 1, new_data[-1] - 1
        del new_data[-1]
        del new_data[0]
        new_data.append(new_el_big)
        new_data.append(new_el_small)
        if new_data[-1] == 0:
            del new_data[-1]

        return solution(new_data, count)


print(solution(data, count))
