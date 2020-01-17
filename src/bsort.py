"""
Bubble sort function.
"""


def bubble_sort(nlist):
    for pass_num in range(len(nlist)-1, 0, -1):
        for i in range(pass_num):
            if nlist[i] > nlist[i+1]:
                nlist[i], nlist[i+1] = nlist[i+1], nlist[i]
