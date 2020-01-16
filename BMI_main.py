from src.BMI import BMI


print('enter the test values')
height = int(input('Enter height value: '))
height = BMI.check_height(height)
print('height after check_height func:', height)
weight = int(input('Enter weight value: '))
weight = BMI.check_weight(weight)
print('weight after check_weight func:', weight)
    
test_BMI = BMI.check_BMI(weight,height)
