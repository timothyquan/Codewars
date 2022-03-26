# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.
import numpy as np


def snail(snail_map):

    sides = [{'slice': np.s_[0, :], 'axis': 0},  # top row
             {'slice': np.s_[:, -1], 'axis': 1},  # right column downward
             {'slice': np.s_[-1, -1::-1], 'axis': 0},  # bottom row
             {'slice': np.s_[-1::-1, 0], 'axis': 1}  # left column upward
             ]

    newarray = np.array(array)

    snailsorted = []
    while len(newarray) > 0:
        for side in sides:
            snailsorted = snailsorted + list(newarray[side['slice']])
            newarray = np.delete(
                newarray, side['slice'][side['axis']], side['axis'])
            if len(newarray) < 1:
                break
    return(snailsorted)


if __name__ == '__main__':
    array = [[1, 2, 3],  # test 1
             [4, 5, 6],
             [7, 8, 9]]

    array = [[1, 2, 3],  # test 2
             [8, 9, 4],
             [7, 6, 5]]

    array = [[1, 2, 3, 4],  # test 3
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]]

    snailsorted = snail(array)

    print(snailsorted)
    # assert snailsorted == [1, 2, 3, 6, 9, 8, 7, 4, 5] #test 1
    # assert snailsorted == [1, 2, 3, 4, 5, 6, 7, 8, 9]  # test 2
    assert snailsorted == [1, 2, 3, 4, 8, 12, 16,
                           15, 14, 13, 9, 5, 6, 7, 11, 10]  # test 3
