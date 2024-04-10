# CSC148 Final Review

## Outline
- [Memory Model](#memory-model)
    - [Variables](#variables)
    - [Storage Patterns](#storage-patterns)
    - [List Copy Logic](#list-copy-logic)
    - [Python Features](#python-features)
- [Object-Oriented Programming (OOP)](#object-oriented-programming-oop)
    - [Classes and Objects](#classes-and-objects)
    - [Inheritance](#inheritance)
    - [Polymorphism](#polymorphism)
    - [Abstraction](#abstraction)
    - [Representation Invariant (RI)](#representation-invariant-(ri))
    - [Special Methods](#special-methods)
- [Exception Handling](#exception-handling)
- [Recursion](#recursion)
- [Sorting Algorithms](#sorting-algorithms)
    - [Merge Sort](#merge-sort)
    - [Quick Sort](#quick-sort)
- [Data Structures](#data-structures)
    - [Linked Lists](#linked-lists)
    - [Stacks and Queues](#stacks-and-queues)
    - [Trees](#trees)
- [Conclusion](#conclusion)

## Memory Model
### Variables
+ Variables store the memory address of instances (objects) `id(var)`
+ The equal sign `=` is used to assign values to variables, for example: `a = 1` assigns `id(1)` to the variable `a`
```python
a = 1
b = 1

a == b # True
a is b # True
```

### Storage Patterns

+ When creating a "container" — `list`, `dict`, `object`
    + Create outer variables first, then inner variables.

### List Copy Logic
```python
lst = [1,2]
new_lst = lst
# new_lst stores id(lst)
# Changing new_lst[i] will also change lst[i]
new_lst.append(3)
print(lst) # [1, 2, 3]

lst = [1, 2]
lst_copy = lst[:] # or lst.copy()
# Here, lst_copy = [id(1), id(2)] 

lst_copy.append(3)
print(lst) # [1,2]
```

Q: Does this code below behave correctly? Why or why not?
```python
def replace(lst: list[int], val: int, new_val: int) -> None:
"""Replaces the first instance of <val> in <lst> with <new_val>.
>>> lst = [0, 1, 2]
>>> replace(lst, 0, 10)
>>> lst == [10, 1, 20]
True
"""
if len(lst) > 0:
    if lst[0] == val:
        lst[0] = new_val
    else:
        replace(lst[1:], val, new_val)

if __name__ == '__main__':
    l = [1, 6, 0]
    replace(l, 6, 12)
    print(l)
```
A: No, the code does not behave correctly. The function recursively calls itself with replace(lst[1:], val, new_val). However, it does not update the original list `lst` with the modified sublist bcz `lst[1:]` have different ID with `lst`

### Python Features
+ When creating immutable instances, Python, to save memory, does not create new instances actively. It first looks in memory to see if the instance exists. If it does, it directly references the address of that instance; otherwise, it creates a new instance.
    + For example, Python pre-creates instances of numbers `1~256` in memory, and when used, Python directly uses these pre-created instances of numbers.
+ `lst.extend([1,2,3])` is equivalent to `lst += [1,2,3]`
    + Both do not change the ID of `lst`

## Object-Oriented Programming (OOP)
Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects", which can contain data and code: data in the form of fields (often known as attributes or properties), and code, in the form of procedures (often known as methods).
### Key Concepts of OOP

- **Classes**: The blueprint for creating objects (instances).
  
  ```python
  class ClassName:
      # class body
  ```

- **Objects**: Instances of a class.

  ```python
  object_name = ClassName()
  ```

- **Attributes**: Variables that belong to a class or instance.

  ```python
  class ClassName:
      class_attribute = 'some value'  # Class attribute
      def __init__(self, value):
          self.instance_attribute = value  # Instance attribute
  ```

- **Methods**: Functions that belong to a class or instance.

  ```python
  class ClassName:
      def instance_method(self):
          # method body
  ```

### Inheritance
Inheritance is one of the fundamental concepts of Object-Oriented Programming (OOP). It allows a class to inherit attributes and methods from another class, enabling code reusability and the creation of hierarchical structures.

- Python supports single-inheritance, meaning each class can inherit from only one parent class.
- Subclasses can access and use attributes and methods from their parent class, which fosters code reuse and simplifies maintenance.
  - If a method is redefined in a subclass, it overrides the parent class's method, and the subclass's version is used.
  - To explicitly call an overridden method of a parent class, you can use:
    - `ParentClass.method_name(self, arguments)` for calling a specific parent class method.
    - `super().method_name(arguments)` for calling the next method in the method resolution order.

- The concept of privacy in Python:
  - Python does not have true private variables, but conventionally, a name prefixed with an underscore is intended for internal use.
  - Single underscore (`_`) before a name is meant as a hint for internal use, e.g., `self._internal_var` or `def _internal_method(self):`.

- Type and instance checks in Python:
  - `type(obj)` is used for checking the type of an object, which does not consider inheritance.
  - `isinstance(obj, class)` checks if an object is an instance of a class or of a subclass thereof, hence taking inheritance into account.

```python
class Parent:
    pass

class Child(Parent):
    pass

parent_instance = Parent()
child_instance = Child()

# Type checking does not consider inheritance.
type(parent_instance) == type(child_instance)  # False

# Instance checking takes inheritance into account.
isinstance(child_instance, Parent)  # True, because Child inherits from Parent.
```

### Polymorphism
Polymorphism lets us perform the same action in different ways, depending on what we're performing it on.

- It means you can use a single type of operation in different ways for different data inputs.
- You can call the same method on different objects, and each object can respond in its own way.

```python
class Bird:
    def speak(self):
        print("Tweet tweet!")

class Dog:
    def speak(self):
        print("Bark bark!")

def make_sound(animal):
    animal.speak()

# Both Bird and Dog can 'speak', but they sound different.
sparrow = Bird()
rover = Dog()

make_sound(sparrow)  # Outputs: Tweet tweet!
make_sound(rover)    # Outputs: Bark bark!
```
### Abstraction
A class with abstract methods

+ Abstract method: In a method, if there is only one line `raise NotImplementedError`, it is called an abstract method
    + It's worth noting that a method that only raises `NotImplementedError` is not a true abstract method, as Python will not prevent us from creating an instance of this method (in other words, Python will not prevent us from creating an instance of this abstract class). The correct way to create an abstract method is to use the `@abstractmethod` decorator to create an abstract method.

        ```Python 
        class A:
            def foo():
                raise NotImplementedError

        class B(A):
            def foo():
                ... # some code here
        ```

        In the above example, class A is an abstract class because it has an abstract method foo().

### Representation Invariant (RI)
A Representation Invariant is a condition that holds true during the lifetime of an object. It's kind like precondition for class
+ For regular variables and methods, we need to specify the type of the variable and the return value of the method

    ```Python
    class A:
        num: int
        name: str

        def foo(self, num: int, name: str) -> None:
            ...
    ```
+ For conditional variables, such as the length of a tweet not exceeding 280 characters, there are three ways to limit this condition
    + By limiting the precondition
        + When using this method, we assume that all inputs are correct, and the person using our method needs to confirm whether the conditions are met before inputting, for example:
        
        ```Python
        class Tweet:
            """
            === Representation Invariant ===
            content: len(content) <= 280
            """
            content: str

            def set_content(self, content: str) -> None:
                """
                Precondition: len(content) <= 280
                """
                self.content = content
        ```
    + If the input parameters do not meet the conditions, do nothing
        + This method is also called failing silently

        ```Python
        class Tweet:
            """
            === Representation Invariant ===
            content: len(content) <= 280
            """
            content: str

            def set_content(self, content: str) -> None:
                if len(content) <= 280:
                    self.content = content
        ```
    + Implicitly fix the problem within the method
        + When using this method, we do not impose any conditions on the input, but when processing the input, we repair the input that does not meet the conditions to meet the conditions (for example: using a qualified parameter to replace, deleting part of the input that does not meet the conditions, etc.)

        ```Python
        class Tweet:
            """
            === Representation Invariant ===
            content: len(content) <= 280
            """
            content: str

            def set_content(self, content: str) -> None:
                self.content = content[:280]
        ```

### Special Methods
Python's special methods enable us to define how objects behave within various operations. Here, we focus on several foundational special methods that allow objects to interact with built-in Python functionalities.

+ `__init__(self, [...])`

    Initializes a new instance of a class.

    ```python
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    ```

+ `__str__(self)`

    Returns a string representation of an object, used by the `print()` function and `str() `conversion.

    ```python
    class Person:
        def __str__(self):
            return f"Person(name={self.name}, age={self.age})"
    ```
+ `__getitem__(self, key)`

    Allows access to elements using square brackets `obj[key]`.

    ```python
    class IndexableContainer:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, key):
        return self.data[key]
    ```
+ `__len__(self)`

    Returns the length of the container. Used by the `len()` function.

    ```python
    class IndexableContainer:
        def __len__(self):
            return len(self.data)
    ```
+ `__iter__(self)` and `__next__(self)`

    Makes an object iterable over its elements, allowing use in a for loop.

    ```python
    class CountDown:
        def __init__(self, start):
            self.current = start

        def __iter__(self):
            return self

        def __next__(self):
            if self.current > 0:
                num = self.current
                self.current -= 1
                return num
            raise StopIteration
    ```

+ `__eq__(self, other)`

    Defines behavior for the equality operator `==`.

    ```python 
    class Person:
        def __eq__(self, other):
            return self.name == other.name and self.age == other.age
    ```

+ `__contains__(self, item)`

    Used for membership testing with `in`.

    ```python
    class CustomContainer:
        def __init__(self, elements):
            self.elements = elements
        
        def __contains__(self, item):
            return item in self.elements

    container = CustomContainer([1, 2, 3, 4, 5])
    print(3 in container)  # True
    print(6 in container)  # False

    ```

## Exception Handling
Exceptions are also objects, and the parent class of common exceptions is `Exception`. So, any class that inherits from the `Exception` class can be recognized by the system as an exception type.

+ Creating an exception object does not affect program execution, only when the exception object is thrown does it affect program execution.
    + Common ways to throw exceptions: `raise XXXXError`
        + Creating a custom error:

        ```Python 
        class MyError(Exception):
            """ This is an example error """
            pass
        ```

+ Assert statement (usually used in unit tests):
    + `assert expression, [msg]` If the value of the expression is `False`, an assertion exception is thrown.
        + Example: `assert 0 == 1, "error msg"` This line of code will raise `AssertionError: error msg`

### Try Module

+ The try module is divided into four parts: `try`, `except`, `else`, and `finally`
    + `try`: Code that needs verification, when an error occurs here, it will not throw an error directly but will jump to the `except` section to run the code.
    + `except`: It is the error handling solution. One try module can have multiple except modules.
        + Its catch logic is: `isinstance(e, XXXError)`
        + From top to bottom, it captures, if anyone is successful, the error is consumed
        + If all processing modules do not succeed in catching the error, the error will be thrown into the system
    + `else`, `finally` are not necessary
        + `else`: When no error is generated in the code block of `try`, the code here is executed
        + `finally`: Regardless of whether an exception is thrown in the `try` block, the code here will be executed.
    + Example:
        ```Python 
        try:
            # Code here that may throw an exception
        except ExceptionType1:
            # Code here will be executed when the code in the try block throws a specific type of exception
        except ExceptionType2:
            # Code here will be executed when the code in the try block throws a specific type of exception
        else:
            # If the code in the try block does not throw an exception, the code here will be executed
        finally:
            # This code will be executed regardless of whether the code in the try block throws an exception
        ```

## Recursion
Recursion is a programming technique where a function calls itself to solve a smaller part of the problem. It's like breaking down a task into smaller tasks of the same type.
### How Recursion Works:
- A recursive function must have a **base case** that stops the recursion.
- Otherwise, the function keeps calling itself with a **reduced version** of the problem.

### Example of Recursion:
Calculating the factorial of a number, which is the product of all positive integers up to that number.

```python
def factorial(n):
    # Base case: factorial of 1 is 1
    if n == 1:
        return 1
    # Recursive case: n times the factorial of n-1
    else:
        return n * factorial(n-1)

# Example usage:
print(factorial(5))  # Output: 120
```

## Sorting Algorithms
### Merge Sort
[click here to see visualize](https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/visualize/)

Merge sort is a 'divide and conquer' algorithm that sorts a list by dividing it into smaller pieces, sorting those, and then merging them back together.

#### How Merge Sort Works:
- The list is split into halves until each sublist has one element.
- Pairs of sublists are merged in a sorted order.
- This merging is repeated until the whole list is merged and sorted.

#### Example of Merge Sort:
Here's how you can implement merge sort in Python.
```python
def mergesort(lst: list) -> list:
    """Return a sorted list with the same elements as <lst>.

    This is a *non-mutating* version of mergesort; it does not mutate the
    input list.
    """
    if len(lst) < 2:
        return lst[:]
    else:
        # Divide the list into two parts, and sort them recursively.
        mid = len(lst) // 2
        left_sorted = mergesort(lst[:mid])
        right_sorted = mergesort(lst[mid:])

        # Merge the two sorted halves.
        return _merge(left_sorted, right_sorted)

def _merge(lst1: list, lst2: list) -> list:
    """Return a sorted list with the elements in <lst1> and <lst2>.

    Precondition: <lst1> and <lst2> are sorted.
    """
    index1 = 0
    index2 = 0
    merged = []

    while index1 < len(lst1) and index2 < len(lst2):
        if lst1[index1] <= lst2[index2]:
            merged.append(lst1[index1])
            index1 += 1
        else:
            merged.append(lst2[index2])
            index2 += 1

    # Now either index1 == len(lst1) or index2 == len(lst2).
    assert index1 == len(lst1) or index2 == len(lst2)
    # The remaining elements of the other list
    # can all be added to the end of <merged>.
    # Note that at most ONE of lst1[index1:] and lst2[index2:]
    # is non-empty, but to keep the code simple, we include both.
    return merged + lst1[index1:] + lst2[index2:]
```
#### Benefits of Merge Sort:

- It has a consistent running time of O(n log n).
- It works well with large data sets.
- It is stable, which means that it preserves the input order of equal elements in the sorted output.

#### Drawbacks of Merge Sort:

- It requires additional space proportional to the size of the input.
- It may not be as fast as other algorithms, like quicksort, on smaller lists.

### Quick Sort
[click here to see visualize](https://www.runoob.com/w3cnote/quick-sort-2.html)

#### How Quick Sort Works:
- Select a 'pivot' element from the array.(in CSC148 we always use the first element in the list)
- Rearrange the array so that all elements with values less than the pivot come before it, while all elements with values greater than the pivot come after it. This operation is known as partitioning.
- Recursively apply the above steps to the sub-array of elements with smaller values and separately to the sub-array of elements with greater values.

#### Example of Quick Sort in Python:
```python
def quicksort(lst: list) -> list:
    """Return a sorted list with the same elements as <lst>.

    This is a *non-mutating* version of quicksort; it does not mutate the
    input list.
    """
    if len(lst) < 2:
        return lst[:]
    else:
        # Pick pivot to be first element.
        # Could make lots of other choices here (e.g., last, random)
        pivot = lst[0]

        # Partition rest of list into two halves
        smaller, bigger = _partition(lst[1:], pivot)

        # Recurse on each partition
        smaller_sorted = quicksort(smaller)
        bigger_sorted = quicksort(bigger)

        # Return! Notice the simple combining step
        return smaller_sorted + [pivot] + bigger_sorted


def _partition(lst: list, pivot: Any) -> tuple[list, list]:
    """Return a partition of <lst> with the chosen pivot.

    Return two lists, where the first contains the items in <lst>
    that are <= pivot, and the second is the items in <lst> that are > pivot.
    """
    smaller = []
    bigger = []

    for item in lst:
        if item <= pivot:
            smaller.append(item)
        else:
            bigger.append(item)

    return smaller, bigger
```
#### Benefits of Quick Sort:

- It's very efficient for large datasets.
On average, it has a time complexity of O(n log n).
- Quick sort is faster than merge sort and bubble sort in practice.

#### Drawbacks of Quick Sort:
- Worst-case time complexity is O(n^2), which occurs when the smallest or largest element is always picked as the pivot.

## Data Structures
### Linked Lists
A linked list is a one-dimensional list structure composed of a group of nodes.

#### Benefits of Linked Lists:
- Dynamic size: Easily grows and shrinks in size.
- Efficient insertions and deletions: Can quickly add or remove items without reorganizing the entire data structure.

#### Node
In Python, a node is a private class consisting of `item` and `next`.
```python 
from __future__ import annotations
from typing import Any, Optional

class _Node:
    item: Any
    next: Optional[_Node]
```

#### Basic Operations:
- **Insertion**: Add an item to the list.
- **Deletion**: Remove an item from the list.
- **Traversal**: Go through the list to find an item or to display the list.

    ```python
    class LinkedList:
        _first: Optional[_Node]
        
        def __init__(self):
            self._first = None
        
        def append(self, item: Any) -> None:
            if _first is None:
                self._first = None
                return
            curr = self._first
            while curr.next is not None:
                curr = curr.next
            curr.next = _Node(item)
        
        def __len__(self) -> int:
            counter = 0
            curr = self._first
            while curr is not None:
                counter += 1
                curr = curr.next
            return counter

        def __contains__(self, target: Any) -> bool:
            curr = self._first
            while curr is not None:
                if curr.item == target:
                    return True
            return False
        
        def __eq__(self, other: LinkedList) -> bool:
            curr1 = self._first
            curr2 = other._first
            while curr1 is not None and curr2 is not None:
                if curr1.item != curr2.item:
                    return False
                curr1 = curr1.next
                curr2 = curr2.next
            return curr1 == curr2

        def __getitem__(self, index: int) -> Any:
            curr = self._first
            i = 0
            while i < index:
                if curr None:
                    raise IndexError
                curr = curr.next
                i += 1
            return curr.item
        
        def __setitem__(self, index: int, new_item: Any) -> None:
            if self._first None:
                return IndexError
            curr = self._first
            i = 0
            while i < index:
                if curr None:
                    raise IndexError
                curr = curr.next
                i += 1
            curr.item = new_item
    ```

### Stacks and Queues
They are Abstract Data Types (ADTs)
#### Stack
A last-in, first-out (LIFO) data structure

+ Defined actions: `push(item)`, `pop()`, `is_empty()`
    + `push(item)`: Add an element to the top of the stack
    + `pop()`: Remove and return the element at the top of the stack
    + `is_empty()`: Check if the stack is empty
    ```python
    class Stack:
        def __init__(self) -> None:
            self._items = []

        def is_empty(self) -> bool:
            return len(self._items) == 0

        def push(self, item) -> None:
            self._items.append(item)

        def pop(self):
            if not self.is_empty():
                return self._items.pop()
            else:
                return None
    ```
+ We have learned how to implement a stack using a regular list and a linked list.
    + Regular list time complexity:
        + `push(item)`: Best O(1); Worst O(n); Average O(1)
        + `pop()`: Best O(1); Worst O(1); Average O(1)
        + `is_empty()`: Best O(1); Worst O(1); Average O(1)
    + Linked list time complexity:
        + `push(item)`: Best O(1); Worst O(n); Average O(1)
        + `pop()`: Best O(1); Worst O(1); Average O(1)
        + `is_empty()`: Best O(1); Worst O(1); Average O(1)

#### Queue
A first-in, first-out (FIFO) data structure

+ Defined actions: `enqueue(item)`, `dequeue()`, `is_empty()`
    + `enqueue(item)`: Add an element to the end of the queue
    + `dequeue()`: Remove and return the element at the front of the queue
    + `is_empty()`: Check if the queue is empty
    ```python
    class Queue:
        def __init__(self):
            self.items = []

        def is_empty(self):
            return self.items == []

        def enqueue(self, item):
            self.items.insert(0,item)

        def dequeue(self):
            return self.items.pop()
    ```

+ We have learned how to implement a queue using a regular list and a linked list.
    + Regular list time complexity:
        + `enqueue(item)`: Best O(1); Worst O(n); Average O(1)
        + `dequeue()`: Best O(1); Worst O(n); Average O(n)
        + `is_empty()`: Best O(1); Worst O(1); Average O(1)
    + Linked list time complexity:
        + `enqueue(item)`: Best O(1); Worst O(n); Average O(1)
        + `dequeue()`: Best O(1); Worst O(n); Average O(n) or O(1) (depending on the implementation of the linked list)
        + `is_empty()`: Best O(1); Worst O(1); Average O(1)

### Trees
A tree is a collection of nodes connected by edges, with one node designated as the root. Each node can have zero or more child nodes, but cannot have cycles (edges that loop back on themselves).

- **Binary Trees**: Each node has at most two children, commonly referred to as the left and right children.
- **Binary Search Trees (BST)**: A binary tree where each node has a value greater than all values in its left subtree and less than all values in its right subtree.
- **Traversal Methods**:
  - **In-order**: Traverse left subtree, visit node, traverse right subtree.
  - **Pre-order**: Visit node, traverse left subtree, traverse right subtree.
  - **Post-order**: Traverse left subtree, traverse right subtree, visit node.

## Conclusion



