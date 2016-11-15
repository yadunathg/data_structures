# python2

class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []
        self._size = 0

    def ReadData(self):
        self._size = int(input())
        self._data = [int(s) for s in raw_input().split()]
        assert self._size == len(self._data)

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print swap[0], swap[1]

    def GenerateSwaps(self):
        # The following naive implementation just sorts
        # the given sequence using selection sort algorithm
        # and saves the resulting sequence of swaps.
        # This turns the given array into a heap,
        # but in the worst case gives a quadratic number of swaps.
        #
        # TODO: replace by a more efficient implementation
        # for i in range(len(self._data)):
        #   for j in range(i + 1, len(self._data)):
        #     if self._data[i] > self._data[j]:
        #       self._swaps.append((i, j))
        #       self._data[i], self._data[j] = self._data[j], self._data[i]

        for i in range(int(self._size/2)-1, -1, -1):
            self.SiftDown(i)

    def SiftDown(self, i):
        min_ind = i
        i_left_child = 2*i+1
        if self._size > i_left_child and self._data[min_ind] > self._data[i_left_child]:
            min_ind = i_left_child
        i_right_child = 2*i+2
        if self._size > i_right_child and self._data[min_ind] > self._data[i_right_child]:
            min_ind = i_right_child
        if i != min_ind:
            self._swaps.append((i, min_ind))
            self._data[i], self._data[min_ind] = self._data[min_ind], self._data[i]
            self.SiftDown(min_ind)

    def Solve(self):
        self.ReadData()
        self.GenerateSwaps()
        self.WriteResponse()
        # print self._data


if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
