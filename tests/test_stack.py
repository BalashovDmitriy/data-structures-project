import unittest
from src.stack import Stack


class TestStack(unittest.TestCase):

    def test_pop(self):
        stack = Stack()
        stack.push('1')
        stack.push('2')
        self.assertEqual(stack.pop(), '2')

    def test_repr(self):
        stack = Stack()
        stack.push('1')
        stack.push('2')
        self.assertEqual(stack.__repr__(), '1, 2')
