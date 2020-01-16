
class BMI:
    
    @staticmethod
    def check_height(num):
        if num == 0:
            return 1
        
        if num < 0:
            return 1
        
        if 1 < num < 300:
            return num

    @staticmethod
    def check_weight(num):
        if num == 0:
            return 1
        
        if num < 0:
            return 1
        
        if num >300:
            return 1
        
        if 1 < num < 300:
            return num
        
    @staticmethod
    def check_BMI(weight,height):
        test_BMI = weight/(height**2)
        if test_BMI == 1:
            print('wrong parameters try again')
            return test_BMI
        
        if 0 < test_BMI< 15:
            print('Very severely underweight ')
            return test_BMI

        if 15 <= test_BMI < 16:
            print('Severely underweight Range')
            return test_BMI
        
        if 16 <= test_BMI < 18.5:
            print('Underweight')
            return test_BMI
        
        if 18.5 <= test_BMI < 25:
            print('Normal (healthy weight)')
            return test_BMI
        
        if 25 <= test_BMI < 30:
            print('Overweigh ')
            return test_BMI
        
        if 30 <= test_BMI < 35:
            print('Obese Class I (Moderately obese)')
            return test_BMI
        
        if 35 <= test_BMI < 40:
            print('Obese Class II (Severely obese)')
            return test_BMI
        
        if 40 <= test_BMI < 45:
            print('Obese Class III (Very severely obese)')
            return test_BMI
        
        if 45 <= test_BMI < 50:
            print('Obese Class IV (Morbidly obese)')
            return test_BMI
        
        if 50 <= test_BMI < 60:
            print('Obese Class V (Super obese)')
            return test_BMI
        
        if 60 <= test_BMI:
            print('Obese Class VI (Hyper obese)')
            return test_BMI
