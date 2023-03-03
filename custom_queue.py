class Node:
    """ Это узел """
    def __init__(self, data):
        self.data = data  # тут данные
        self.next = None # тут ссылка на следующий

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self,data):
        """Добавляет элемент в очередь"""
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):

      """Удаляет первый элемент из очереди и возвращает этот удалённый элемент"""
      remove = self.head.data
      self.top = self.head.next
      return remove


q1 = Queue()
q1.enqueue('data1')
q1.enqueue('data2')
q1.enqueue('data3')
print(q1.dequeue())
