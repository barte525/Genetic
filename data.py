import json
import numpy as np


class Data:
    def __init__(self, cost_file, flow_file, number_of_machines):
        self.cost_array = self.fetch_data_from_file(cost_file, number_of_machines, 'cost')
        self.flow_array = self.fetch_data_from_file(flow_file, number_of_machines, 'amount')
        self.cost_flow_array = self.cost_array * self.flow_array

    @staticmethod
    def fetch_data_from_file(file, n, value):
        array = np.zeros(shape=(n, n), dtype=int)
        with open(file) as json_file:
            data = json.load(json_file)
        for elem in data:
                array[elem['source'], elem['dest']] = elem[value]
        return array

