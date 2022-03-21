from data import Data
import numpy as np
from algorythm import Genetic
from random_solution import generate_random_solution
import matplotlib.pyplot as plt
from solution import Objective
import statistics

class Simulation:
    def __init__(self, population_size, number_of_generations, tournament_selection, selection_parameter,
                 genes_to_cross, crossover_probability, mutation_probability, case):
        self.population_size = population_size
        self.number_of_generations = number_of_generations
        self.tournament_selection = tournament_selection
        self.selection_parameter = selection_parameter
        self.genes_to_cross = genes_to_cross
        self.mutation_probability = mutation_probability
        self.crossover_probability = crossover_probability
        self.best = []
        self.worst = []
        self.avg = []
        if case == 'easy':
            self.cost_flow_arr = Data('data/easy_cost.json', 'data/easy_flow.json', 9).cost_flow_array
            self.machines = 9
            self.rows = 3
            self.columns = 3
        if case == 'flat':
            self.cost_flow_arr = Data('data/flat_cost.json', 'data/flat_flow.json', 12).cost_flow_array
            self.machines = 12
            self.rows = 1
            self.columns = 12
        if case == 'hard':
            self.cost_flow_arr = Data('data/hard_cost.json', 'data/hard_flow.json', 24).cost_flow_array
            self.machines = 24
            self.rows = 5
            self.columns = 6

    def run_simulation(self, plot):
        population = []
        print(self.rows, self.columns, self.machines)
        for i in range(self.population_size):
            population.append(generate_random_solution(self.rows, self.columns, self.machines))
        generate_random_solution(self.rows, self.columns, self.machines)
        gen = Genetic(self.cost_flow_arr, self.machines, population, self.rows, self.columns)
        self.append_stat(gen)
        for i in range(1, self.number_of_generations):
            if self.tournament_selection:
                gen.tournament(self.selection_parameter)
            else:
                gen.roulette(self.selection_parameter)
            gen.crossover(self.genes_to_cross, self.crossover_probability)
            gen.mutate(self.mutation_probability)
            gen.evaluate()
            self.append_stat(gen)
        print("All Best:", min(self.best))
        if plot:
            self.draw_plot()
        return min(self.best)

    def append_stat(self, gen):
        self.best.append(min(gen.population_obj))
        self.worst.append(max(gen.population_obj))
        self.avg.append(self.count_avr(gen.population_obj))

    def draw_plot(self):
        x = range(self.number_of_generations)
        plt.plot(x, self.best, label="best")
        plt.plot(x, self.worst, label="worst")
        plt.plot(x, self.avg, label="avg")
        plt.legend()
        plt.show()

    def count_avr(self, population_obj):
        return round(population_obj.sum()/self.population_size, 1)

    def run_random(self):
        result = []
        obj = Objective(self.cost_flow_arr, self.machines)
        for x in range(10):
            all_v = []
            for x in range(self.number_of_generations*self.population_size):
                all_v.append(obj.evaluate_solution(generate_random_solution(self.rows, self.columns, self.machines)))
            result.append(min(all_v))
        print("rmin", min(result), "rmax", max(result), "ravg", sum(result) / len(result), "rstd", statistics.stdev(result))



