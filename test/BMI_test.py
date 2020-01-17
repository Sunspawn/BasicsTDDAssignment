import unittest
from src.BMI import BMI


class BMI_Test(unittest.TestCase):
    def test_height(self):
        # stub
        stub1 = 178
        stub2 = 0
        stub3 = -50

        # assume
        expected1 = 1.78
        expected2 = -1
        expected3 = -1

        # action
        result1 = BMI.check_height(stub1)
        result2 = BMI.check_height(stub2)
        result3 = BMI.check_height(stub3)

        # expect/assert
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)

    def test_weight(self):
        # stub
        stub1 = 178
        stub2 = 400
        stub3 = -50
        stub4 = 0

        # assume
        expected1 = 178
        expected2 = 400
        expected3 = 0
        expected4 = 0

        # action
        result1 = BMI.check_weight(stub1)
        result2 = BMI.check_weight(stub2)
        result3 = BMI.check_weight(stub3)
        result4 = BMI.check_weight(stub4)

        # expect/assert
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)
        self.assertEqual(result4, expected4)
        
    def test_BMI(self):
        # stub height
        height_stub1 = 1.5
        height_stub2 = 1.65
        height_stub3 = 1.8
        height_stub4 = -1
        height_stub5 = 0.9
        
        # stub weight
        weight_stub1 = 40
        weight_stub2 = 60
        weight_stub3 = 80
        weight_stub4 = 0
        weight_stub5 = 0

        # assume
        expected1 = 17.77777777777778
        expected2 = 22.03856749311295
        expected3 = 24.691358024691358
        expected4 = 0
        expected5 = 0

        # action
        result1 = BMI.check_BMI(weight_stub1, height_stub1)
        result2 = BMI.check_BMI(weight_stub2, height_stub2)
        result3 = BMI.check_BMI(weight_stub3, height_stub3)
        result4 = BMI.check_BMI(weight_stub4, height_stub3)
        result5 = BMI.check_BMI(weight_stub5, height_stub5)

        # expect/assert
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3) 
        self.assertEqual(result4, expected4)
        self.assertEqual(result5, expected5)

    def get_tests(self):
        return self.test_height, self.test_weight, self.test_BMI


if __name__ == '__main__':
    unittest.main()
