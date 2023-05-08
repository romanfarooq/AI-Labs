10
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 07:15:34 2022

@author: Sheikh Waqas Akhtar
"""

##Binary search tree implementation
class Node:
    def __init__(self,data):
        self.data = data
        self.right_child= None
        self.left_child = None

class Tree(Node):
    def __init__(self):
        self.root_node = None
        
    def find_min(self):
        current = self.root_node
        while current.left_child:
            current = current.left_child
            
        return current
    
    def find_max(self):
        current = self.root_node
        while current.right_child:
            current = current.right_child
            
        return current
    
    def insert (self, data):
        node = Node(data)
        if self.root_node is None:
            self.root_node = node
        else:
            current = self.root_node
            parent = None
            while True:
                parent = current
                if node.data < parent.data:
                    current = current.left_child
                    if current is None:
                        parent.left_child= node
                        return
                else:
                    current= current.right_child
                    if current is None:
                        parent.right_child = node
                        return
                    
    def search(self, data):
        current = self.root_node
        while True:
            if current is None:
                return None
            elif current.data is data:
                return data
            elif current.data > data:
                current = current.left_child
            else:
                current = current.right_child

    def get_node_with_parent(self, data):
        parent = None
        current = self.root_node
        if current is None:
            return (parent, None)
        while True:
            if current.data == data:
                return (parent, current)
            elif current.data > data:
                parent = current
                current = current.left_child
            else:
                parent = current
                current = current.right_child
                return (parent, current)
            
    def remove(self, data):
        parent, node = self.get_node_with_parent(data)
        if parent is None and node is None:
            return False
        # Get children count
        children_count = 0
        if node.left_child and node.right_child:
            children_count = 2
        elif (node.left_child is None) and (node.right_child is None):
            children_count = 0
        else:
            children_count = 1
        if children_count == 0:
            if parent:
                if parent.right_child is node:
                    parent.right_child = None
                else:
                    parent.left_child = None
            else:
                self.root_node = None
        elif children_count == 1:
            next_node = None
            if node.left_child:
                next_node = node.left_child
            else:
                next_node = node.right_child
            if parent:
                if parent.left_child is node:
                    parent.left_child = next_node
                else:
                    parent.right_child = next_node
            else:
                self.root_node = next_node
             
        else:
            parent_of_leftmost_node = node
            leftmost_node = node.right_child
            while leftmost_node.left_child:
                parent_of_leftmost_node = leftmost_node
                leftmost_node = leftmost_node.left_child
             
            node.data = leftmost_node.data
            if parent_of_leftmost_node.left_child == leftmost_node:
                parent_of_leftmost_node.left_child = leftmost_node.right_child
            else:
                parent_of_leftmost_node.right_child = leftmost_node.right_child
            
            
tree = Tree()
tree.insert(5)
tree.insert(2)
tree.insert(7)
tree.insert(9)
tree.insert(1)
for i in range(1, 10):
    found = tree.search(i)
    print("{}: {}".format(i, found))
"""
#Task
--Write a class named "uninformed" which should contain BFS and DFS search algorithms
to traverse the tree.
--Create an instance of that class.
--Call the instance method BFS, pass the above created tree to the method, 
the traversing result should be stored. Print the traversed result.
--Call the instance method DFS, pass the above created tree to the method, 
the traversing result should be stored. Print the traversed result.
"""
#Write your solution here

class uninformed:
    def __init__(self):
        self.root_node = None
        self.BFS_result = []
        self.DFS_result = []
        
    def BFS(self, tree):
        queue = []
        queue.append(tree.root_node)
        while len(queue) > 0:
            node = queue.pop(0)
            self.BFS_result.append(node.data)
            if node.left_child is not None:
                queue.append(node.left_child)
            if node.right_child is not None:
                queue.append(node.right_child)
        return self.BFS_result
    
    def DFS(self, tree):
        stack = []
        stack.append(tree.root_node)
        while len(stack) > 0:
            node = stack.pop()
            self.DFS_result.append(node.data)
            if node.right_child is not None:
                stack.append(node.right_child)
            if node.left_child is not None:
                stack.append(node.left_child)
        return self.DFS_result
    
un = uninformed()
print(un.BFS(tree))
print(un.DFS(tree))