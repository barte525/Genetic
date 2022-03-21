from data import Data
from solution import Objective
import numpy as np
from algorythm import Genetic
import unittest


class Test(unittest.TestCase):
    population_e = [
        np.array([[0, 5, 2],
                  [8, 1, 6],
                  [4, 7, 3]]), #1
        np.array([[4, 1, 3],
                 [2, 5, 6],
                 [8, 7, 0]]), #3
        np.array([[3, 8, 2],
                 [4, 0, 6],
                 [1, 5, 7]]), #5
        np.array([[3, 0, 6],
                 [2, 7, 8],
                 [5, 4, 1]]), #2
        np.array([[3, 1, 4],
                 [5, 2, 6],
                 [7, 0, 8]]) #4
    ]
    cost_flow_arr_e = Data('data/easy_cost.json', 'data/easy_flow.json', 9).cost_flow_array
    obj_e = Objective(cost_flow_arr_e, 9)
    machines_e = 9
    rows_e = 3
    columns_e = 3

    population_f = [np.array([[2,  1,  4,  8,  9,  5,  0,  7,  6,  3, 10, 11]]),
                       np.array([[7,  6,  0,  3,  1, 11,  8,  5,  9, 10,  4,  2]]),
                       np.array([[9,  5,  3, 10,  4, 11,  2,  0,  7,  1,  6,  8]]),
                       np.array([[4, 11,  7,  0,  8,  6,  3,  9,  2,  5,  1, 10]]),
                       np.array([[11,  8,  1,  3, 10,  9,  7,  0,  2,  4,  5,  6]])]
    cost_flow_arr_f = Data('data/flat_cost.json', 'data/flat_flow.json', 12).cost_flow_array
    obj_f = Objective(cost_flow_arr_f, 12)
    machines_f = 12
    rows_f = 1
    columns_f = 12

    population_h = [
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
    cost_flow_arr_h = Data('data/hard_cost.json', 'data/hard_flow.json', 24).cost_flow_array
    obj_h = Objective(cost_flow_arr_f, 24)
    machines_h = 24
    rows_h = 5
    columns_h = 6

    @staticmethod
    def roulette_test(gen):
        number = [0, 0, 0, 0, 0]
        for i in range(1, 300):
            _, idx, _ = gen.roulette(1000)
            for i in idx:
                number[i] += 1
        return number

    def test_roulette_easy(self):
        gen = Genetic(self.cost_flow_arr_e, self.machines_e, self.population_e, self.rows_e, self.columns_e)
        result = self.roulette_test(gen)
        assert result.index(max(result)) == 0
        assert result.index(min(result)) == 2

    def test_roulette_flat(self):
        gen = Genetic(self.cost_flow_arr_f, self.machines_f, self.population_f, self.rows_f, self.columns_f)
        result = self.roulette_test(gen)
        assert result.index(max(result)) == 3
        assert result.index(min(result)) == 2

    def test_roulette_hard(self):
        gen = Genetic(self.cost_flow_arr_h, self.machines_h, self.population_h, self.rows_h, self.columns_h)
        result = self.roulette_test(gen)
        assert result.index(max(result)) == 2
        assert result.index(min(result)) == 3

    @staticmethod
    def tournament_test(gen, size):
        number = [0, 0, 0, 0, 0]
        for i in range(1, 101):
            _, idx = gen.tournament(size)
            for i in idx:
                number[i] += 1
        return number

    def test_tournament_easy(self):
        gen = Genetic(self.cost_flow_arr_e, self.machines_e, self.population_e, self.rows_e, self.columns_e)
        result = self.tournament_test(gen, 2)
        result.sort()
        assert result[-1] + result[-2] > sum(result) / (len(result) - 1)
        assert min(result) == 0

    def test_tournament_flat(self):
        gen = Genetic(self.cost_flow_arr_f, self.machines_f, self.population_f, self.rows_f, self.columns_f)
        result = self.tournament_test(gen, 2)
        result.sort()
        assert result[-1] + result[-2] > sum(result) / (len(result) - 1)
        assert min(result) == 0

    def test_tournament_hard(self):
        gen = Genetic(self.cost_flow_arr_h, self.machines_h, self.population_h, self.rows_h, self.columns_h)
        result = self.tournament_test(gen, 2)
        result.sort()
        assert result[-1] + result[-2] > sum(result) / (len(result) - 1)
        assert min(result) == 0

    def check_hard_matrix(self, matrix):
        is_ok = True
        for i in range(self.machines_h):
            if i not in matrix:
                is_ok = False
        negatives = np.where(matrix < 0)
        if len(negatives[0]) != self.rows_h * self.columns_h - self.machines_h:
            is_ok = False
        return is_ok

    def test_crossover_hard(self):
        for x in range(10):
            gen = Genetic(self.cost_flow_arr_h, self.machines_h, self.population_h, self.rows_h, self.columns_h)
            gen.crossover(5, 1)
            for i in range(len(self.population_h) - 1):
                assert self.check_hard_matrix(gen.population[i])

    def test_mutate_hard(self):
        pop = [np.copy(self.population_h[0])]
        gen = Genetic(self.cost_flow_arr_h, self.machines_h, pop, self.rows_h, self.columns_h)
        pop_before = np.copy(gen.population[0])
        gen.mutate(1)
        comparison = pop_before == gen.population[0]
        assert not comparison.all()




