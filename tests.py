from test_folder.BMI_test import BMI_Test

testers = BMI_Test(),

for tester in testers:
    try:
        tester.run()
    except tester.failureException as e:
        print("Test failed:", e)
