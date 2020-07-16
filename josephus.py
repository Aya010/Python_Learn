"""
There are class and function about Josephus Problem.
"""

import person
import copy

class Josephus():
    def __init__(self, start, step, people):
        self._people = people
        self.start = start # public_?  add a new 
        self._current = self.start - 1
        self.step = step

    def __iter__(self): # save data
        self._iter = copy.deepcopy(self._people)
        current = self.start - 1
        while len(self._iter) > 0:
            current =  self._get_pop_order(self._iter, current)
            yield self._iter.pop(current)
        #return self

    """
    def __next__(self):
        if len(self._iter) > 0:
            #return self._pop(self._iter)
            print("here")
        else:   #   reload data and stop iteration
            #self.start = self._current
            #self._people = copy.deepcopy(self._iter)
            self._current = self.start - 1
            raise StopIteration
    """

    def append(self, person):
        self._people.append(person)

    def pop(self):
        self._current = self._get_pop_order(self._people, self._current)
        return self._people.pop(self._current)

    def _get_pop_order(self, target, current):
        num = len(target)
        current = (current + self.step - 1) % num
        return current

def create_ring(person_list):
    ring = []
    for one in person_list:
        person_ = person.Person(one[0], one[1], one[2])
        #print(person_)
        ring.append(person_)
    return ring



    """
    @property # unnessery
    def get_out_order(self):
        num = len(self._people)
        self._current = (self._current + self.step - 1) % num
        return self._current
    """



"""def create_ring(file_str, ring):  # 输入参数可以设计为文件名
    with open(file_str) as file_:
        for line in file_:
            line_words = line.split(" ")
            person_ = person.Person(line_words[0], line_words[1], line_words[2])
            ring.append(person_)
    return ring

if __name__ == "__main__":

    STEP = 2
    START = 3
    ring = Josephus(START, STEP) # ring
    ring = create_ring("Josephus_List2.txt", ring)
    for person in ring: #person
        print(person)
"""