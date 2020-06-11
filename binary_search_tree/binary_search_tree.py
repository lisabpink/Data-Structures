"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#! Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        elif value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    #! insert SOLUTION/LECTURE CODE
    # * call stack:
    # 5.insert(2)
    # 2.insert(3)- this happened on  (self.left.insert(value))
    # 5.insert (7)
    # Insert the given value into the tree
    def insert(self, value):
        # if value(2)[test line 13] is less than self value (5)
        if value < self.value:
            # if left node is None(assigned value above)
            if self.left is None:
                # insert value(2)
                self.left = BSTNode(value)
            else:
                # self left insert (3)
                self.left.insert(value)

        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)

            else:
                self.right.insert(value)

#! Return True if the tree contains the value
   # False if it does not
    def contains(self, target):
        if target < self.value:
            return self.left.contains(target) if self.left else False
        elif target > self.value:
            return self.right.contains(target) if self.right else False
        else:
            return True

#! contains SOLUTION/LECTURE CODE
# * Call stack:
# 5.contains(7)
# 7.contains(7) - return true - this true gets passes back up to 5. 5 now true- tests passing
# RECURSION IS CONFUSING!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# See if bst contains a value
# Return True if the tree contains the value
 # False if it does not
    def contains(self, target):
        # start out with a node that is 5, then insert 2, 7
        if self.value == target:
            return True
        # which direction?
        if target >= self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

    #! Return the maximum value found in the tree
        # start with node of 5- assert git max will return 5
        # rule at root- anything left is lower- anything right is bigger
        # if you start at root and go right until you hit none- you will get your largest item
        # how many calls will be pushed onto the stack before we hit the base case? 3
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    #! Call the function `fn` on the value of each node

    def for_each(self, fn):
        self.value = fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

#! for_each SOLUTION/LECTURE CODE
# the only thing it accepts is a callback function
# call stack
# 5.for_each(fn) = 5(fn)appends 5 to the list then pops off
# 50.for_each(fn) = fn(50) appends 50 to the list then pops off, etc, etc

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        # if there is something to the right of our node
        if self.right is not None:
            # callback fn - appends to array
            self.right.for_each(fn)
        if self.left is not None:
            self.left.for_each(fn)


#    # Part 2 -----------------------

   # Print all the values in order from low to high
   # Hint:  Use a recursive, depth first traversal


        def in_order_print(self, node):
            pass
    # # lowest number is always the furthest to the left

    # # base case?
    # if node is None:
    #     return
    #  # if node is None?

    #  # recursive case?
    #  self.in_order_print(self.left)

     # build up your call stack to see what happens?
     # were trying to get all the way to the bottom before we print anything

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        # queue and/or stack would work best here- USE QUEUE- around 20-25 lines of code
        pass
    # *use queue
        # start queue with root node
        # if queue is filled up and then taken out-
        # #how will we know when we stop? what condition is it going to check?
        # what if first thing we put in queue? no heads on BST- only nodes
        # if queue is empyt- called size

    # *while loop that checks size of queue- not using recursion
        # need somekind of pointer variable that updates at the begenning of each loop

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass
        # *use stack class
        # start stack with root node

        # *iterate whith while loop that checks stack size
        # use a pointer variable

        # why does queue work for BFT?

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
