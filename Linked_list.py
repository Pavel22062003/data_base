class Node:
    def __init__(self,data):
        self.data = dict(data)
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.end = None

    def insert_beginning(self, data): #добавляет элемент в начало
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.end = new_node
            new_node.next = self.end
        else:

            new_node.next = self.head
            self.head = new_node


    def insert_at_end(self,data): # добавляет элемент в конец
        new_node = Node(data)
        if self.end is None:
            self.head = new_node
            self.end = new_node
            new_node.next = self.end

        else:

            self.end.next = new_node
            self.end = new_node

    def print_ll(self): # выводит в консоль данные из односвязанного списка
        ll_string = ''
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next

        ll_string += ' None'
        print(ll_string)




ll = LinkedList()
ll.insert_beginning({'id': 1})
ll.insert_at_end({'id': 2})
ll.insert_at_end({'id': 3})
ll.insert_beginning({'id': 0})
ll.print_ll()
#{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None



