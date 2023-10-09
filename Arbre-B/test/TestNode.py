import unittest
import sys

sys.path.insert(0, '../src')
from Node import *

class TestNode(unittest.TestCase):

    def setUp(self):
        self.node = Node()

    def test_add_key(self):
        
        self.assertEqual(self.node.add_key(5), 0)
        self.assertEqual(self.node.add_key(2), 0)
        self.assertEqual(self.node.add_key(8), 2)
        self.assertEqual(self.node.add_key(1), 0)
        self.assertEqual(self.node.add_key(10), 4)
        self.assertEqual(self.node.keys, [1, 2, 5, 8, 10])

    def test_add_childs(self):
        
        child1 = Node()
        child2 = Node()
        child3 = Node()

        self.node.add_childs(child1)
        self.node.add_childs(child2)
        self.node.add_childs(child3)

        self.assertEqual(self.node.childs, [child1, child2, child3])

    def test_add_childs_idx(self):
        
        child1 = Node()
        child2 = Node()
        child3 = Node()

        self.node.add_childs(child1)
        self.node.add_childs(child3)

        self.node.add_childs_idx(1, child2)

        self.assertEqual(self.node.childs, [child1, child2, child3])

    def test_childSearch(self):
        
        self.node.add_key(5)
        self.node.add_key(10)
        self.node.add_key(15)

        self.assertEqual(self.node.childSearch(3), 0)
        self.assertEqual(self.node.childSearch(8), 1)
        self.assertEqual(self.node.childSearch(12), 2)
        self.assertEqual(self.node.childSearch(17), 3)

    def test_search(self):
        
        child1 = Node()
        child1.add_key(1)
        child1.add_key(2)
        child1.add_key(3)

        child2 = Node()
        child2.add_key(5)
        child2.add_key(7)
        child2.add_key(9)

        child3 = Node()
        child3.add_key(12)
        child3.add_key(15)
        child3.add_key(18)

        self.node.add_key(5)
        self.node.add_key(10)
        self.node.add_key(15)

        self.node.add_childs(child1)
        self.node.add_childs(child2)
        self.node.add_childs(child3)

        self.assertTrue(self.node.search(5))
        self.assertFalse(self.node.search(4))
        self.assertFalse(self.node.search(18))
        self.assertFalse(self.node.search(20))
        self.assertTrue(child1.search(1))
        self.assertFalse(child2.search(8))
        self.assertTrue(child3.search(12))
        
    def test_get_max_and_get_min(self):
        
        node1 = Node()
        node1.add_key(5)
        node1.add_key(7)
        node1.add_key(10)
        node1.add_key(15)
        self.assertEqual(node1.get_max(),15)
        self.assertEqual(node1.get_max(),10)
        self.assertEqual(node1.get_min(),5)

        root = Node()
        root.add_key(20)
        root.add_key(40)
        root.add_key(60)

        child1 = Node()
        child1.add_key(10)
        child1.add_key(30)

        child2 = Node()
        child2.add_key(50)

        child3 = Node()
        child3.add_key(70)
        child3.add_key(80)

        root.add_childs(child1)
        root.add_childs(child2)
        root.add_childs(child3)

        self.assertEqual(root.get_max(),80)
        self.assertEqual(root.get_min(),10)



if __name__ == '__main__':
    unittest.main()
