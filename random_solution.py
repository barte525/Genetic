import numpy as np


def generate_random_solution(rows, columns, number_of_machines):
    array = np.random.choice(range(number_of_machines-rows*columns, number_of_machines), rows*columns, replace=False)
    return np.asarray(array).reshape(rows, columns)