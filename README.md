# SWE_Practical_Works

lab 1 question
Unique Word Count:

The count_unique_words function removes punctuation, converts text to lowercase, and counts the number of unique words in the text.
Longest Word:

The Longest_words function finds the longest word in the text after removing punctuation and converting to lowercase.
Word Occurrence Counter:

The count_word_occurrences function counts how many times a specific target word appears in the text, ignoring case and punctuation.
Percentage of Words Longer than Average:

The percentage_longer_than_average function calculates the percentage of words in the text that are longer than the average word length.

lab 2

Different Fibonacci Calculation Methods:

fibonacci_recursive: Classical recursive implementation
fibonacci_iterative: Iterative implementation returning a list of Fibonacci numbers
fibonacci_generator: Generator implementation for memory efficiency
fibonacci_memoized: Optimized recursive implementation using memoization
Performance Measurement:

measure_time: Utility function to measure execution time of different Fibonacci implementations
Compares performance between recursive, iterative, and memoized approaches
Utility Functions:

fibonacci_up_to_n: Generates Fibonacci numbers up to n
index_of_first_exceeding_fibonacci: Finds the index of first Fibonacci number exceeding a given value
is_fibonacci_number: Checks if a number is part of the Fibonacci sequence
fibonacci_ratios: Calculates ratios between consecutive Fibonacci numbers
Main Program Features:

Displays Fibonacci sequence up to n terms
Finds index of first Fibonacci number exceeding a given value
Tests if user input is a Fibonacci number
Shows ratios between consecutive Fibonacci numbers
Compares execution times of different implementations

lab 3

Search Algorithms:

Linear Search: Searches through the entire list sequentially.
Binary Search: Uses a divide-and-conquer approach on a sorted list.
Jump Search: A block-jumping method that works on sorted arrays.
Performance Measurement:

A timing mechanism to measure the execution time of each search algorithm.
A comparison counter for the binary search to track the number of comparisons made.
Utility Functions:

count_comparisons: A decorator to count comparisons in binary search.
compare_search_algorithms: Compares the performance of all three search algorithms.
Main Program Features:

Generates a random list of integers for testing.
Demonstrates the use of each search algorithm individually.
Performs a comprehensive comparison of all three algorithms on a larger dataset.
Specific Implementations:

Linear Search: Returns all indices where the target is found.
Binary Search: Implemented iteratively, returns the index or insertion point.
Jump Search: Implements the jump search algorithm for sorted arrays.
Additional Features:

Handles cases where the target might appear multiple times (in linear search).
Uses Python's random module for generating test data.
Incorporates the math module for calculations in jump search.

lab4

Data Structures:

Stack: Implemented with push, pop, peek, is_empty, and size methods.
Queue: Implemented with enqueue, dequeue, front, is_empty, and size methods.
Algorithm Implementations:

Postfix Expression Evaluation: Uses a stack to evaluate postfix mathematical expressions.
Queue using Two Stacks: Implements a queue data structure using two stacks.
Task Scheduler: Uses a queue to implement a basic task scheduling system.
Infix to Postfix Conversion: Converts infix mathematical expressions to postfix notation using a stack.
Utility Functions:

evaluate_postfix: Evaluates a postfix expression and returns the result.
queue_using_two_stacks: Returns enqueue and dequeue functions for a queue implemented with two stacks.
task_scheduler: Simulates processing of tasks in a queue.
infix_to_postfix: Converts an infix expression to postfix notation.
Main Program Features:

Demonstrates the use of each implemented algorithm with example inputs.
Prints results of postfix evaluation, queue operations, task scheduling, and infix-to-postfix conversion.

lab 5 

Basic Linked List Structure:

Node class: Represents individual nodes in the linked list.
LinkedList class: Implements the linked list structure.
Basic Operations:

append: Adds a new node to the end of the list.
display: Prints the elements of the list.
insert: Inserts a new node at a specified position.
delete: Removes a node with a specific value.
search: Finds the position of a node with a given value.
Advanced Operations and Algorithms:

reverse: Reverses the order of nodes in the list.
find_middle: Finds the middle element of the list using the two-pointer technique.
has_cycle: Detects if the linked list has a cycle using Floyd's Cycle-Finding Algorithm.
remove_duplicates: Removes duplicate nodes from the list.
merge_sorted: Static method to merge two sorted linked lists.
Demonstration:

Creates multiple linked lists to showcase different operations.
Demonstrates finding the middle element, cycle detection, duplicate removal, and merging sorted lists.

lab 6

Core Classes:

Node: Represents tree nodes with value and left/right child references.
BinarySearchTree: Implements the BST structure and operations.
Basic BST Operations:

insert: Adds new nodes maintaining BST properties.
search: Finds nodes with specific values.
delete: Removes nodes while maintaining BST structure.
Tree Traversal Methods:

inorder_traversal: Left-Root-Right traversal.
preorder_traversal: Root-Left-Right traversal.
postorder_traversal: Left-Right-Root traversal.
level_order_traversal: Breadth-first traversal using a queue.
Tree Analysis and Utility Functions:

find_max: Finds the maximum value in the tree.
count_nodes: Counts total nodes in the tree.
find_height: Calculates the height of the tree.
is_valid_bst: Validates if the tree follows BST properties.
Helper Methods:

Various recursive helper functions for main operations.
_min_value: Finds minimum value in a subtree.
_is_valid_bst_recursive: Recursively validates BST properties.

lab 7 

Sorting Algorithms:

Quick Sort (In-Place):

Uses partition-based approach
Implements recursive sorting strategy
Efficient for large datasets
Bubble Sort (Optimized):

Includes early termination optimization
Tracks swapping operations
Best for nearly sorted arrays
Hybrid Merge Sort:

Combines Merge Sort and Insertion Sort
Uses Insertion Sort for small subarrays (≤10 elements)
Maintains merge sort's efficiency for larger datasets
Insertion Sort:

Used as a component in hybrid sorting
Efficient for small arrays
Implemented as a helper function
Helper Functions:

partition: Supports Quick Sort implementation
merge: Combines sorted subarrays in Merge Sort
Visualization Component:

Uses matplotlib for visual representation
Implements animated bubble sort visualization
Features:
Real-time bar chart updates
Interactive display
Visual representation of sorting process
Implementation Details:

All algorithms maintain in-place sorting where applicable
Includes optimization techniques
Provides visual feedback for educational purposes

lab 8

Graph Structure:

Uses a defaultdict to represent the graph as an adjacency list.
Supports both weighted and unweighted graphs.
Basic Graph Operations:

add_vertex: Adds a new vertex to the graph.
add_edge: Adds an edge between two vertices, with optional weight.
print_graph: Displays the graph structure.
Graph Traversal Algorithms:

Depth-First Search (DFS): Implemented recursively.
Breadth-First Search (BFS): Implemented using a queue.
Path Finding Algorithms:

find_all_paths: Finds all possible paths between two vertices.
find_shortest_path_bfs: Finds the shortest path using BFS.
dijkstra: Implements Dijkstra's algorithm for finding shortest paths in weighted graphs.
Graph Analysis Algorithms:

detect_cycle: Detects if the graph contains a cycle.
is_bipartite: Checks if the graph is bipartite.
Advanced Features:

Supports weighted edges.
Implements priority queue (using heapq) for Dijkstra's algorithm.