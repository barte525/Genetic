import numpy as np

class Objective:
    def __init__(self, cost_flow_arr, number_of_machines):
        self.cost_flow_arr = cost_flow_arr
        self.number_of_machines = number_of_machines

    def evaluate_solution(self, solution_array):
        coordinates_array = self.find_coordinates(solution_array)
        distance_arr = self.find_distance_arr(coordinates_array)
        result_arr = distance_arr * self.cost_flow_arr
        return result_arr.sum()

    def find_distance_arr(self, coordinates_array):
        distance_arr = np.zeros(shape=(self.number_of_machines, self.number_of_machines), dtype=int)
        for x in range(self.number_of_machines):
            for y in range(self.number_of_machines):
                distance_arr[x][y] = abs(coordinates_array[0, x] - coordinates_array[0, y]) + abs(coordinates_array[1, x]-
                                                              coordinates_array[1, y])
        return distance_arr

    def find_coordinates(self, solution_array):
        result = np.zeros(shape=(2, self.number_of_machines), dtype=int)
        for i in range(self.number_of_machines):
            coord = np.where(solution_array == i)
            result[0, i] = coord[0]
            result[1, i] = coord[1]
        return result

    @staticmethod
    def count_distance(x0, x1, y0, y1):
        return abs(x0 - x1) + abs(y0 - y1)




