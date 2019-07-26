# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 18:15:50 2019

Linked List
@author: Arjan
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.nextNode = None
    
    def traverse(self):
        node = self
        while node != None:
            print(node.value)
            node = node.nextNode

n1 = Node(7)
n2 = Node(30)
n3 = Node(73)
n1.nextNode = n2
n2.nextNode = n3
n1.traverse()