import unittest
from Stack import *
from custom_queue import *
from Linked_list import *

class Testutils(unittest.TestCase):
    def test(self):
      stack = Stack()
      stack.push('data1')
      self.assertEqual('data1',stack.top.data)


    def test_pop(self):
        stack1 = Stack()
        stack1.push('data1')
        stack1.push('data2')
        stack1.pop()
        self.assertEqual('data1', stack1.top.data)

    def test_enqueue(self):
        q = Queue()
        q.enqueue('data1')
        q.enqueue('data2')
        q.enqueue('data3')
        self.assertEqual('data2', q.head.next.data)

    def test_linkedlist(self):
        l = LinkedList()
        l.insert_beginning({'id': 1})
        l.insert_at_end({'id': 2})
        self.assertEqual({'id': 2}, l.head.next.data)





if __name__ == '__name__':
    unittest.main()
