import unittest
from Stack import *


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


if __name__ == '__name__':
    unittest.main()
