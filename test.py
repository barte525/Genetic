from data import Data
from solution import Objective
import numpy as np
from algorythm import Genetic


class Test:
    def __init__(self, matrix_type):
        self.matrix_type = matrix_type
        if matrix_type == 'easy':
            self.population = [
                np.array([[0, 5, 2],
                          [8, 1, 6],
                          [4, 7, 3]]),
                np.array([[4, 1, 3],
                         [2, 5, 6],
                         [8, 7, 0]]),
                np.array([[3, 8, 2],
                         [4, 0, 6],
                         [1, 5, 7]]),
                np.array([[3, 0, 6],
                         [2, 7, 8],
                         [5, 4, 1]]),
                np.array([[3, 1, 4],
                         [5, 2, 6],
                         [7, 0, 8]])
            ]
            self.cost_flow_arr = Data('data/easy_cost.json', 'data/easy_flow.json', 9).cost_flow_array
            self.obj = Objective(self.cost_flow_arr, 9)
            self.machines = 9
            self.rows = 3
            self.columns = 3
        if matrix_type == 'flat':
            self.population = [np.array([[2,  1,  4,  8,  9,  5,  0,  7,  6,  3, 10, 11]]),
                               np.array([[7,  6,  0,  3,  1, 11,  8,  5,  9, 10,  4,  2]]),
                               np.array([[9,  5,  3, 10,  4, 11,  2,  0,  7,  1,  6,  8]]),
                               np.array([[4, 11,  7,  0,  8,  6,  3,  9,  2,  5,  1, 10]]),
                               np.array([[11,  8,  1,  3, 10,  9,  7,  0,  2,  4,  5,  6]])]
            self.cost_flow_arr = Data('data/flat_cost.json', 'data/flat_flow.json', 12).cost_flow_array
            self.obj = Objective(self.cost_flow_arr, 12)
            self.machines = 12
            self.rows = 1
            self.columns = 12
        if matrix_type == 'hard':
            self.population = [
                np.array([[20,  8,  9, 11, -1, 12],
                         [ 1, -2,  6, 23, -3, 21],
                         [15, 19, 22, 17, 18,  3],
                         [-6, 16, 13,  7,  5, -5],
                         [10,  0, 14,  2,  4, -4]]),
                np.array([[-2, 19,  4,  8,  7, -4],
                         [22, -5,  6, 11, 14, 16],
                         [ 1, 21, 23,  0,  2,  3],
                         [-1, 17,  5, -3, -6, 10],
                         [13, 18, 15, 12,  9, 20]]),
                np.array([[-3,  7, 23, 17, 18, -4],
                         [15, 12, 20,  8, 14,  6],
                         [16,  9, -1,  0,  4, 22],
                         [ 1,  2, 21, -5, 10, -6],
                         [11,  3, -2,  5, 19, 13]]),
                np.array([[18, -1, -6, 13, 21, 15],
                         [14, 17,  3, 16, -5, 19],
                         [11, 20, 22, -2, -3, 12],
                         [10,  2,  1,  5,  6, -4],
                         [ 9,  0,  4,  7, 23,  8]]),
                np.array([[21,  4, -5, -1, 16,  9],
                         [ 5, 17, -4, 23,  7,  2],
                         [19, 20, -2,  1, 10, 18],
                         [-3,  0, 13, 22, 14, -6],
                         [ 3,  8, 12, 15,  6, 11]])]
            self.cost_flow_arr = Data('data/hard_cost.json', 'data/hard_flow.json', 24).cost_flow_array
            self.obj = Objective(self.cost_flow_arr, 24)
            self.machines = 24
            self.rows = 5
            self.columns = 6

    def roulette_test(self, loops, parameter):
        print('Roulette for', self.matrix_type, 'and parameter', str(parameter) + ':')
        costs = [self.obj.evaluate_solution(self.population[i]) for i in range(5)]
        print('costs: ', costs)
        gen = Genetic(self.cost_flow_arr, self.machines, self.population, self.rows, self.columns)
        number = [0, 0, 0, 0, 0]
        for i in range(loops):
            _, idx, p = gen.roulette(parameter)
            for i in idx:
                number[i] += 1
        print('p: ', p)
        print('next generation from', loops, 'loops: ', number)
        print('')
        print('x' * 100)
        print('')

    def tournament_test(self, loops, tournament_size):
        print('Tournament for', self.matrix_type, 'and tournament size', str(tournament_size) + ':')
        costs = [self.obj.evaluate_solution(self.population[i]) for i in range(5)]
        print('costs: ', costs)
        gen = Genetic(self.cost_flow_arr, self.machines, self.population, self.rows, self.columns)
        number = [0, 0, 0, 0, 0]
        for i in range(loops):
            _, idx = gen.tournament(tournament_size)
            for i in idx:
                number[i] += 1
        print('next generation from', loops, 'loops: ', number)
        print('')
        print('x' * 100)
        print('')

    def crossover_test(self, n):
        print('Crossover for', self.matrix_type, 'and number of genes changes', str(n) + ':')
        population = [self.population[0], self.population[1]]
        gen = Genetic(self.cost_flow_arr, self.machines, population, self.rows, self.columns)
        gen.crossover(n, 1)
        print('parent1:\n', population[0])
        print('parent2:\n', population[1])
        print('child1:\n', gen.population[0])
        print('child2:\n', gen.population[1])
        print('')
        print('x' * 100)
        print('')
        return gen.population[0], gen.population[1]

    @staticmethod
    def check_hard_matrix(matrix):
        is_ok = True
        for i in range(24):
            if i not in matrix:
                is_ok = False
        negatives = np.where(matrix < 0)
        if len(negatives[0]) != 6:
            is_ok = False
        return is_ok

    def mutate_test(self, p):
        print('Mutation for', self.matrix_type, 'and probability:', str(p) + ':')
        population = [self.population[0]]
        gen = Genetic(self.cost_flow_arr, self.machines, population, self.rows, self.columns)
        print('before mutation:\n', population[0])
        gen.mutate(p)
        print('after mutation:\n', gen.population[0])
        print('')
        print('x' * 100)
        print('')