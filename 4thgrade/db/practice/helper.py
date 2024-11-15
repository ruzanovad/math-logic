from copy import deepcopy


def decompose_fd(fds):
    """
    Разбивает зависимости с множеством атрибутов справа
    на несколько зависимостей с одним атрибутом справа
    """
    decomposed_fds = []
    for left, right in fds:
        for r in right:
            decomposed_fds.append((left, {r}))
    return decomposed_fds


def find_closure(attributes, fds):
    """
    Находит замыкание атрибутов по множеству зависимостей
    """
    closure = set(attributes)  # по множеству каких атрибутов строим
    while True:
        new_elements = len(closure)  # текущее количество атрибутов
        for left, right in fds:
            if set(left).issubset(closure):  # если левая часть текущей ФЗ
                # является подмножеством текущего множества атрибутов, добавляем туда
                # правую часть
                closure.update(right)
        if len(closure) == new_elements:  # если на текущем шаге не добавили ни одну...
            break
    return closure


def remove_redundant_fds(fds):
    """
    Удаляет избыточные зависимости
    """
    minimized_fds = deepcopy(fds)
    for fd in fds:
        minimized_fds.remove(fd)  # удаляем из множества ФЗ текущую
        closure = find_closure(
            fd[0], minimized_fds
        )  # строим замыкание на основе левой части

        if not fd[1].issubset(closure):  # если правую часть не удалось вывести
            # мы не можем ее удалить, добавляем обратно
            minimized_fds.append(fd)
        else:
            print("Удаляем ФЗ", fd[0], "->", fd[1])
    return minimized_fds


def remove_redundant_attributes(fds):
    """
    Удаляет избыточные атрибуты из левой части каждой зависимости
    """

    minimized_fds = deepcopy(fds)
    for i in range(len(minimized_fds)):
        left, right = minimized_fds[i]
        left = list(left)  # левые части
        flag = False
        if len(left) > 1:  # слева больше одного атрибута
            for attr in left:  # пытаемся удалить атрибут
                test_left = set(left)
                test_left.remove(attr)
                closure = find_closure(
                    test_left, minimized_fds
                )  # minimized fds обновляется
                # находим замыкание на основе оставшихся атрибутов
                if right.issubset(closure):
                    flag = True
                    left.remove(attr)
                    print(
                        f"Удаляем избыточный атрибут '{attr}' из зависимости: {left | {attr}} -> {right}"
                    )
        if flag:
            minimized_fds[i] = (set(left), right)
    return minimized_fds


def minimal_cover(fds):
    """
    Строит минимальное покрытие для множества функциональных зависимостей
    """
    decomposed_fds = decompose_fd(fds)
    without_redundant_fds = remove_redundant_fds(decomposed_fds)
    minimized_fds = remove_redundant_attributes(without_redundant_fds)
    return minimized_fds


def reading_function(file="dependencies.md"):
    fds = []
    with open(file, "r") as f:
        lines = f.readlines()
        for line in lines:
            left, right = line.strip().split(" -> ")
            left_set = set(left.split(", "))
            right_set = set(right[1:-1].split(", "))
            fds.append((left_set, right_set))
    return fds


# fds = {
#     ("A1",): {"A2", "A3", "A4", "A5", "A6", "A7", "A8"},
#     ("B1",): {"B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10", "B11"},
#     ("C1",): {"C2"},
#     ("D1",): {"D2"},
# }


def convert_fds_list_to_map_single(fds_list):
    """
    :param fds_list: Список кортежей вида (set(left), set(right))
    :return: Словарь вида {left: set(right)}
    """
    fd_map = {}
    for left, right in fds_list:
        left = frozenset(left)
        # right = frozenset(right)
        if left in fd_map.keys():
            fd_map[left] |= right
        else:
            fd_map[left] = right
    return fd_map


def printing_function(fds):
    converted = convert_fds_list_to_map_single(fds)
    for x, y in converted.items():
        print(set(x), ":", y)


fds = reading_function()
printing_function(fds)

min_cover = minimal_cover(fds)
print("Минимальное покрытие:")
printing_function(min_cover)