#!python

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self): # O(n)
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self): # O(1)
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self): # O(n)
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each
        currentNode = self.head
        nodeLength = 0
        while currentNode != None:
            nodeLength += 1
            currentNode = currentNode.next
        return nodeLength

    def append(self, item): # O(1)
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists
        newNode = Node(item)

        # currentNode = self.head
        # while currentNode != None:
        #     currentNode = currentNode.next
        # currentNode = newNode
        # self.tail.next = currentNode
        # self.tail = currentNode


        if self.is_empty():
            self.head = newNode
        else:
            self.tail.next = newNode
        self.tail = newNode



    def prepend(self, item): # O(1)
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        newNode = Node(item)
        if self.is_empty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head

        self.head = newNode

    def find(self, quality): # O(n)
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        currentNode = self.head
        while currentNode != None:
            if currentNode.data == quality:
                return currentNode
            currentNode = currentNode.next
        return None

    def delete(self, item): # O(n)
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))

        # currentNode = self.head
        # while currentNode != None:
        #     lastNode = currentNode
        #     currentNode = currentNode.next
        #     if currentNode == item:
        #         lastNode.next = currentNode.next
        #         return

        node = self.head  # O(1) time to assign new variable
        previous_node = None # O(1) time/space
        # Loop until node is None, which is one node too far past tail
        find_item = self.find(lambda item_: item_ == item) # O(n) time/O(1) space
        if find_item is None:
            raise ValueError('Item not found: {}'.format(item)) # O(1) time/space
        else:
            for node in self: # best case running time: O(1), worst case running time: O(n)
                if node == self.head:
                    if node.data == item:
                        self.head = node.next # O(1) time/space
                        if node == self.tail:
                            self.tail = previous_node # O(1) time/space
                        break
                    else:
                        previous_node = node # O(1) time/space
                else:
                    if node.data == item:
                        previous_node.next = node.next # O(1) time/space
                        if node == self.tail:
                            self.tail = previous_node # O(1) time/space
                        break
                    else:
                        previous_node = node # O(1) time/space




def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
