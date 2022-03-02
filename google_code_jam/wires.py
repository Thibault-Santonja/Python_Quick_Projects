from typing import Tuple, List


def calculate_intersections(input_links: List[Tuple[int, int]]) -> int:
    """

    @param input_links: List of tuple which represents links between two windows
    @return: Number of intersections between two wires
    """
    # Copy link to keep input data immutability
    links = input_links.copy()

    # Sort wires
    links.sort()

    # Algorithm
    res = 0
    diff = [link[0] - link[1] for link in links]
    print(diff)
    """
    for idx, link in enumerate(links):
        if link[0] == link[1]:
            continue
        if link[0] > link[1]:
            res += count_bigger(links[:idx], link[1])
        else:
            res += count_lower(links[idx+1:], link)
    """

    return res


def count_lower(wires: List[Tuple[int, int]], value: tuple) -> int:
    """

    @param wires:
    @param value:
    @return:
    """
    counter = 0
    for wire in wires:
        if wire[1] < value[1]:
            counter += 1
    return counter
    pass


def count_bigger(wires: List[Tuple[int, int]], value: int) -> int:
    """

    @param wires:
    @param value:
    @return:
    """
    counter = 0
    for wire in wires:
        if wire[1] > value and wire[0] == wire[1]:
            counter += 1
    return counter

"""
Si tous les liens sont //, on a 0 intersection -> il faut des "outliners"
si 
"""

if __name__ == "__main__":
    test = [(1, 10), (3, 3), (2, 2), (6, 4), (5, 5), (8, 8), (7, 9)]
    print(test[:2])
    print(test[2:])

    print(calculate_intersections([(1, 10)]))
    print(calculate_intersections([(1, 10), (3, 3), (2, 2)]))
    print(calculate_intersections([(10, 1), (3, 3), (2, 2)]))
    print(calculate_intersections([(10, 1), (3, 3), (2, 2), (1, 10)]))
