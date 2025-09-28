# Functions, Data Structures and Modules

This project delves into the fundamentals of functions, data structures, and modules in Python. The aim is to explore how to define and utilize functions, effectively manage data using various built-in structures, and leverage modules and libraries to extend Python’s capabilities.

## 0. Arithmetic Operations Function
**task**:
Create a Python script named arithmetic_operations.py. In this script, define a function that performs basic arithmetic operations. This function, perform_operation, will be imported and used in a separate main.py script, which we provide.

## 1. Shopping List Manager
Objective: Utilize Python lists to create a simple shopping list manager that allows users to add items, view the current list, and remove items.

**Learnings**
- try...except Structure and Learnings
The try...except block in Python is the standard way to handle potential errors (exceptions) in a program gracefully, preventing a crash.

1. The Basic Structure
The block works on the principle of "Easier to Ask for Forgiveness than Permission" (EAFP). You attempt a risky operation in the try block. If it fails, control immediately jumps to the except block.
```
try:
    # 1. ATTEMPT: Code to be executed (the "risky" operation).
    #    If this code succeeds, the 'except' block is skipped.
    risky_operation()
    
except ExceptionType:
    # 2. HANDLE: Code to execute ONLY IF a specific error 
    #    (like 'ExceptionType') occurs in the 'try' block.
    handle_error_gracefully()
```
2. II. Key Learnings from the Shopping List App
We used try...except for the "Remove Item" functionality to handle the scenario where the user tries to delete an item that isn't in the list.

**Concept**
1. Python Implementation: except ValueError:
* => The list.remove() method raises a specific error called ValueError when the item is not found. We must catch this specific error rather than a general one to keep our error handling precise.

2. EAFP Principle: Attempting shopping_list.remove(item) directly inside try:
* => The best practice is to just try the operation. We don't check if item in list: first (the "permission" approach). We assume success and only handle the failure (forgiveness).

3. Robustness: The entire structure prevents the program from crashing.	
* => By anticipating an error, we replace a harsh crash (a fatal unhandled exception) with a polite, user-friendly error message. This makes the application robust.


## Setup
1. First create the environment
    => python3 -m venv .venv
2. Activate it
    => source .venv/bin/activate
3. Install the requests library
    => pip install requests
4. in the app.py import the requests lib
    => import requests