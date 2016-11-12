# python2

import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        self.height_dict = {}

    def compute_height(self):
        # Replace this code with a faster implementation
        # maxHeight = 0
        # for vertex in range(self.n):
        #     height = 0
        #     i = vertex
        #     while i != -1:
        #         height += 1
        #         i = self.parent[i]
        #     maxHeight = max(maxHeight, height)
        # return maxHeight

        node_list = range(self.n)
        for node in node_list:
            _ = self.compute_node_height(node)
        return max(self.height_dict.values())

    def compute_node_height(self, node):
        if not self.height_dict.get(node):
            if self.parent[node] == -1:
                self.height_dict[node] = 1
            else:
                self.height_dict[node] = self.compute_node_height(self.parent[node]) + 1
        return self.height_dict[node]




def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())


threading.Thread(target=main).start()
