# System Modules
import math

# Installed Modules
# - None


def area_of_circle(radius):
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2


def get_nth_fibonacci(n):
    """Calculate the nth Fibonacci number using an optimized approach.
    
    Uses iterative method for small numbers (n < 100) and matrix exponentiation
    for larger numbers to achieve better performance for large inputs.
    """
    if n < 0:
        raise ValueError("n cannot be negative")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 100:
        # Use iterative approach for small numbers (most efficient for small n)
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    else:
        # Use matrix exponentiation for large numbers (O(log n) complexity)
        return _fibonacci_matrix_power(n)


def _fibonacci_matrix_power(n):
    """Calculate nth Fibonacci number using matrix exponentiation.
    
    This method has O(log n) time complexity, making it efficient for large n.
    Uses the property that:
    [F(n+1)]   [1 1]^n   [1]
    [F(n)  ] = [1 0]   * [0]
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Base matrix [[1, 1], [1, 0]]
    result_matrix = _matrix_power([[1, 1], [1, 0]], n - 1)
    
    # F(n) = result_matrix[0][0] * 1 + result_matrix[0][1] * 0 = result_matrix[0][0]
    return result_matrix[0][0]


def _matrix_power(matrix, power):
    """Calculate matrix raised to a power using fast exponentiation."""
    if power == 1:
        return matrix
    
    # Initialize result as identity matrix
    result = [[1, 0], [0, 1]]
    base = [row[:] for row in matrix]  # Copy the matrix
    
    while power > 0:
        if power % 2 == 1:
            result = _matrix_multiply(result, base)
        base = _matrix_multiply(base, base)
        power //= 2
    
    return result


def _matrix_multiply(a, b):
    """Multiply two 2x2 matrices."""
    return [
        [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
        [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]
    ]
