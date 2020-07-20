"""Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b.
array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:
array_diff([1,2,2,2,3],[2]) == [1,3]"""


def array_diff(a, b):
    # your code here
    for search_el in b:
        for del_index in sorted(
            [i for i, el in enumerate(a) if el == search_el], reverse=True
        ):
            del a[del_index]
    return a


print(array_diff([1, 2, 2, 2, 3], [2]))
