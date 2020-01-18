import unittest
import sys  # bandaid fix
sys.path.append("./..")  # bandaid fix
from src.bsort import bubble_sort


class bsort_tester(unittest.TestCase):
    def test_logic(self):
        # stub
        stub1 = [1, 2, 3]  # sanity check
        stub2 = [3, 1, 2]  # natural numbers
        stub3 = [-1, -3, 5, 0]  # negative numbers
        stub4 = [0.1, 0.15, 4.9, 0, 100.1, 100]  # fractions

        # assume
        assume1 = [1, 2, 3]
        assume2 = [1, 2, 3]
        assume3 = [-3, -1, 0, 5]
        assume4 = [0, 0.1, 0.15, 4.9, 100, 100.1]

        # action
        bubble_sort(stub1)
        bubble_sort(stub2)
        bubble_sort(stub3)
        bubble_sort(stub4)

        # expect/assert
        self.assertListEqual(stub1, assume1, "logic 1")
        self.assertListEqual(stub2, assume2, "logic 2")
        self.assertListEqual(stub3, assume3, "logic 3")
        self.assertListEqual(stub4, assume4, "logic 4")

    def test_elem(self):
        # stub
        stub1 = [1, 2, 3]  # sanity check
        stub2 = [-1, -3, 5, 0, -1, -3]  # loss of elements due to repetition

        # assume
        assume1 = [1, 2, 3]
        assume2 = [-3, -3, -1, -1, 0, 5]

        # action
        bubble_sort(stub1)
        bubble_sort(stub2)

        # expect/assert
        self.assertCountEqual(stub1, assume1, "elem 1")
        self.assertCountEqual(stub2, assume2, "elem 2")

    def run(self):
        self.test_elem()
        self.test_logic()


if __name__ == '__main__':
    unittest.main()
