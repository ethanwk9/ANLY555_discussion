# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 12:32:31 2020

"Array" implementation of heap using built-in lists

@author: jerem
"""
class nHeap:
    def __init__(self, n):
        self.heapList = [float('-inf')]
        self.currentSize = 0
        self.n = n

    def percUp(self,i):
        '''swap the parent and child position up the tree to meet the value constraint'''
        while i // self.n > 0:
          # if the child is less than the parent, swap the postion of nodes
          if self.heapList[i] < self.heapList[i // self.n]:
             tmp = self.heapList[i // self.n]
             self.heapList[i // self.n] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // self.n

    def insert(self,k):
      '''method to insert new value in the tree'''
      # first add the value to the end of the tree, then check for value constraint, if violate, move up the node into correct position
      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize)

    def percDown(self,i):
      '''method to swap node position down the tree'''
      while (i * self.n) <= self.currentSize:
          mc = self.minChild(i)
          if self.heapList[i] > self.heapList[mc]:
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc

    def minChild(self,i):
      '''find the child of a parent node with the minimum value'''
      if i * self.n > self.currentSize:
        return (i-1)*self.n + 2
      else:
        # looking for the patterns in finding the first children of a node
        # n = 2, i=2 fc=4, i=3 fc=6, i=4 fc=8
        # n = 3, i=2 fc=5, i=3 fc=8, i=4 fc=11
        # n = 4, i=2 fc=6, i=3 fc=10,i=4 fc=14
        # fc = (i-1)*n + 2
        firstChild = (i-1)*self.n + 2
        mc = 0
        # compare the value of all children with the parent and return the position of the min child node
        for j in range(1,self.n):
          nextChild = firstChild + j
          if nextChild < self.currentSize and self.heapList[firstChild+mc] > self.heapList[firstChild+j]:
            mc = j
        return firstChild + mc
 
    def delMin(self):
      '''delete and return the minimum value of the heap'''
      # the minimum value of a heap is always the first element in the hep
      retval = self.heapList[1]
      # move the last element to the top of the tree
      self.heapList[1] = self.heapList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      # then swap the node down the tree to meet the value constraint of a heap
      self.percDown(1)
      return retval

    def buildHeap(self,alist):
      '''build the heap with an array'''
      i = len(alist) // self.n
      self.currentSize = len(alist)
      self.heapList = [float('-inf')] + alist[:]
      while (i > 0):
          self.percDown(i)
          i = i - 1
    
    def __str__(self):
      '''visualize the tree'''
      return self.toString(0)

    def toString(self,i):
      '''recursive helper function to visualize the tree'''
      # slice the place holder -inf out the list then build the string representation of the tree
      sss = '[' + str(self.heapList[1:][i])
      # loop through the children of a node
      for j in range(1, self.n+1):
        child = i*self.n+j
        if child < self.currentSize:
          sss += self.toString(child)
      sss += ']'
      return sss


nh = nHeap(3)
nh.buildHeap([9,5,6,2,3,10,12,1,20,24,23,17])
print(nh.heapList)
print(nh)
print(nh.delMin())
print(nh.delMin())
print(nh.delMin())
print(nh.delMin())
print(nh.delMin())

'''
Test results:
[-inf, 1, 3, 6, 2, 5, 10, 12, 9, 20, 24, 23, 17]
[1[3[5][10][12]][6[9][20][24]][2[23][17]]]
1
2
3
5
6

Discussion:
One main goal associated with trees is improved time complexity, but how is this related to the branching factor? 
For example, are 2-ary heaps more or less efficient than 5-ary heaps? 
Propose an optimal value for n and justify your proposition with an extensive discussion and explanation. 

The branching factor n determines the maximum number of children a node could have which affect the height of the tree.
And the height of the tree will affect the time complexity of operations on the tree. 
Comparing the 2-ary heaps and 5-ary heaps with a same length array, a 5-ary heap will result in a shorter height tree.
For insertion operations, a 5-ary heaps will need less time/less steps to move the values inserted up the level of breath of the tree
because a 5-art heaps is shorter in height. 
Also, when looking a the minimum/maximun value (deletion operation), a 5-ary heaps will need less time since there are more children in one breath level.
Therefore, 5-ary heaps will be more efficient than 2-ary heaps in terms of time complexity.
'''