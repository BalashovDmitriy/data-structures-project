"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    """Тесты для класса linked_list."""

    def test_linked_list(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})
        self.assertEqual(str(ll), "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")

    def test_linked_list_to_list(self):
        ll = LinkedList()

        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        ll.insert_beginning({'id': 0, 'username': 'serebro'})
        lst = ll.to_list()
        self.assertEqual(lst[0], {'id': 0, 'username': 'serebro'})
        self.assertEqual(lst[3], {'id': 3, 'username': 'mosh_s'})

    def test_linked_list_get_by_data_id(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end('idusername')
        ll.insert_at_end([1, 2, 3])
        ll.insert_at_end({'id': 2, 'username': 'mosh_s'})

        user_data = ll.get_data_by_id(2)
        self.assertEqual(user_data, {'id': 2, 'username': 'mosh_s'})
