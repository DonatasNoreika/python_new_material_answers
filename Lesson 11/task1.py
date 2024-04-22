def puzzle_pieces(list1: list, list2: list) -> bool:
    if len(list1) != len(list2):
        return False

    sum_value = None
    for i in range(len(list1)):
        if sum_value is None:
            sum_value = list1[i] + list2[i]
        elif list1[i] + list2[i] != sum_value:
            return False

    return True


print(puzzle_pieces([1, 2, 3, 4], [4, 3, 2, 1]))
print(puzzle_pieces([1, 8, 5, 0, -1, 7], [0, -7, -4, 1, 2, -6]))
print(puzzle_pieces([1, 2], [-1, -1]))
print(puzzle_pieces([9, 8, 7], [7, 8, 9, 10]))
