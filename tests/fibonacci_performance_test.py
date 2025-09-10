# System Modules
import sys
import os
import time

# Installed Modules
import pytest

# Project Modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculations import get_nth_fibonacci   # noqa: E402


def test_fibonacci_large_numbers():
    """Test Fibonacci calculation for moderately large numbers."""
    # Test some larger Fibonacci numbers to ensure correctness
    test_cases = [
        (20, 6765),
        (30, 832040),
        (35, 9227465),
    ]
    
    for n, expected in test_cases:
        result = get_nth_fibonacci(n)
        assert result == expected, f"Fibonacci({n}) should be {expected}, got {result}"


def test_fibonacci_performance_baseline():
    """Benchmark current implementation for performance analysis."""
    # Test performance for n=100 to see if optimization is needed
    n = 100
    start_time = time.time()
    result = get_nth_fibonacci(n)
    end_time = time.time()
    
    # The 100th Fibonacci number is 354224848179261915075
    assert result == 354224848179261915075
    
    # This test mainly serves to establish baseline performance
    # The actual time will vary by system, but should be reasonable
    duration = end_time - start_time
    assert duration < 1.0, f"Fibonacci(100) took {duration:.4f}s, which may indicate need for optimization"


def test_fibonacci_very_large_number():
    """Test that the optimized implementation can handle very large Fibonacci numbers efficiently."""
    # Test a very large Fibonacci number that would be slow with naive approaches
    n = 1000
    start_time = time.time()
    result = get_nth_fibonacci(n)
    end_time = time.time()
    
    # Verify the result is correct (first few digits of F(1000))
    # F(1000) starts with 43466...
    result_str = str(result)
    assert result_str.startswith("43466"), f"F(1000) should start with 43466, got {result_str[:5]}"
    
    # Should complete very quickly with matrix exponentiation
    duration = end_time - start_time
    assert duration < 0.1, f"Fibonacci(1000) took {duration:.4f}s, optimization may not be working"


def test_fibonacci_edge_cases_optimized():
    """Test edge cases to ensure the optimized version handles them correctly."""
    # Test boundary between iterative and matrix approaches
    test_cases = [
        (99, 218922995834555169026),  # Last one using iterative
        (100, 354224848179261915075),  # First one using matrix
        (101, 573147844013817084101),  # Ensure matrix method works for 101
    ]
    
    for n, expected in test_cases:
        result = get_nth_fibonacci(n)
        assert result == expected, f"Fibonacci({n}) should be {expected}, got {result}"


@pytest.mark.parametrize("n,expected", [
    (40, 102334155),
    (50, 12586269025),
    (60, 1548008755920),
])
def test_fibonacci_medium_large_numbers(n, expected):
    """Test Fibonacci for medium-large numbers to validate optimization."""
    result = get_nth_fibonacci(n)
    assert result == expected