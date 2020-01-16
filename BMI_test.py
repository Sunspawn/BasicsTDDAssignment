import unittest
from BMI import BMI

class BMI_Test(unittest.TestCase):
    def test_height(self):
        # stub
        stub1 = 178
        stub2 = 0
        stub3 = -50

        # assume
        expected1 = 178
        expected2 = 1
        expected3 = 1

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
        expected2 = 1
        expected3 = 1
        expected4 = 1

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
        # stub height weight
        height_stub1 = 180
        height_stub2 = 0
        height_stub3 = -50
        weight_stub1 = 60
        weight_stub2 = 1000
        weight_stub3 = -5

        # assume
        expected1 = 178
        expected2 = 1
        expected3 = 1

        # action
        result1 = BMI.check_BMI(stub1)
        result2 = BMI.check_BMI(stub2)
        result3 = BMI.check_BMI(stub3)

        # expect/assert
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3) 


if __name__ == '__main__':
    unittest.main()
