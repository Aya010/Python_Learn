"""
There are class and function about Josephus Problem.
"""
import person
import copy
class Josephus():
    def __init__(self, start, step):
        self._people = []
        self.start = start - 1 # public? 
        self.step = step
    def __iter__(self): # save data
        self._iter = copy.deepcopy(self._people)
        self._start = self.start
        return self
    def __next__(self):
        if len(self._people) > 0:
            return self._people.pop(self.out_order)
        else:   #   reload data and stop iteration
            self.start = self._start
            self._people = copy.deepcopy(self._iter)
            raise StopIteration
    def append(self, person):
        self._people.append(person)
    def pop(self):
        return self._people.pop(self.out_order)
    @property
    def out_order(self):
        num = len(self._people)
        self.start = (self.start + self.step - 1) % num
        return self.start

"""
    def create_ring(self, file_str):  # 输入参数可以设计为文件名
        with open(file_str) as file_:
            for line in file_:
                line_words = line.split(" ")
                person_ = person.Person(line_words[0], line_words[1], line_words[2])
                self._people.append(person_)
        return ring
"""

def create_ring(file_str, ring):  # 输入参数可以设计为文件名
    with open(file_str) as file_:
        for line in file_:
            line_words = line.split(" ")
            person_ = person.Person(line_words[0], line_words[1], line_words[2])
            ring.append(person_)
    return ring
