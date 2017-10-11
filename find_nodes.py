# -*- coding: UTF-8 -*-

# Set the data structure
class BinaryTree(object):

    # initialization of the class
    def __init__(self, value):
        self.value = value
        self.leftBranch = None
        self.rightBranch = None
        self.parent = None

    # setting the 'coordinates'
    def setLeftBranch(self, node):
        self.leftBranch = node

    def setRightBranch(self, node):
        self.rightBranch = node

    def setParent(self, parent):
        self.parent = parent

    def getValue(self):
        return self.value

    def getLeftBranch(self):
        return self.leftBranch

    def getRightBranch(self):
        return self.rightBranch

    def getParent(self):
        return self.parent

    def __unicode__(self):
        return self.value

    # if python 3x
    # def __str__(self):
    #     return self.value


def BFSBinary(root, function):
    queue = [root]
    while len(queue) > 0:
        if function(queue[0]):
            return True
        else:
            temp = queue.pop(0)
            if temp.getLeftBranch():
                queue.append(temp.getLeftBranch())
            if temp.getRightBranch():
                queue.append(temp.getRightBranch())
    return False


def DFSBinaryPath(root, function):
    stack = [root]
    while len(stack) > 0:
        if function(stack[0]):
            return TracePath(stack[0])
        else:
            temp = stack.pop(0)
            if temp.getRightBranch():
                stack.insert(0, temp.getRightBranch())
            if temp.getLeftBranch():
                stack.insert(0, temp.getLeftBranch())
    return False


def TracePath(node):
    """ Recursive function call with a base case where node is Parent
        and case where node is not the Parent and we climb the tree up.
    """
    if not node.getParent():
        return [node]
    else:
        return [node] + TracePath(node.getParent)
