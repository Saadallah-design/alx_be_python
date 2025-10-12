# Objective: Solidify your understanding of class methods and static methods in Python 
# by implementing examples of each in a class, 
# demonstrating their usage and differences.

class Calculator:

    # a class attribute is shared across all instances of the class
    calculation_type = "Arithmetic Operations" 


    # for the static method we don't use self or cls as the first parameter
    # a static method does not have access to the instance (self) or class (cls)
    @staticmethod
    def add(x, y):
        return x + y

    # for the class method we use cls as the first parameter by convention
    @classmethod
    def multiply(cls, x, y):
        # Access the class attribute using the 'cls' parameter
        method_type = cls.calculation_type 
        result = x * y
        # We can use the class attribute in the output
        print(f"[{method_type}] Calculating: {x} * {y}")
        return result
    
    