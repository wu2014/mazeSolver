"""
File: stack.py

Stack implementations
"""

from arrays import Array

class ArrayStack(object):
    """ Array-based stack implementation."""

    DEFAULT_CAPACITY = 10  # Class variable for all array stacks
    
    def __init__(self):
        self._items = Array(ArrayStack.DEFAULT_CAPACITY)
        self._top = -1
        self._size = 0

    def push(self, newItem):
        """Inserts newItem at top of stack."""
        # Resize array if necessary
        if len(self) == len(self._items):
            temp = Array(2 * self._size)
            for i in xrange(len(self)):
                temp[i] = self._items[i]
            self._items = temp
        # newItem goes at logical end of array
        self._top += 1
        self._size += 1
        self._items[self._top] = newItem

    def pop(self):
        """Removes and returns the item at top of the stack.
        Precondition: the stack is not empty."""
        oldItem = self._items[self._top]
        self._top -= 1
        self._size -= 1
        # Resizing the array is an exercise
        return oldItem

    def peek(self):
        """Returns the item at top of the stack.
        Precondition: the stack is not empty."""
        return self._items[self._top]

    def __len__(self):
        """Returns the number of items in the stack."""
        return self._size

    def isEmpty(self):
        return len(self) == 0

    def __str__(self):
        """Items strung from bottom to top."""
        result = ""
        for i in xrange(len(self)):
            result += str(self._items[i]) + " "
        return result


from node import Node

class LinkedStack(object):
    """ Link-based stack implementation."""

    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, newItem):
        """Inserts newItem at top of stack."""
        self._top = Node(newItem, self._top)
        self._size += 1

    def pop(self):
        """Removes and returns the item at top of the stack.
        Precondition: the stack is not empty."""
        oldItem = self._top.data
        self._top = self._top.next
        self._size -= 1
        return oldItem

    def peek(self):
        """Returns the item at top of the stack.
        Precondition: the stack is not empty."""
        return self._top.data

    def __len__(self):
        """Returns the number of items in the stack."""
        return self._size

    def isEmpty(self):
        return len(self) == 0

    def __str__(self):
        """Items strung from bottom to top."""
        
        # Helper recurses to end of nodes
        def strHelper(probe):
            if probe is None:
                return ""
            else:
                return strHelper(probe.next) + \
                       str(probe.data) + " "
            
        return strHelper(self._top)


def main():
    # Test either implementation with same code
    s = ArrayStack()
    #s = LinkedStack()
    print "Length:", len(s)
    print "Empty:", s.isEmpty()
    print "Push 1-10"
    for i in xrange(10):
        s.push(i + 1)
    print "Peeking:", s.peek() 
    print "Items (bottom to top):",  s
    print "Length:", len(s)
    print "Empty:", s.isEmpty()
    print "Push 11"
    s.push(11)
    print "Popping items (top to bottom):",
    while not s.isEmpty(): print s.pop(),
    print "\nLength:", len(s)
    print "Empty:", s.isEmpty()


if __name__ == '__main__': 
    main()
