from test_folder.bsort_test import bsort_tester

testers = bsort_tester(),

for tester in testers:
    try:
        tester.run()
    except tester.failureException as e:
        print("Test failed:", e)
