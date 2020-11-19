# Course: CS261 - Data Structures
# Student Name: Ryan Farol
# Assignment: Assignment 4
# Description: The code below contains functions for a Binary Search Tree. It also implements the use of the Stack
# and Queue classes when necessary


class Stack:
    """
    Class implementing STACK ADT.
    Supported methods are: push, pop, top, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty stack based on Python list """
        self._data = []

    def push(self, value: object) -> None:
        """ Add new element on top of the stack """
        self._data.append(value)

    def pop(self) -> object:
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self) -> object:
        """ Return value of top element without removing from stack """
        return self._data[-1]

    def is_empty(self):
        """ Return True if the stack is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "STACK: { " + ", ".join(data_str) + " }"


class Queue:
    """
    Class implementing QUEUE ADT.
    Supported methods are: enqueue, dequeue, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty queue based on Python list """
        self._data = []

    def enqueue(self, value: object) -> None:
        """ Add new element to the end of the queue """
        self._data.append(value)

    def dequeue(self) -> object:
        """ Remove element from the beginning of the queue and return its value """
        return self._data.pop(0)

    def is_empty(self):
        """ Return True if the queue is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "QUEUE { " + ", ".join(data_str) + " }"


class TreeNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value          # to store node's data
        self.left = None            # pointer to root of left subtree
        self.right = None           # pointer to root of right subtree

    def __str__(self):
        return str(self.value)


class BST:
    def __init__(self, start_tree=None) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using in-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self.root, values)
        return "TREE in order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does in-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # base case
        if cur is None:
            return
        # recursive case for left subtree
        self._str_helper(cur.left, values)
        # store value of current node
        values.append(str(cur.value))
        # recursive case for right subtree
        self._str_helper(cur.right, values)

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """add functon takes a new node and adds it onto the BST. First, it checks if it's empty. Then, it traverses
        down the tree until None is reached. If the value is less than the parent node, it goes to the left. If the
        value is greater than or equal to, it goes to the right"""
        add_node = TreeNode(value) # initialize new node
        if self.root == None: # checks if tree is empty
            self.root = add_node
            return
        else:
            parent = None # initialize parent for the new node
            curr_node = self.root # current pointer at the root
            while curr_node != None: # traverse down the list until None is met
                parent = curr_node
                if add_node.value < curr_node.value: # if value is less than, an edge is formed on the left
                    curr_node = curr_node.left
                elif add_node.value >= curr_node.value: # if value is greater than or equal, an edge is formed on the right
                    curr_node = curr_node.right
            if add_node.value < parent.value: # checks value again and places new node on the left if less than the parent value
                parent.left = add_node
            elif add_node.value >= parent.value: # checks value again and places new node on the right if more than or equal to parent value
                parent.right = add_node

    def contains(self, value: object) -> bool:
        """contains function first checks if the BST is empty and returns False if true. Then it traverses down the list
        until the it reaches the leaf node. If value is found, returns True. Else, return False"""
        if self.root == None: # checks if BST is empty
            return False

        else:
            curr_node = self.root # intialize current node pointer at the root
            while curr_node != None: # traverse down the BST
                if curr_node.value == value: # if value is found, return True
                    return True
                elif value < curr_node.value: # determine if needed to traverse left
                    curr_node = curr_node.left
                elif value >= curr_node.value: # determine if needed to traverse right
                    curr_node = curr_node.right
            return False # if not found, return false


    def get_first(self) -> object:
        """get first function first checks if the BST is empty and returns None if true. If not, it returns the value
        of the root node"""
        if self.root == None: # checks if BST is empty an returns None if True
            return None
        else: # returns the root node value
            return self.root.value

    def remove_first(self) -> bool:
        """remove first function deletes the root note of the BST. first checks if the BST is empty and if there
        is only one node. If empty, return False. If only node, delete the root node. Else, find the in order successor
        of the root node which is the leftmost child of the right subtree. If the deleted node only has the left subtree,
        the root node becomes the rood node of the left subtree."""
        if self.root == None: # checks if BST is empty
            return False
        if self.root.left == None and self.root.right == None: # checks if only root node exists within BST
            self.root = None
        elif self.root.right == None: # checks if only left subtree exists
            self.root = self.root.left
        else:
            subtree = self.root.right # initialize subtree
            p_subtree = subtree # initialize parent node
            while subtree.left != None: # traverse down till the in order successor is found (leftmost child)
                p_subtree = subtree
                subtree = subtree.left
            if subtree != self.root.right: # reestablish edges
                p_subtree.left = subtree.right
                subtree.right = self.root.right
            subtree.left = self.root.left # original subtree left is now connected to new node
            self.root = subtree # new root is placed
        return True

    def remove(self, value) -> bool:
        """remove function first traverses throughout the BST and deletes the value entered while restructuring the BST.
        First checks if the BST is empty, if there is only one node, and if the value is contained within the BST.
        If empty, return False. If only node, delete the root node. Else, find the in order successor of the current
        node which is the leftmost child of the right subtree of the current node. If the deleted node only has the
        left subtree, the current node becomes the rood node of the left subtree."""
        if self.contains(value) == False: # check if the value is within the BST
            return False
        if self.root == None: # checks if BST is empty
            return False
        if self.root.value == value: # checks if the value matches the root node
            self.remove_first(value)
            return True

        # traverse through the list first until the value is found
        curr_node = self.root
        parent_node = None
        while curr_node != None: # traverse through the list
            if curr_node.value == value:
                node = curr_node # in order success is initialized as node
                break # once node is found, break the while loop
            elif value < curr_node.value:
                parent_node = curr_node
                curr_node = curr_node.left
            elif value >= curr_node.value:
                parent_node = curr_node
                curr_node = curr_node.right

        # if successor has no children, parent node's node children is updated to None
        if node.left == None and node.right == None:
            parent_node.left = None
            parent_node.right = None
        elif node.right == None: # if success only has a left child, point parent node to its children
            parent_node.right = node.left
        else: # once success is found, traverse to the left most child
            subtree = node.right
            p_subtree = subtree
            while subtree.left != None: # traverse down the list
                p_subtree = subtree
                subtree = subtree.left
            if subtree != node.right: # reestablish edges
                p_subtree.left = subtree.right
                subtree.right = node.right
            parent_node.right = subtree # point parent to new subtree
            temp = curr_node.left # store any other subtrees from the deleted node
            node = subtree # replace successor with current node
            node.left = temp # reattach remaining subtrees
        return True

    def pre_order_traversal(self) -> Queue:
        """pre order traversal function outputs the values of the BST in the que as it is traversed FROM THE LEFT.
        A helper function is used to help with recursive calls"""
        que = Queue() # initialize que
        self.pre_order_traversal_helper(self.root, que) # call helper and using the root node and que as arguments
        return que

    def pre_order_traversal_helper(self, cur_node, que):
        """helper function for pre order traversal"""
        if cur_node == None: # return once traversal is completed
            return

        else:
            que.enqueue(cur_node.value) # add value
            self.pre_order_traversal_helper(cur_node.left, que) # move node left
            self.pre_order_traversal_helper(cur_node.right, que) # move node right

    def in_order_traversal(self) -> Queue:
        """in order traversal function outputs the values of the BST in the que as it is traversed FROM THE BOTTOM.
        A helper function is used to help with recursive calls"""
        que = Queue() # initialize que
        self.in_order_traversal_helper(self.root, que) # call helper and using the root node and que as arguments
        return que

    def in_order_traversal_helper(self, cur_node, que):
        """helper function for in order traversal"""
        if cur_node == None: # return once traversal is completed
            return

        else:
            self.in_order_traversal_helper(cur_node.left, que) # move node left
            que.enqueue(cur_node.value) # add value
            self.in_order_traversal_helper(cur_node.right, que) # move node right

    def post_order_traversal(self) -> Queue:
        """post order traversal function outputs the values of the BST in the que as it is traversed FROM THE RIGHT.
        A helper function is used to help with recursive calls"""
        que = Queue() # initialize que
        self.post_order_traversal_helper(self.root, que) # call helper and using the root node and que as arguments
        return que

    def post_order_traversal_helper(self, cur_node, que):
        """helper function for post order traversal"""
        if cur_node == None: # return once traversal is complete
            return

        else:
            self.post_order_traversal_helper(cur_node.left, que) # move node left
            self.post_order_traversal_helper(cur_node.right, que) # move node right
            que.enqueue(cur_node.value) # add value

    def by_level_traversal(self) -> Queue:
        """by level traversal creates two ques. It uses the first queue to travers through the list in left to right
        order, and the second queue is used to store the outputs once they are passed."""
        que = Queue() # first queue used for traversal
        final_que = Queue() # second queue to produce the output
        que.enqueue(self.root) # initialize root

        while que.is_empty() != True:
            N = que.dequeue() # initialize dequeue
            if N != None:
                final_que.enqueue(N.value) # add value once node is passed passed
                que.enqueue(N.left) # move left
                que.enqueue(N.right) # move right
        return final_que

    def is_full(self) -> bool:
        """is full function creates a que and traverses through the que to see if the BST is considered a full binary
        tree. A full binary tree is true when all interior nodes have exactly two children. An empty tree and a
        single root node is also considered full"""
        full_que = Queue() # initialize full que
        self.is_full_helper(self.root, full_que) # call helper function
        if self.size() == 1 or self.size() == 0: # if size is 0 and 1 return True
            return True
        else:
            while full_que.is_empty() != True:
                pointer = full_que.dequeue()
                # checks if all interior nodes have two children, if not return false
                if pointer.left == None and pointer.right != None or pointer.left != None and pointer.right == None:
                    return False
        return True

    def is_full_helper(self, curr_node, full_que):
        """is full helper function"""
        if curr_node == None:  # return once traversal is completed
            return
        else:
            full_que.enqueue(curr_node)  # add value
            self.is_full_helper(curr_node.left, full_que)  # move node left
            self.is_full_helper(curr_node.right, full_que)  # move node right


    # couldn't figure out how to complete the is complete function. I commented my thought process below
    def is_complete(self) -> bool:
        """is_complete function checks if most of the nodes are on the left side. Follows the same process as the height
        function where left and right side depth is compared"""
        return self.is_complete_helper(self.root)

    def is_complete_helper(self, curr_node):
        """helper for is complete function"""
        if curr_node == None: # if BST is empty return Tre
            return True
        else:
            # compares the height of the left and right side. If left side is higher, return True
            left_side = self.height_helper(curr_node.left) # traverse down the left side
            right_side = self.height_helper(curr_node.right) # traverse down the right side
            if left_side > right_side: # since left side depth is higher, that means that the BST is complete
                return True
            else:
                return False




    def is_perfect(self) -> bool:
        """is perfect function checks if the BST is a perfect binary tree which means that all interior nodes
        have the same children and all the leaves are the same depths. According to Exploration: Binary Trees -
        Types/States of Binary Trees. We know that a BST is perfect if it has 2^h total leaves. The code below
        replicates this equation and checks it against the total leaves to determine if it's true"""
        if self.size() == 1 or self.size() == 0: # if size is 0 and 1 return True
            return True
        if self.is_full() == False: # if is_full is false then it cannot be perfect
            return False
        else:
            total_height = self.height() # initialize total height
            all_leaves = 1 # intialize total leaves
            while total_height != 0:
                all_leaves = all_leaves * 2 # keep multiplying the leaves by 2 until height reaches 0
                total_height -= 1
            if self.count_leaves() != all_leaves: # check if numbers match, and if they don't, return False
                return False
        return True

    def size(self) -> int:
        """size function determines the size of the current BST by counting the total number of nodes. A helper function
        is used to help with the recursive calls"""
        size_que = Queue() # initialize queue
        self.size_helper(self.root, size_que) # call size helper function
        size_counter = 0 # initialize size counter
        while size_que.is_empty() != True:
            size_que.dequeue() # keep dequeue until queue is empty
            size_counter += 1 # increment the size counter by 1 every time dequeue is called
        return size_counter

    def size_helper(self, curr_node, size_que):
        """size helper function"""
        if curr_node == None:  # return once traversal is completed
            return
        else:
            size_que.enqueue(curr_node)  # add value
            self.size_helper(curr_node.left, size_que)  # move node left
            self.size_helper(curr_node.right, size_que)  # move node right

    def height(self) -> int:
        """height function returns the height of the BST. An empty tree has a height of -1, and a tree consisting of a
        single root node has a height of 0. A helper function is used for the recursive call"""
        return self.height_helper(self.root)

    def height_helper(self, curr_node):
        """helper for height function"""
        if curr_node == None: # if BST is empty return -1
            return -1
        else:
            # compares the height of the left and right side. Max function is used to output the highest number
            left_side = self.height_helper(curr_node.left) # traverse down the left side
            right_side = self.height_helper(curr_node.right) # traverse down the right side
            return max(left_side + 1, right_side + 1) # add 1 since height starts at - 1

    def count_leaves(self) -> int:
        """count leaves function counts the leaves of the BST by checking with the nodes that have no children.
        If tree is empty, leaf counter returns 0. First, a queue is made to store all the nodes. A helper function is
        called which copies the traversal methods. The main function then checks if each node is a leaf. If a node is
        a leaf, the counter is incremented by 1."""
        leaf_que = Queue() # queue is initialized
        self.count_leaves_helper(self.root, leaf_que) # helper is called
        leaf_counter = 0 # counter is set
        while leaf_que.is_empty() != True:
            pointer = leaf_que.dequeue() # removes node after it is passed
            if pointer.left == None and pointer.right == None: # checks if node is a leaf
                leaf_counter += 1 # increment counter if leaf is found
        return leaf_counter

    def count_leaves_helper(self, curr_node, leaf_que):
        """count leaves helper function"""
        if curr_node == None: # return once traversal is completed
            return
        else:
            leaf_que.enqueue(curr_node) # add value
            self.count_leaves_helper(curr_node.left, leaf_que) # move node left
            self.count_leaves_helper(curr_node.right, leaf_que) # move node right

    def count_unique(self) -> int:
        """count unique function returns the count of unique values stored in the BST. If there are no unique values,
        it returns the same value as the size method"""
        unique_que = Queue()  # initialize queue
        self.count_unique_helper(self.root, unique_que)  # call count unique helper function
        prev_node = None # initialize prev node
        unique_counter = 0  # initialize unique counter
        while unique_que.is_empty() != True:
            pointer = unique_que.dequeue()  # keep dequeue until queue is empty
            if pointer == prev_node: # checks if nodes have the same value
                unique_counter -= 1  # decrement the size counter by 1 if values are not unique
            unique_counter += 1 # increment by 1
            prev_node = pointer # move along the BST
        return unique_counter

    def count_unique_helper(self, curr_node, unique_que):
        """counter unique helper function and needs to follow the same process as the in order traversal so it can
        compare the same values next to each other."""
        if curr_node == None:  # return once traversal is completed
            return
        else:
            self.count_unique_helper(curr_node.left, unique_que)  # move node left
            unique_que.enqueue(curr_node.value)  # add value
            self.count_unique_helper(curr_node.right, unique_que)  # move node right



# BASIC TESTING - PDF EXAMPLES

if __name__ == '__main__':
    """ add() example #1 """
    print("\nPDF - method add() example 1")
    print("----------------------------")
    tree = BST()
    print(tree)
    tree.add(10)
    tree.add(15)
    tree.add(5)
    print(tree)
    tree.add(15)
    tree.add(15)
    print(tree)
    tree.add(5)
    print(tree)

    """ add() example 2 """
    print("\nPDF - method add() example 2")
    print("----------------------------")
    tree = BST()
    tree.add(10)
    tree.add(10)
    print(tree)
    tree.add(-1)
    print(tree)
    tree.add(5)
    print(tree)
    tree.add(-1)
    print(tree)

    """ contains() example 1 """
    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = BST([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    """ contains() example 2 """
    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = BST()
    print(tree.contains(0))

    """ get_first() example 1 """
    print("\nPDF - method get_first() example 1")
    print("----------------------------------")
    tree = BST()
    print(tree.get_first())
    tree.add(10)
    tree.add(15)
    tree.add(5)
    print(tree.get_first())
    print(tree)

    """ remove() example 1 """
    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    tree = BST([10, 5, 15])
    print(tree.remove(7))
    print(tree.remove(15))
    print(tree.remove(15))

    """ remove() example 2 """
    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.remove(20))
    print(tree)

    """ remove() example 3 """
    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    tree = BST([10, 5, 20, 18, 12, 7, 27, 22, 18, 24, 22, 30])
    print(tree.remove(20))
    print(tree)
    # comment out the following lines
    # if you have not yet implemented traversal methods
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ remove_first() example 1 """
    print("\nPDF - method remove_first() example 1")
    print("-------------------------------------")
    tree = BST([10, 15, 5])
    print(tree.remove_first())
    print(tree)

    """ remove_first() example 2 """
    print("\nPDF - method remove_first() example 2")
    print("-------------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7])
    print(tree.remove_first())
    print(tree)

    """ remove_first() example 3 """
    print("\nPDF - method remove_first() example 3")
    print("-------------------------------------")
    tree = BST([10, 10, -1, 5, -1])
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)

    """ Traversal methods example 1 """
    print("\nPDF - traversal methods example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Traversal methods example 2 """
    print("\nPDF - traversal methods example 2")
    print("---------------------------------")
    tree = BST([10, 10, -1, 5, -1])
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Comprehensive example 1 """
    print("\nComprehensive example 1")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'  N/A {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in [10, 5, 3, 15, 12, 8, 20, 1, 4, 9, 7]:
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print()
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Comprehensive example 2 """
    print("\nComprehensive example 2")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'N/A   {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in 'DATA STRUCTURES':
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print('', tree.pre_order_traversal(), tree.in_order_traversal(),
          tree.post_order_traversal(), tree.by_level_traversal(),
          sep='\n')

