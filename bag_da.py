# Name: Sheng Feng
# OSU Email: fengsh@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 2
# Due Date: 05/01/2023
# Description: Build methods manage additional functionality for a bag ADT

from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(_))
                          for _ in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        Add an item to the bag
        """
        self._da.append(value)
        pass

    def remove(self, value: object) -> bool:
        """
        Remove an item from the bag
        """
        array_length = self._da.length()
        for number in range(array_length):
            if self._da.get_at_index(number) == value:
                self._da.remove_at_index(number)
                return True
        else:
            return False
        pass

    def count(self, value: object) -> int:
        """
        Count the instances of an item in the bag
        """
        value_counter = 0
        array_length = self._da.length()

        for number in range(array_length):
            if self._da.get_at_index(number) == value:
                value_counter += 1
        return value_counter

        pass

    def clear(self) -> None:
        """
        Clear all contents of the bag
        """
        new_array = DynamicArray()
        self._da = new_array
        pass

    def equal(self, second_bag: "Bag") -> bool:
        """
        Determine if two bags contain the exact same items in equal quantities. Two empty bags are equal.
        """
        array_length = self._da.length()

        # check if the overall number of items in both bags are equal
        if self._da.length() != second_bag._da.length():
            return False

        # check if the quantity of each item in bag 1 is the same as bag 2
        for number in range(array_length):
            lookup_value = self._da[number]
            original_count = 0
            bag_count_count = 0
            for number2 in range(array_length):
                if self._da[number2] == lookup_value:
                    original_count +=1
                if second_bag._da[number2] == lookup_value:
                    bag_count_count +=1
            if original_count != bag_count_count:
                return False
        return True

        pass

    def __iter__(self):
        """
        Create iterator for loop
        """
        self._index = 0

        return self

        pass

    def __next__(self):
        """
        Obtain next value and advance iterator
        """
        try:
            value = self._da[self._index]
        except DynamicArrayException:
            raise StopIteration

        self._index += 1
        return value

        pass