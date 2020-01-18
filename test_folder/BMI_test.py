import unittest
import sys  # bandaid fix
sys.path.append("./..")  # bandaid fix
from src.BMI import BMI


class BMI_Test(unittest.TestCase):
    def test_height(self):
        # stub
        stub1 = 178
        stub2 = 0
        stub3 = -50

        # assume
        expected1 = 1.78
        expected2 = BMI.height_error + BMI.zero_error
        expected3 = BMI.height_error + BMI.negative_error

        # action
        result1 = BMI.check_height(stub1)
        with self.assertRaises(ValueError) as result2:
            BMI.check_height(stub2)
        result2 = result2.exception.args[0]
        with self.assertRaises(ValueError) as result3:
            BMI.check_height(stub3)
        result3 = result3.exception.args[0]

        # expect/assert
        self.assertEqual(result1, expected1, "height 1")
        self.assertEqual(result2, expected2, "height 2")
        self.assertEqual(result3, expected3, "height 3")

    def test_weight(self):
        # stub
        stub1 = 178
        stub2 = 400
        stub3 = -50
        stub4 = 0

        # assume
        expected1 = 178
        expected2 = 400
        expected3 = BMI.weight_error + BMI.negative_error
        expected4 = BMI.weight_error + BMI.zero_error

        # action
        result1 = BMI.check_weight(stub1)
        result2 = BMI.check_weight(stub2)
        with self.assertRaises(Exception) as result3:
            BMI.check_weight(stub3)
        result3 = result3.exception.args[0]
        with self.assertRaises(Exception) as result4:
            BMI.check_weight(stub4)
        result4 = result4.exception.args[0]

        # expect/assert
        self.assertEqual(result1, expected1, "weight 1")
        self.assertEqual(result2, expected2, "weight 2")
        self.assertEqual(result3, expected3, "weight 3")
        self.assertEqual(result4, expected4, "weight 4")
        
    def test_BMI(self):
        # stub height
        height_stub1 = 150
        height_stub2 = 165
        height_stub3 = 180
        
        # stub weight
        weight_stub1 = 40
        weight_stub2 = 60
        weight_stub3 = 80

        # assume
        expected1 = 17.77777777777778
        expected2 = 22.03856749311295
        expected3 = 24.691358024691358

        # action
        result1 = BMI.check_BMI(weight_stub1, height_stub1)
        result2 = BMI.check_BMI(weight_stub2, height_stub2)
        result3 = BMI.check_BMI(weight_stub3, height_stub3)

        # expect/assert
        self.assertEqual(result1, expected1, "bmi 1")
        self.assertEqual(result2, expected2, "bmi 2")
        self.assertEqual(result3, expected3, "bmi 3")

    def run(self):
        self.test_height()
        self.test_weight()
        self.test_BMI()


if __name__ == '__main__':
    unittest.main()
