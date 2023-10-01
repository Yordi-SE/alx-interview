#!/usr/bin/python3
"""pascal triangle function"""


def pascal_triangle(n):
    if n <= 0:
        return []
    main_list = [[1], [1, 1]]
    sub_list = []
    for j in range(n - 2):
        for i in range(len(main_list[-1]) - 1):
            sub_list.append(main_list[-1][i] + main_list[-1][i + 1])
        sub_list.append(1)
        sub_list.insert(0, 1)
        main_list.append(sub_list)
        sub_list = []
    return main_list
