# Name: Sheng Feng
# OSU Email: fengsh@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 2
# Due Date: 05/01/2023
# Description: Build methods to manage additional functionality for a dynamic array


from static_array import StaticArray


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'

    def __iter__(self):
        """
        Create iterator for loop
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Obtain next value and advance iterator
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        try:
            value = self[self._index]
        except DynamicArrayException:
            raise StopIteration

        self._index += 1
        return value

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the capacity of the array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    def print_da_variables(self) -> None:
        """
        Print information contained in the dynamic array.
        Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """
        Resize the underlying storage for the dynamic array based on the new_capacity parameter.
        """

        # ensure the new capacity is valid size
        if new_capacity >= self.length() and new_capacity > 0:

            # create a new static array with new_capacity size
            resize_array = StaticArray(new_capacity)

            # copy data from old static array to new static array
            for number in range(self.length()):
                resize_array[number] = self.get_at_index(number)

            # update capacity size variable
            self._capacity = new_capacity

            # point underlying storage to the new static array
            self._data = resize_array
        pass

    def append(self, value: object) -> None:
        """
        Append a new value to the dynamic array
        """

        current_capacity = self.get_capacity()
        current_length = self.length()

        # resize array if necessary
        if (current_length + 1) > current_capacity:
            self.resize(current_capacity * 2)

        # update size variable
        self._size += 1

        # insert value into array at the end
        self.set_at_index(current_length, value)
        pass

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Add a value to the dynamic array at the index value passed into the function
        """
        current_capacity = self.get_capacity()
        current_length = self.length()

        # ensure the index is valid
        if index < 0 or index > current_length:
            raise DynamicArrayException

        # resize array if necessary
        if current_length == current_capacity:
            self.resize(current_capacity * 2)

        # update size variable to account for added value
        self._size += 1

        # move every value after the index parameter one space right, loop backwards to potential work
        for number in range(current_length, index - 1, -1):
            insert_move = self.get_at_index(number)
            if insert_move is not None:
                self.set_at_index(number + 1, insert_move)
        self.set_at_index(index, value)

        pass

    def remove_at_index(self, index: int) -> None:
        """
        Remove a value from the dynamic array at the index value passed into the function
        """
        current_capacity = self.get_capacity()
        current_length = self.length()

        # ensure the index is valid
        if index < 0 or index >= current_length:
            raise DynamicArrayException

        # resize array if necessary, do not go under 10 capacity
        if current_length < (0.25 * current_capacity) and current_capacity > 10:
            altered_capacity = (current_length * 2)
            if altered_capacity < 10:
                self.resize(10)
            else:
                self.resize(altered_capacity)

        # move all values after the index parameter one space left
        for number in range(index, current_length - 1):
            self.set_at_index(number, self.get_at_index(number+1))
            self.set_at_index(number + 1, None)
        self._size = self._size - 1

        pass

    def slice(self, start_index: int, size: int) -> "DynamicArray":
        """
        Slice a section of dynamic array and return it as a separate dynamic array
        """

        current_capacity = self.get_capacity()
        current_length = self.length()

        # ensure the start_index is valid
        if start_index < 0 or start_index > (current_length - 1) or size < 0:
            raise DynamicArrayException

        # ensure the size is not too large
        if size > (current_length - start_index):
            raise DynamicArrayException

        # create a new array to store the slice
        slice_array = DynamicArray()

        slice_counter = 0
        slice_index = start_index

        # add values from dynamic array from start_index until size is reached
        while slice_counter < size:
            insert_value = self.get_at_index(slice_index)
            slice_array.append(insert_value)
            slice_index += 1
            slice_counter += 1

        return slice_array

        pass

    def merge(self, second_da: "DynamicArray") -> None:
        """
        merge a second dynamic array into this one
        """
        merge_length = second_da.length()
        merge_index = 0

        while merge_length > 0:
            self.append(second_da.get_at_index(merge_index))
            merge_index += 1
            merge_length = merge_length - 1

        pass

    def map(self, map_func) -> "DynamicArray":
        """
        Apply a function to each value in the dynamic array and return results in a new dynamic array
        """
        map_array = DynamicArray()
        current_length = self.length()

        for number in range(0, current_length):
            map_value = self.get_at_index(number)
            map_array.append(map_func(map_value))

        return map_array
        pass

    def filter(self, filter_func) -> "DynamicArray":
        """
        Apply a function to each value in the dynamic array and append only the values that return "True" to a new dynamic array.
        Return that new dynamic array.
        """
        filter_array = DynamicArray()
        current_length = self.length()

        for number in range(0, current_length):
            filter_value = self.get_at_index(number)
            if filter_func(filter_value) is True:
                filter_array.append(filter_value)

        return filter_array

        pass

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        Apply a function to the first two values and store the result.
        Then apply that function to the stored result and the next value, repeat until the last value is reached.
        The initializer, when present, becomes the very first value.
        """

        # logic to handle when the array has too few values to reduce normally
        if initializer is not None and self.length() < 1:
            return initializer

        if initializer is None and self.length() == 0:
            return None

        if initializer is None and self.length() == 1:
            return self.get_at_index(0)

        current_length = self.length()

        # logic when there is no initializer
        if initializer is None:
            result1 = self.get_at_index(0)
            result2 = self.get_at_index(1)
            reduce_storage = reduce_func(result1, result2)

            for number in range(2, current_length):
                reduce_storage = reduce_func(reduce_storage, self.get_at_index(number))

            return reduce_storage

        # logic when there is an initializer
        if initializer is not None:
            result1 = initializer
            result2 = self.get_at_index(0)
            reduce_storage = reduce_func(result1, result2)

            for number in range(1, current_length):
                reduce_storage = reduce_func(reduce_storage, self.get_at_index(number))

            return reduce_storage
        pass


def find_mode(arr: DynamicArray) -> (DynamicArray, int):
    """
    Find the mode value(s) in a dynamic array.
    Return a tuple with all mode values in a dynamic array and how often they appear.
    """
    find_array = DynamicArray()
    array_length = arr.length()

    current_count = 1
    current_mode = 1

    for number in range(1, array_length):
        if arr[number] == arr[number - 1]:
            current_count += 1
            if current_count > current_mode:
                current_mode = current_count
        elif arr[number] != arr[number - 1]:
            if current_count > current_mode:
                current_mode = current_count
            current_count = 1

    current_count = 1
    if current_count == current_mode:
        find_array.append(arr[0])

    for number in range(1, array_length):
        if arr[number] == arr[number - 1]:
            current_count += 1
            if current_count == current_mode:
                find_array.append(arr[number])
        elif arr[number] != arr[number - 1]:
            current_count = 1
            if current_count == current_mode:
                find_array.append(arr[number])

    result = (find_array, current_mode)

    return result
    pass
