__author__ = 'Your Name'
__email__ = 'Your Email'


class UnrolledLinkedList(object):
    """ This is the container class for your unrolled linked list """

    class Node(object):
        """ This is the node object you should use within your unrolled linked
            list
        """

        def __init__(self):
            self.nextNode = None
            self.array = []

    def __init__(self, max_node_capacity=16):
        """  The constructor for the list.
        """
        self.start = None
        self.end = None
        self.max_node_capacity = max_node_capacity
        self.size_of_list = 0


    def __add__(self, other):
        """ Appends two Unrolled Linked Lists end-to-end using `+`
        """
        if not isinstance(other, UnrolledLinkedList):
            raise TypeError(str(type(other)) + " is not compatible with " + str(type(self)))

        new_list = UnrolledLinkedList(max_node_capacity=self.max_node_capacity)
        
        for i in range(0, self.size_of_list):
            new_list.append(self[i])

        for i in range(0, other.size_of_list):
            new_list.append(other[i])

        return new_list

    def __mul__(self, count):
        """ Repeats (multiplies) the list a given number of times

        """
        if type(count) != int:
            raise TypeError("Input argument count: " + str(count) + " is not an int")

        new_list = UnrolledLinkedList(max_node_capacity=self.max_node_capacity)
        for i in range(0, count):
            for j in range(0, self.size_of_list):
                new_list.append(self[j])
        return new_list

    def __getitem__(self, index):
        """ Access the element at the given index.
        """
        originalIndex = index
        if index < 0:
            index = self.size_of_list + index
        if index > self.size_of_list-1 or index < 0:
            raise IndexError(str(originalIndex) + ' Not a Valid Index')

        currentNode = self.start
        while(index > 0):
            if(index - len(currentNode.array) >= 0):
                index -= len(currentNode.array)
                currentNode = currentNode.nextNode
            else:
                break
        
        if type(currentNode.array[index]) != int:
            raise TypeError("Value at index " + str(originalIndex) + " is not an int")
        else:
            return currentNode.array[index]

    def __len__(self):
        """Return the total number of items in the list
        """
        return self.size_of_list

    def __setitem__(self, index, value):
        """ Sets the item at the given index to a new value
        """
        originalIndex = index
        if index < 0:
            index = self.size_of_list + index

        if index > self.size_of_list-1 or index < 0:
            raise IndexError(str(originalIndex) + ' Not a Valid Index')

        currentNode = self.start
        while(index > 0):
            if(index - len(currentNode.array) >= 0):
                index -= len(currentNode.array)
                currentNode = currentNode.nextNode
            else:
                break
        if type(currentNode.array[index]) != int:
            raise TypeError("Value at index " + str(originalIndex) + " is not an int")
        else:
            currentNode.array[index] = value

    def __delitem__(self, index):
        """ Deletes an item using the built-in `del` keyword
        """
        originalIndex = index
        if index < 0:
            index = self.size_of_list + index

        if index > self.size_of_list-1 or index < 0:
            raise IndexError(str(originalIndex) + ' Not a Valid Index')

        currentNode = self.start
        while(index > 0):
            if(index - len(currentNode.array) >= 0):
                index -= len(currentNode.array)
                currentNode = currentNode.nextNode
            else:
                break
        del currentNode.array[index]
        self.size_of_list -= 1

        next = currentNode.nextNode
        if len(currentNode.array) < self.max_node_capacity/2 and next is not None:
            numberOfElementsNeeded = self.max_node_capacity/2 - len(currentNode.array) + 1
            currentNode.array = currentNode.array + next.array[:numberOfElementsNeeded]
            next.array = next.array[numberOfElementsNeeded:]
            if len(next.array) < self.max_node_capacity/2:
                currentNode.array = currentNode.array + next.array
                currentNode.nextNode = next.nextNode
                del next



    def __iter__(self):
        """ Returns an iterable to allow one to iterate the list.
        """
        currentNode = self.start
        while currentNode is not None:
            for i in currentNode.array:
                yield i
            currentNode = currentNode.nextNode

    def __contains__(self, item):
        """ Returns True/False whether the list contains the given item
        """
        for i in self:
            if i == item:
                return True
        return False

    def append(self, data):
        """ Add a new object to the end of the list.
        """
        self.size_of_list += 1
        if self.start is None:
            self.start = self.Node()
            self.start.array.append(data)
            self.end = self.start

        elif(len(self.end.array) < self.max_node_capacity):
            self.end.array.append(data)
        
        else:
            newNode = self.Node()
            newNode.array = self.end.array[len(self.end.array)/2:]
            self.end.array = self.end.array[:len(self.end.array)/2]
            self.end.nextNode = newNode
            self.end = newNode
            self.end.array.append(data)



    def __reversed__(self):
        """ Works just like __iter__, but starts from the back.
        """
        index = self.size_of_list-1

        while index>=0:
            yield self[index]
            index-=1

    def __str__(self):
        """ Returns a string representation of the list.
        """
        if self.size_of_list == 0:
            return "empty"
        else:
            string = "{"
            node = self.start
            while(node is not None):
                string+="["
                for index in range(0,len(node.array)):
                    string+=str(node.array[index])
                    if index+1 < len(node.array):
                        string+=","
                string+="]"
                if node.nextNode is not None:
                    string+=", "
                node = node.nextNode
            string+="}"
            return string
