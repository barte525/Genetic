from test import Test
from simulation import Simulation
import statistics
from random_solution import generate_random_solution
from data import Data

def run_ten(sim):
    result = []
    for x in range(10):
        result.append(sim.run_simulation(False))
    print("min", min(result), "max",  max(result), "avg", sum(result)/len(result), "std", statistics.stdev(result))



if __name__ == '__main__':
    # loops = 1000
    # roulette_power = 5
    # tournament_size = 2
    # amount_to_cross = 3
    # mutate_probability = 0.01
    # easy_test = Test('easy')
    # flat_test = Test('flat')
    # hard_test = Test('hard')
    # easy_test.roulette_test(loops, roulette_power)
    # flat_test.roulette_test(loops, roulette_power)
    # hard_test.roulette_test(loops, roulette_power)
    # easy_test.tournament_test(loops, tournament_size)
    # flat_test.tournament_test(loops, tournament_size)
    # hard_test.tournament_test(loops, tournament_size)
    # easy_test.crossover_test(amount_to_cross)
    # flat_test.crossover_test(amount_to_cross)
    # m1, m2 = hard_test.crossover_test(amount_to_cross)
    # print(hard_test.check_hard_matrix(m1))
    # print(hard_test.check_hard_matrix(m2))
    # easy_test.mutate_test(mutate_probability)
    # flat_test.mutate_test(mutate_probability)
    # hard_test.mutate_test(mutate_probability)
    population_size = 500
    number_of_generations = 50
    is_tournament = True
    selection_parameter = 25
    genes_to_cross = 4
    crossover_probability = 1
    mutation_probability = 0.8
    case = 'hard'
    sim = Simulation(population_size, number_of_generations, is_tournament, selection_parameter, genes_to_cross,
                     crossover_probability, mutation_probability, case)
    sim.run_simulation(plot=True)
    run_ten(sim)
    #data = Data('data/hard_cost.json', 'data/hard_flow.json', 24).cost_flow_array

    #sim.run_random()






