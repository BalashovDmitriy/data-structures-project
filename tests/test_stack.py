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

        assert stack.top is None

        stack.push('data1')
        stack.push('data2')
        data = stack.pop()

        assert stack.top.data == 'data1'
        assert data == 'data2'


