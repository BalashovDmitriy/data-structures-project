import unittest
from src.stack import Stack


class TestStack(unittest.TestCase):

    def test_pop(self):
        stack = Stack()
        stack.push('test1')
        self.assertEqual(stack.pop(), 'test1')

    def test_top(self):
        stack = Stack()
        stack.push('data1')
        stack.pop()

        self.assertEqual(stack.top, None)

        stack.push('data1')
        stack.push('data2')
        data = stack.pop()

        self.assertEqual(stack.top.data, 'data1')
        self.assertEqual(data, 'data2')

    def test_str(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')
        self.assertEqual(str(stack), "data3, data2, data1")
