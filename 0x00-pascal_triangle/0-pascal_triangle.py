#!/usr/bin/python3
"""
Module to find Pascal's Triangle integers
"""


def pascal_triangle(n):
    """
    Function to find Pascal's Triangle integers

    Args:
        n (int): The number of rows of Pascal's triangle

    Returns:
        list: Pascal's triangle as a list of lists
    """
    pascal_triangle = []
    
    if not isinstance(n, int) or n <= 0:
        return pascal_triangle

    pascal_triangle.append([1])
    
    if n > 1:
        pascal_triangle.append([1, 1])

    for x in range(3, n+1):
        row = [0] * x
        row[0] = 1
        row[-1] = 1

        for y in range(1, x-1):
            row[y] = pascal_triangle[x-2][y-1] + pascal_triangle[x-2][y]

        pascal_triangle.append(row)

    return pascal_triangle
