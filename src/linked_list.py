class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next_node = self.head
        self.head = new_node
        self.tail = new_node

    def insert_at_end(self, data) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        new_node = Node(data)
        self.tail.next_node = new_node
        self.tail = new_node

    def to_list(self):
        """Вывод данных односвязного списка в список"""
        node = self.head
        if node is None:
            return None
        ll_list = []
        while node:
            ll_list.append(node.data)
            node = node.next_node
        return ll_list

    def get_data_by_id(self, id_: int):
        """Возвращает данные (словарь) узла с указанным id"""
        node = self.head
        if node is None:
            return None
        while node:
            try:
                if node.data['id'] == id_:
                    return node.data
                node = node.next_node
            except TypeError:
                print("Данные не являются словарем или в словаре нет id.")
                node = node.next_node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string
