from heapq import heappush, heappop

class Cola(object):
    cola = []

    def __init__(self, cola = []):
        self.cola = cola

    def push(self, item):
        heappush(self.cola, item)

    def pop(self):
        return heappop(self.cola)
