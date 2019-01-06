import unittest
import functools

"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array 
is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be 
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

"""


def mul(x, y):
    return x * y


def product_list(list_num):
    """
    :param list_num: integer of list of numbers
    :return: list of numbers as per the problem
    """
    return [functools.reduce(mul, x) for x in [list_num[:i] + list_num[i + 1:] for i in range(len(list_num))]]


'''Test List'''
test_list1 = [3, 4, -1, 1]
test_list2 = [1, 2, 0]
test_list3 = [2, 4, -8, 10, 15, 0, 0, -1, 1]
test_list4 = [0, 0, 0]


class MyTest(unittest.TestCase):
    def test_case1(self):
        self.assertListEqual(product_list(test_list1), [-4, -3, 12, -12], msg="test_case1 not passed")

    def test_case2(self):
        self.assertListEqual(product_list(test_list2), [0, 0, 2], msg="test_case2 not passed")

    def test_case3(self):
        self.assertListEqual(product_list(test_list3), [0, 0, 0, 0, 0, 0, 0, 0, 0], msg="test_case3 not passed")

    def test_case4(self):
        self.assertListEqual(product_list(test_list4), [0, 0, 0], msg="test_case4 not passed")


if __name__ == '__main__':
    unittest.main()
