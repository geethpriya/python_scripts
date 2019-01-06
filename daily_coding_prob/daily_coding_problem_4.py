"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words,
find the lowest positive integer that does not exist in the array. The array can contain duplicates and
negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

import unittest

'''List for testing'''
test_list1 = [3, 4, -1, 1]
test_list2 = [1, 2, 0]
test_list3 = [2, 4, -8, 10, 15, 0, 0, -1, 1]
test_list4 = [0, 0, 0]


def find_first_missing_pos_num(list_num):
    """
    :param list_num:
    :return: first missing positive integer
    """
    pos_num = -1
    for num in sorted(list_num):
        if num < 0:
            continue
        if pos_num < 0:
            pos_num = num
            continue
        if num == pos_num + 1 or num == pos_num:
            pos_num = num
            continue
        else:
            break
    return pos_num+1


class MyTest(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(find_first_missing_pos_num(test_list1), 2, msg="test_case1 not passed")

    def test_case2(self):
        self.assertEqual(find_first_missing_pos_num(test_list2), 3, msg="test_case2 not passed")

    def test_case3(self):
        self.assertEqual(find_first_missing_pos_num(test_list3), 3, msg="test_case3 not passed")

    def test_case4(self):
        self.assertEqual(find_first_missing_pos_num(test_list4), 1, msg="test_case4 not passed")


if __name__ == '__main__':
    unittest.main()
