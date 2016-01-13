__author__ = 'Grant Lubeck'
__email__ = 'gdlubeck@gmail.com'

import unittest
from unrolled_linked_list import UnrolledLinkedList

'''
> Implement your tests here

To run your tests, just run `python tests.py`
'''


class ExampleTest(unittest.TestCase):
    """ Demonstrates how the unittest framework works """

    def test_example(self):
        #----------------------appending test------------------------------------
        list_one = UnrolledLinkedList(max_node_capacity=8)
        self.assertIsNotNone(list_one)
        list_one.append(0)
        list_one.append(1)
        list_one.append(2)
        list_one.append(3)
        list_one.append(4)
        list_one.append(5)
        list_one.append(6)
        list_one.append(7)

        self.assertTrue(str(list_one)=="{[0,1,2,3,4,5,6,7]}")

        list_one.append(8)
        self.assertTrue(str(list_one)=="{[0,1,2,3], [4,5,6,7,8]}")

        list_one.append(9)
        list_one.append(10)
        list_one.append(11)
        list_one.append(12)
        self.assertTrue(str(list_one)=="{[0,1,2,3], [4,5,6,7], [8,9,10,11,12]}")

        #----------------------deleting test------------------------------------
        del list_one[-2]
        self.assertTrue(str(list_one)=="{[0,1,2,3], [4,5,6,7], [8,9,10,12]}")

        del list_one[3]
        self.assertTrue(str(list_one)=="{[0,1,2,4,5,6,7], [8,9,10,12]}")

        list_one.append(13)
        list_one.append(14)

        del list_one[0]
        del list_one[0]
        del list_one[0]
        del list_one[0]
        self.assertTrue(str(list_one)=="{[5,6,7,8,9], [10,12,13,14]}")

        #----------------------adding test------------------------------------
        list_two = UnrolledLinkedList(max_node_capacity=8)
        list_two.append(15)
        list_two.append(16)
        list_two.append(17)
        list_two.append(18)

        list_three = list_one + list_two
        self.assertTrue(str(list_three)=="{[5,6,7,8], [9,10,12,13], [14,15,16,17,18]}")       

        #----------------------getitem test------------------------------------
        self.assertTrue(list_three[0]==5)
        self.assertTrue(list_three[4]==9)
        self.assertTrue(list_three[8]==14)
        self.assertTrue(list_three[-1]==18)
        self.assertTrue(list_three[-6]==13)

        #----------------------setitem test------------------------------------
        list_three[0]=100
        self.assertTrue(list_three[0]==100)
        list_three[4]=101
        self.assertTrue(list_three[4]==101)
        list_three[-5]=200
        self.assertTrue(list_three[-5]==200)

        #----------------------iter test------------------------------------
        test = ""
        for i in list_three:
            test+=str(i)+" "
        self.assertTrue(test=="100 6 7 8 101 10 12 13 200 15 16 17 18 ")

        #----------------------reversed iter test------------------------------------
        test = ""
        for i in reversed(list_three):
            test+=str(i)+" "
        self.assertTrue(test=="18 17 16 15 200 13 12 10 101 8 7 6 100 ")

        #----------------------length test------------------------------------
        self.assertTrue(len(list_one)==9)
        self.assertTrue(len(list_two)==4)
        self.assertTrue(len(list_three)==13)

        #----------------------contains test------------------------------------
        self.assertTrue(200 in list_three)
        self.assertTrue(100 in list_three)
        self.assertTrue(15 in list_three)
        self.assertTrue(15 in list_two)
        self.assertFalse(15 in list_one)

        #----------------------mulitply test------------------------------------
        list_four = UnrolledLinkedList(max_node_capacity=8)
        list_four.append(1)
        list_four.append(2)
        list_four.append(3)
        list_four.append(4)
        list_four.append(5)
        list_four*=2
        self.assertTrue(str(list_four)=="{[1,2,3,4], [5,1,2,3,4,5]}")
        list_four*=3
        self.assertTrue(str(list_four)=="{[1,2,3,4], [5,1,2,3], [4,5,1,2], [3,4,5,1], [2,3,4,5], [1,2,3,4], [5,1,2,3,4,5]}")


if __name__ == '__main__':
    unittest.main()
