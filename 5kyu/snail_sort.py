# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.
import numpy as np


def snail(snail_map):
    sides = [{'slice': np.s_[0, :], 'axis': 0},
             {'slice': np.s_[:, -1], 'axis': 1},
             {'slice': np.s_[-1, -1::-1], 'axis': 0},
             {'slice': np.s_[-1::-1, 0], 'axis': 1}
             ]

    newarray = np.array(array)

    print(newarray)
    print('======Start: ')
    snailsorted = []
    while len(newarray) > 0:
        for side in sides:
            snailsorted = snailsorted + list(newarray[side['slice']])
            print("To append: ", newarray[side['slice']])
            newarray = np.delete(
                newarray, side['slice'][side['axis']], side['axis'])
            print(newarray)
            print('======')
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

    snailsorted = snail(array)
    print(snailsorted)
    # assert snailsorted == [1, 2, 3, 6, 9, 8, 7, 4, 5] #test 1
    assert snailsorted == [1, 2, 3, 4, 5, 6, 7, 8, 9]  # test 2
