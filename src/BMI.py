"""
num1 = 40/1.5**2
print('40/1.5**2=', num1)
num1 = 60/1.65**2
print('60/1.65**22=', num1)
num1 = 80/1.8**2
print('80/1.8**2=', num1)
num1 = 0/1.8**2
print('0/1.8**2=', num1)
num1 =1/1**2
print('1/1**2=', num1)
num1 =-1/(-1)**2
print('-1/(-1)**2=', num1)
num1 = -1/1**2
print('-1/1**2=', num1)
num1 = 1/(-1)**2
print('1/(-1)**2=', num1)
num1 = -1/0.9**2
print('-1/0.9**2=', num1)
"""


class BMI:
    height_error = "Height error: "
    weight_error = "Weight error: "
    negative_error = "Negative value."
    zero_error = "Zero value."
    
    @staticmethod
    def check_height(num):
        if num == 0:
            raise ValueError(BMI.height_error + BMI.zero_error)

        if num < 0:
            raise ValueError(BMI.height_error + BMI.negative_error)
        
        if 0 < num:
            return num/100

    @staticmethod
    def check_weight(num):
        if num == 0:
            raise ValueError(BMI.weight_error + BMI.zero_error)

        if num < 0:
            raise ValueError(BMI.weight_error + BMI.negative_error)
        
        if 0 < num:
            return num
        
    @staticmethod
    def check_BMI(weight, height):
        test_BMI = BMI.check_weight(weight)/BMI.check_height(height)**2
        
        if 0 < test_BMI < 15:
            print('Very severely underweight', test_BMI)
            return test_BMI

        if 15 <= test_BMI < 16:
            print('Severely underweight', test_BMI)
            return test_BMI
        
        if 16 <= test_BMI < 18.5:
            print('Underweight', test_BMI)
            return test_BMI
        
        if 18.5 <= test_BMI < 25:
            print('Normal (healthy weight)', test_BMI)
            return test_BMI
        
        if 25 <= test_BMI < 30:
            print('Overweight', test_BMI)
            return test_BMI
        
        if 30 <= test_BMI < 35:
            print('Obese Class I (Moderately obese)', test_BMI)
            return test_BMI
        
        if 35 <= test_BMI < 40:
            print('Obese Class II (Severely obese)', test_BMI)
            return test_BMI
        
        if 40 <= test_BMI < 45:
            print('Obese Class III (Very severely obese)', test_BMI)
            return test_BMI
        
        if 45 <= test_BMI < 50:
            print('Obese Class IV (Morbidly obese)', test_BMI)
            return test_BMI
        
        if 50 <= test_BMI < 60:
            print('Obese Class V (Super obese)', test_BMI)
            return test_BMI
        
        if 60 <= test_BMI:
            print('Obese Class VI (Hyper obese)', test_BMI)
            return test_BMI
