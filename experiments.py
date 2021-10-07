from random import shuffle, randint

from time import time, time_ns

from copy import deepcopy

import json

from insertion_sort import insertion_sort
from selection_sort import selection_sort
from merge_sort import merge_sort
from shell_sort import shell_sort

size_from = 7
size_to = 15
file_name = "results_in_ns.json"

def generate_ordered_array(power):
    arr = []
    for i in range(pow(2, power)):
        arr.append(i)
    return arr

def generate_reverse_ordered_array(power):
    arr = []
    for i in range(pow(2, power)-1, -1, -1):
        arr.append(i)
    return arr

def generate_random_array(power):
    arr = generate_ordered_array(power)
    shuffle(arr)
    return arr

def generate_1_2_3_elements_array(power):
    arr = []
    for i in range(pow(2, power)):
        arr.append(randint(1, 3))
    return arr

def main():
    experiments = {"random_5_trials": generate_random_array, "ordered": generate_ordered_array, 
            "reverse_ordered": generate_reverse_ordered_array, "1_2_3_elements_only": generate_1_2_3_elements_array}

    sorts = [insertion_sort, selection_sort, merge_sort, shell_sort]

    data = {}    
    for exp in experiments:
        exp_data = {}
        for size in range(size_from, size_to+1):
            size_data = {}
            for sort in sorts:
                size_data[sort.__name__] = {"num_of_comparisons": [], "time": []}
            exp_data[size] = size_data
        data[exp] = exp_data
            

    def make_experiment(exp, size, arr):
        for sort in sorts:
            # print("arr1")
            # print(arr)
            # print("\n")

            start_time = time_ns()
            num_compare = sort(arr.copy())
            time_res = time_ns()-start_time

            # print("arr2")
            # print(arr)
            # print("\n")

            data[exp][size][sort.__name__]["num_of_comparisons"].append(num_compare)
            data[exp][size][sort.__name__]["time"].append(time_res)


    for exp in experiments:

        for size in range(size_from, size_to+1):

            arr = experiments[exp](size)

            if exp == "1_2_3_elements_only":
                for _ in range(1, 4):
                    make_experiment(exp, size, arr)
                    shuffle(arr)
                    
            elif exp == "random_5_trials":
                for _ in range(1, 6):
                    make_experiment(exp, size, arr)
                    shuffle(arr)
            else:
                make_experiment(exp, size, arr)

    with open(file_name, 'w') as json_file:
        obj = json.dumps(data, indent = 2)
        json_file.write(obj)

main()
