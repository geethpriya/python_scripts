"""
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

import itertools
import unittest

''' Test Lists'''
test_list1 = [10, 15, 3, 7]
test_list2 = [-1, -5, -8, 10]
test_list3 = [23, 45, 67, 56]
test_list4 = [0, 0, 1, 1]


def check(list_num, val):
    for i in range(len(list_num)):
        for j in range(len(list_num)):
            if i == j:
                continue
            else:
                if list_num[i] + list_num[j] == val:
                    return True
    return False


def check_sum_two(list_num, val):
    """
    :param list_num: list of numbers to check
    :param val: int value to check against the list
    :return: bool (True or False)
    """

    for (i, j) in itertools.combinations(list_num, 2):
        if i + j == val:
            return True
    return False


class MyTest(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(check_sum_two(test_list1, 18), True, "test_case1 Failed")

    def test_case2(self):
        self.assertEqual(check_sum_two(test_list2, 9), True, "test_case2 Failed")

    def test_case3(self):
        self.assertEqual(check_sum_two(test_list3, 68), True, "test_case3 Failed")

    def test_case4(self):
        self.assertEqual(check_sum_two(test_list4, 2), True, "test_case4 Failed")


if __name__ == '__main__':
    unittest.main()
