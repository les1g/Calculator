"""Core calculation functions for the calculator application."""


def add(a, b):
    """
    Add two numbers.
    
    Args:
        a (int/float): First number
        b (int/float): Second number
        
    Returns:
        int/float: Sum of a and b
    """
    return a + b


def subtract(a, b):
    """
    Subtract two numbers.
    
    Args:
        a (int/float): First number
        b (int/float): Second number
        
    Returns:
        int/float: Difference (a - b)
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers.
    
    Args:
        a (int/float): First number
        b (int/float): Second number
        
    Returns:
        int/float: Product of a and b
    """
    return a * b


def divide(a, b):
    """
    Divide two numbers.
    
    Args:
        a (int/float): Dividend
        b (int/float): Divisor
        
    Returns:
        float: Quotient (a / b)
        
    Raises:
        ValueError: If divisor (b) is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def test_calculator():
    """Run basic tests for all calculator functions."""
    assert add(2, 3) == 5, "Addition test failed"
    assert subtract(5, 3) == 2, "Subtraction test failed"
    assert multiply(2, 3) == 6, "Multiplication test failed"
    assert divide(6, 3) == 2, "Division test failed"
    
    try:
        divide(1, 0)
        assert False, "Division by zero should raise ValueError"
    except ValueError as e:
        assert str(e) == "Cannot divide by zero.", "Error message mismatch"


if __name__ == "__main__":
    test_calculator()
    print("All tests passed!")