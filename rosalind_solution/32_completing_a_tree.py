# Problem
#
# Figure 2. A labeled tree with 6 vertices and 5 edges.
# An undirected graph is connected if there is a path connecting any two nodes. A tree is a connected (undirected) graph containing no cycles; this definition forces the tree to have a branching structure organized around a central core of nodes, just like its living counterpart. See Figure 2.
#
# We have already grown familiar with trees in “Mendel's First Law”, where we introduced the probability tree diagram to visualize the outcomes of a random variable.
#
# In the creation of a phylogeny, taxa are encoded by the tree's leaves, or nodes having degree 1. A node of a tree having degree larger than 1 is called an internal node.
#
# Given: A positive integer n (n≤1000) and an adjacency list corresponding to a graph on n nodes that contains no cycles.
#
# Return: The minimum number of edges that can be added to the graph to produce a tree.
#
# Sample Dataset
# 10
# 1 2
# 2 8
# 4 10
# 5 9
# 6 10
# 7 9
# Sample Output
# 3

import sys

def read_file(filename):
    nodes = 0
    edges = []
    with open(filename) as file:
        contents = file.readlines()
        nodes = int(contents[0])
        for i in range(1, len(contents)):
            edges.append(list(map(int, contents[i].split())))
    return nodes, edges

def min_add(filename):
    nodes, edges = read_file(filename)
    # for the total nodes, number of edges/connect required is total nodes - 1
    return nodes - 1 - len(edges)

if __name__ == "__main__":
    print(min_add(sys.argv[1]))
