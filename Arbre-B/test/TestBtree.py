import unittest
import time
import sys
import random

sys.path.insert(0, '../src')
from Btree import *


class TestBTree(unittest.TestCase):
    
    def test_init(self):
        
        btree = Btree(2, 4)
        self.assertEqual(btree.L, 2)
        self.assertEqual(btree.U, 4)
        self.assertIsInstance(btree.root, Node)
        
    def test_search(self):
        
        btree = Btree(2, 4)
        btree.insert(5)
        btree.insert(3)
        btree.insert(7)
        btree.insert(1)
        btree.insert(2)
        self.assertTrue(btree.search(5))
        self.assertFalse(btree.search(6))
        self.assertTrue(btree.search(2))
        self.assertFalse(btree.search(10))
    
    def test_insert(self):
        
        btree = Btree(2, 3)

        btree.insert(2)
        btree.insert(4)
        btree.insert(5)
        btree.insert(6)        
        btree.insert(8)
        btree.insert(10)
        btree.insert(12)
        btree.insert(14)
        btree.insert(16)
        btree.insert(18)


        self.assertTrue(btree.search(2))
        self.assertTrue(btree.search(4))
        self.assertTrue(btree.search(5))
        self.assertTrue(btree.search(6))
        self.assertTrue(btree.search(8))
        self.assertTrue(btree.search(10))
        self.assertTrue(btree.search(12))
        self.assertTrue(btree.search(14))
        self.assertTrue(btree.search(16))
        self.assertTrue(btree.search(18))
        
        self.assertEqual(btree.root.keys[0], 6)
        self.assertEqual(btree.root.childs[0].keys[0], 4)
        self.assertEqual(btree.root.childs[1].keys[0], 10)
        self.assertEqual(btree.root.childs[1].keys[1], 14)
        self.assertEqual(btree.root.childs[0].childs[0].keys[0], 2)
        self.assertEqual(btree.root.childs[0].childs[1].keys[0], 5)
        self.assertEqual(btree.root.childs[1].childs[0].keys[0], 8)
        self.assertEqual(btree.root.childs[1].childs[1].keys[0], 12)
        self.assertEqual(btree.root.childs[1].childs[2].keys[0], 16)
        self.assertEqual(btree.root.childs[1].childs[2].keys[1], 18)
        
    def test_delete(self):
        
        btree = Btree(2, 3)

        btree.insert(2)
        btree.insert(4)
        btree.insert(5)
        btree.insert(6)        
        btree.insert(8)
        btree.insert(10)
        btree.insert(12)
        btree.insert(14)
        btree.insert(16)
        btree.insert(18)

        self.assertTrue(btree.search(2))
        self.assertTrue(btree.search(4))
        self.assertTrue(btree.search(5))
        self.assertTrue(btree.search(6))
        self.assertTrue(btree.search(8))
        self.assertTrue(btree.search(10))
        self.assertTrue(btree.search(12))
        self.assertTrue(btree.search(14))
        self.assertTrue(btree.search(16))
        self.assertTrue(btree.search(18))
        
        self.assertEqual(btree.root.childs[1].childs[2].keys[1], 18)
        btree.delete(18)
        self.assertEqual(len(btree.root.childs[1].childs[2].keys), 1)
        self.assertFalse(btree.search(18))
        
        self.assertEqual(btree.root.childs[1].childs[2].keys[0], 16)
        btree.delete(16)
        self.assertEqual(len(btree.root.childs[1].childs), 2)
        self.assertFalse(btree.search(16))
        
        btree.delete(14)
        btree.delete(12)
        
        self.assertFalse(btree.search(12))
        self.assertFalse(btree.search(14))

    def test_performance_E1(self):
        
        btree = Btree(4, 8)
        
        start_time = time.time()
        for i in range(10000):
            btree.insert(i) 
        for i in range(50):
            key = random.randint(0, 10000)
            btree.search(key)
        for i in range(100):
            btree.delete(i)
            
        end_time = time.time()
        execution_time = end_time - start_time
        print("test_performance_E1 : ", execution_time)

    def test_performance_E4(self):
        
        btree = Btree(4, 8)
        
        start_time = time.time()
        for i in range(10000):
            btree.insert(i)
        for i in range(50):
            key = random.randint(10000, 20000)
            btree.insert(key)
        for i in range(1000):
            key = random.randint(0, 10000)
            btree.search(key)
        for i in range(10000):
            btree.delete(i)
            
        end_time = time.time()
        execution_time = end_time - start_time
        print("test_performance_E4 : ", execution_time)
        

    def test_performance_E5(self):
        
        btree = Btree(4, 8)
        
        start_time = time.time()
        for i in range(5000):
            key = random.randint(0, 5000)
            btree.insert(key) 
        for i in range(1000):
            key = random.randint(0, 5000)
            btree.search(key)
        for i in range(5000):
            btree.delete(i)
            
        end_time = time.time()
        execution_time = end_time - start_time
        print("test_performance_E5 : ", execution_time)
        
        
    def test_performance_E7(self):
        
        btree = Btree(4, 8)
        
        start_time = time.time()
        for i in range(5000):
            btree.insert(i)
        for i in range(6000):
            key = random.randint(5000, 999999)
            btree.insert(key) 
        for i in range(6000):
            key = random.randint(0, 999999)
            btree.search(key)
        for i in range(60000):
            btree.delete(i)
            
        end_time = time.time()
        execution_time = end_time - start_time
        print("test_performance_E7 : ", execution_time)
        
        
    def test_performance_E10(self):
        
        btree = Btree(4, 8)
        
        start_time = time.time()
        for i in range(100000):
            btree.insert(i)
        for i in range(6000):
            key = random.randint(100000, 999999)
            btree.insert(key) 
        for i in range(6000):
            key = random.randint(0, 999999)
            btree.search(key)
        for i in range(60000):
            btree.delete(i)
            
        end_time = time.time()
        execution_time = end_time - start_time
        print("test_performance_E10 : ", execution_time)        

        
if __name__ == '__main__':
    unittest.main()