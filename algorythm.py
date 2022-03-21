from solution import Objective
import random
import sys
import numpy as np


class Genetic:
    NUMBER_GREATER_THEN_AMOUNT_OF_MACHINES = 999999999

    def __init__(self, cost_flow_arr, number_of_machines, population, rows, columns):
        self.population_obj = np.array([])
        self.population = population
        self.obj = Objective(cost_flow_arr, number_of_machines)
        self.population_len = len(population)
        self.evaluate()
        self.rows = rows
        self.columns = columns

    def evaluate(self):
        population_obj = []
        for subject in self.population:
            population_obj.append(self.obj.evaluate_solution(subject))
        self.population_obj = np.array(population_obj)
        self.population_len = len(self.population_obj)

    def tournament(self, n):
        result = []
        result_idx = []
        while len(result) < self.population_len:
            random_idx_list = random.sample(range(self.population_len), n)
            min_obj = sys.maxsize
            winner_idx = -1
            for idx in random_idx_list:
                objective = self.population_obj[idx]
                if objective < min_obj:
                    min_obj = objective
                    winner_idx = idx
            result.append(self.population[winner_idx])
            result_idx.append(winner_idx)
        self.population = result
        return result, result_idx

    def roulette(self, n):
        probability = (self.population_obj - max(self.population_obj) - min(self.population_obj)/n) * -1
        if n > 1:
            probability = probability * probability * probability * probability * probability * probability
        probability_sum = probability.sum()
        probability = probability/probability_sum
        full_idx_list = np.array(range(self.population_len))
        random_idx_list = np.random.choice(full_idx_list, self.population_len, p=probability)
        self.population = [self.population[i] for i in random_idx_list]
        return self.population, random_idx_list, probability

    def crossover(self, n, p):
        new_population = []
        for i in range(1, self.population_len, 2):
            gen_change_row = random.randint(0, self.rows - 1)
            gen_change_column = random.randint(0, self.columns - 1)
            new_population.append(np.copy(self.population[i-1]))
            new_population.append(np.copy(self.population[i]))
            if p >= random.random():
                self.swap_with_repair(gen_change_column, gen_change_row, i, new_population)
                for j in range(n-1):
                    gen_change_column, gen_change_row = self.get_neighbor(gen_change_column, gen_change_row, False)
                    self.swap_with_repair(gen_change_column, gen_change_row, i, new_population)
        self.population = new_population

    def get_neighbor(self, gen_change_column, gen_change_row, back_flag):
        if gen_change_column < self.columns - 1:
            gen_change_column = gen_change_column + 1
        elif gen_change_row < self.rows - 1:
            gen_change_row = gen_change_row + 1
            gen_change_column = 0
        elif back_flag:
            gen_change_column = gen_change_column - 1
        else:
            gen_change_row = 0
            gen_change_column = 0
        return gen_change_column, gen_change_row

    def swap_with_repair(self, gen_change_column, gen_change_row, i, new_population):
        value1 = new_population[i-1][gen_change_row][gen_change_column]
        value2 = new_population[i][gen_change_row][gen_change_column]
        new_population[i - 1][gen_change_row][gen_change_column] = Genetic.NUMBER_GREATER_THEN_AMOUNT_OF_MACHINES
        new_population[i][gen_change_row][gen_change_column] = Genetic.NUMBER_GREATER_THEN_AMOUNT_OF_MACHINES
        self.repair(i-1, value1, value2, new_population)
        new_population[i - 1][gen_change_row][gen_change_column] = value2
        self.repair(i, value2, value1, new_population)
        new_population[i][gen_change_row][gen_change_column] = value1

    @staticmethod
    def repair(idx, value1, value2, new_population):
        if value2 in new_population[idx] and value2 >= 0:
            row, column = np.where(new_population[idx] == value2)
            new_population[idx][row[0]][column[0]] = value1
        if value2 < 0 <= value1:
            row, column = np.where(new_population[idx] < 0)
            new_population[idx][row[0]][column[0]] = value1

    def mutate(self, p):
        for arr in self.population:
            for x in range(self.rows * self.columns):
                if p >= random.random():
                    random_row_1 = random.randint(0, self.rows - 1)
                    random_column_1 = random.randint(0, self.columns - 1)
                    random_column_2, random_row_2 = self.get_neighbor(random_column_1, random_row_1, True)
                    self.swap(arr, random_column_1, random_column_2, random_row_1, random_row_2)

    def get_square(self, random_row_1, random_column_1):
        if random_row_1 < self.rows - 1 and random_column_1 < self.columns - 1:
            return random_row_1, random_column_1 + 1, random_row_1 + 1, random_column_1, random_row_1 + 1,\
                   random_column_1 + 1
        elif random_column_1 < self.columns - 1:
            return random_row_1, random_column_1 + 1, random_row_1 - 1, random_column_1 + 1, random_row_1 - 1,\
                   random_column_1
        elif random_row_1 < self.rows - 1:
            return random_row_1, random_column_1 - 1, random_row_1 + 1, random_column_1, random_row_1 + 1,\
                   random_column_1 - 1
        else:
            return random_row_1, random_column_1 - 1, random_row_1 - 1, random_column_1, random_row_1 - 1, \
                   random_column_1 - 1

    @staticmethod
    def swap(arr, random_column_1, random_column_2, random_row_1, random_row_2):
        value_to_swap = arr[random_row_1][random_column_1]
        arr[random_row_1][random_column_1] = arr[random_row_2][random_column_2]
        arr[random_row_2][random_column_2] = value_to_swap







