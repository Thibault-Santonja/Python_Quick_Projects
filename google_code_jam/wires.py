from typing import Tuple, List


def calculate_intersections(input_links: List[Tuple[int, int]]) -> int:
    """

    @param input_links: List of tuple which represents links between two windows
    @return: Number of intersections between two wires
    """
    # Copy link to keep input data immutability
    links: List[Tuple[int, int]] = input_links.copy()

    # Sort wires
    links.sort()

    # Algorithm
    intersections: List[Tuple[float, float]] = []
    for idx, link in enumerate(links):
        for link_ in links[idx:]:
            if link_[0] > link[0] and link_[1] < link[1] or link_[0] < link[0] and link_[1] > link[1]:
                intersect: Tuple[float, float] = find_line_intersection_point(
                    (0, link[0]),
                    (1, link[1]),
                    (0, link_[0]),
                    (1, link_[1])
                )
                if intersect not in intersections:
                    intersections.append(intersect)

    return len(intersections)


def det(a: Tuple[float, float], b: Tuple[int, int]) -> float:
    """
    Calculate determinant of a vector

    @param a: first point
    @param b: final point
    @return: determinant
    """
    return a[0] * b[1] - a[1] * b[0]


def find_line_intersection_point(p1: Tuple[int, int], p2: Tuple[int, int],
                                 p3: Tuple[int, int], p4: Tuple[int, int]) -> Tuple[float, float]:
    """

    @param p1: first point of vector 1
    @param p2: final point of vector 1
    @param p3: first point of vector 2
    @param p4: final point of vector 2
    @return: intersection position
    """
    xdiff = (p1[0] - p2[0], p3[0] - p4[0])
    ydiff = (p1[1] - p2[1], p3[1] - p4[1])

    div = det(xdiff, ydiff)
    if div == 0:
        raise ValueError('lines do not intersect')

    d = (det(p1, p2), det(p3, p4))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div

    return x, y
