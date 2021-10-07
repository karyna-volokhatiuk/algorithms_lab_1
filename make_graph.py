import matplotlib.pyplot as plt
import json

size_from = 7
size_to = 15

experiments = ["random_5_trials", "ordered", "reverse_ordered", "1_2_3_elements_only"]

def build_graph(mode = "time", exp = experiments[1]):
    sizes_of_data = [str(i) for i in range(size_from, size_to+1)]
    sorts = ["insertion_sort", "selection_sort", "merge_sort", "shell_sort"]
    
    graph_color = {"insertion_sort": "r", "selection_sort": "g", "merge_sort": "b", "shell_sort": "y"}

    names_of_exp = {"random_5_trials": "Random list", "ordered": "Sorted list", "reverse_ordered": "Sorted in reverse order", "1_2_3_elements_only": "1, 2, 3 elements only"}

    modes = {"time": "Time in nanoseconds", "num_of_comparisons": "Number of comparisons"}
    

    with open('results_in_ns.json', 'r') as exp_file:
        data = json.load(exp_file)

    graph_data = {}

    #print(data)

    for name_of_sort in sorts:
        graph_data[name_of_sort] = []


    for size in sizes_of_data:
        for name_of_sort in sorts:
            #print(type(data), exp, size, name_of_sort, mode)
            get_data = data[exp][size][name_of_sort][mode]
            #print(get_data)
            graph_data[name_of_sort].append(sum(get_data)/len(get_data))
    

    
    for name_of_sort in sorts:
        plt.plot(sizes_of_data, graph_data[name_of_sort], color=graph_color[name_of_sort], label=name_of_sort)
            
    plt.yscale("log")
    plt.xlabel("Array size")
    plt.ylabel(modes[mode])
    plt.title(names_of_exp[exp])
    plt.legend()
    plt.savefig(exp + "_" + mode + ".png")

    plt.show()



build_graph()