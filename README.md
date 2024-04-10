# Data-Structures

This repo includes two classes that represent the **dynamic array** and **bag** data structures coded in Python. 
The assignment is done without reliance on any of Python's built-in data structures and all processing is done iteratively to demonstrate our understanding of how these two fundamental data structures work under the hood. 

## Dynamic Array
Code included in **dyanmic_array.py** and utilizes **static_array.py** as an underlying data structure (provided by the instructor). 

Functionality created from class methods:
* Insert, remove, or append values to the dynamic array
* Slice and merge dynamic arrays
* map, filter, and reduce array elements via function in the input parameter
* Find the mode of an array

Whenever a dynamic array is full, it will automatically double in size to accommodate additional elements. 
If the array is less than 1/4 full, it will resize to 2x the current number of elements as long as the new size is >= 10.

## Bag
Code included in **bag_da.py** and relies on **dynamic_array.py** as an underlying data structure. 

Functionality created from class methods:
* Add or remove elements from the bag
* Count instances of a specific element in the bag
* Clear bag
* Evaluate if two bags are equal
* Iterators for the bag

## Usage Instructions
Download all three files into a local directory. 
Open files directly in an IDE (such as Pycharm) to test functionality or import into a new Python file to test separately. 
