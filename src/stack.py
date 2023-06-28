class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.__top = None

    @property
    def top(self):
        return self.__top

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        self.__top = Node(data, self.__top)

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        data = self.__top.data
        self.__top = self.__top.next_node
        return data

    def __str__(self):
        list_ = []
        while True:
            if self.__top is None:
                return ", ".join(list_)
            else:
                list_.append(self.__top.data)
                self.pop()
