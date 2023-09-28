class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_data(self, new_data):
        self.data = new_data
    def set_next(self, new_next):
        self.next = new_next
    def __str__(self):
        return f"{self.data}"
    def add_after(self, value):
        tmp = self.get_next()
        self.set_next(Node(value))
        self.get_next().set_next(tmp)
    def add_list_from_last(self, a_list):
        while len(a_list) != 0:
            self.add_after(a_list.pop(0))
    def get_vowels(self):
        v = 'AEIOUaeiou'
        vs = ''
        for i in self.data:
            if i in v:
                vs += i
        return vs
