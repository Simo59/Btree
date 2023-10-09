import unittest
import time
import sys
import random
import matplotlib.pyplot as plt


sys.path.insert(0, '../src')
from Btree import *

class TestBTree(unittest.TestCase):
    
    def test_performance_insertion(self):
        
        btree = Btree(2, 3)
        start_time = time.time()
        for i in range(10000):
            btree.insert(i)
        end_time = time.time()
        execution_time = end_time - start_time
        print("test_performance_insertion: ", execution_time)
        
    def test_performance_delete(self):
        
        btree = Btree(2, 3)
        start_time = time.time()
        for i in range(10000):
            btree.insert(i)
        for i in range(10000, 0, -1):
            btree.delete(i)
        end_time = time.time()
        execution_time = end_time - start_time
        print("test_performance_delete :", execution_time)
    
    def test_performance_random_ops(self):
        btree = Btree(4, 8)
        start_time = time.time()
        
        for i in range(100000):
            key = random.randint(0, 9999)
            btree.insert(key)
            btree.search(key)
            
        end_time = time.time()
        execution_time = end_time - start_time
        print("test_performance_random: ", execution_time)
        
    def test_read_t(self):
        
        btree = Btree(2, 4)
        num_transactions = 1000
        total_virtual_reads = 0
        
        for i in range(num_transactions):
            btree.insert(i)
            total_virtual_reads += btree.root.num_virtual_reads
            
        avg = total_virtual_reads / num_transactions
        
        print("test_vr_t :", avg)
        
    def test_write_i(self):
        
        btree = Btree(2, 4)
        num_insert = 1000
        total_virtual_write = 0
        
        for i in range(num_insert):
            btree.insert(i)
            total_virtual_write += btree.root.num_virtual_write
            
        avg = total_virtual_write / num_insert
        
        print("test_vw_i :", avg)
        
        
    def test_complexity_search(self):
        complexities = []
        for n in [10, 500, 1000, 2500, 5000,10000]:
            btree = Btree(2, 7)
            for i in range(n):
                btree.insert(i)

            start_time = time.time()
            for i in range(n):
                btree.search(i)
            end_time = time.time()
            execution_time = end_time - start_time
            complexities.append((n, execution_time))
            
        for i in range(1, len(complexities)):
            time_ratio = complexities[i][0] / complexities[i - 1][0]
            if complexities[i - 1][1] == 0:
                continue
            time_ratio = complexities[i][1] / complexities[i - 1][1]
            print(time_ratio)
        
        return complexities



    def test_complexity_insert(self):
        complexities = []
        for n in [10, 500, 1000, 2500, 5000,10000]:
            btree = Btree(2, 7)
            start_time = time.time()
            for i in range(n):
                btree.insert(i)
            end_time = time.time()
            execution_time = end_time - start_time
            complexities.append((n, execution_time))

        for i in range(1, len(complexities)):
            time_ratio = complexities[i][0] / complexities[i - 1][0]
            if complexities[i - 1][1] == 0:
                continue
            time_ratio = complexities[i][1] / complexities[i - 1][1]
            print(time_ratio)
        
        return complexities



    def test_complexity_delete(self):
        complexities = []
        for n in [10, 500, 1000, 2500, 5000,10000]:
            btree = Btree(2, 7)
            for i in range(n):
                btree.insert(i)

            start_time = time.time()
            for i in range(n):
                btree.delete(i)
            end_time = time.time()
            execution_time = end_time - start_time
            complexities.append((n, execution_time))

        for i in range(1, len(complexities)):
            time_ratio = complexities[i][0] / complexities[i - 1][0]
            if complexities[i - 1][1] == 0:
                continue
            time_ratio = complexities[i][1] / complexities[i - 1][1]
            print(time_ratio)
            
        return complexities

    
    def test_complexity(self):
        
        complexities_search = self.test_complexity_search()
        complexities_insert = self.test_complexity_insert()
        complexities_delete = self.test_complexity_delete()
        
        self.plot_complexity_graph('Complexité temporelle', [('Search', complexities_search), ('Insert', complexities_insert), ('Delete', complexities_delete)])

    def plot_complexity_graph(self, title, data):
        plt.figure()
        print(data)
        for label, complexities in data:
            x = [c[0] for c in complexities]
            y = [c[1] for c in complexities]
            plt.plot(x, y, marker='o', label=label)
        plt.xscale('linear')
        plt.yscale('log')
        plt.xlabel('Elements : n')
        plt.ylabel('Time : s')
        plt.title(title)
        plt.legend()
        plt.grid(True)
        plt.show()
    
        
if __name__ == '__main__':

    unittest.main()
