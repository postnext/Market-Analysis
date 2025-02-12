import random
import string
import math

def generate_random_string(length=10):
    """Generate a random string of given length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def fibonacci(n):
    """Generate a Fibonacci sequence up to n."""
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_random_numbers(count=10, lower=1, upper=100):
    """Generate a list of random numbers."""
    return [random.randint(lower, upper) for _ in range(count)]

def reverse_string(s):
    """Reverse a given string."""
    return s[::-1]

def factorial(n):
    """Calculate factorial of a number."""
    if n == 0:
        return 1
    return n * factorial(n - 1)

def count_vowels(s):
    """Count the number of vowels in a string."""
    return sum(1 for char in s.lower() if char in "aeiou")

def sort_numbers(numbers):
    """Sort a list of numbers in ascending order."""
    return sorted(numbers)

def find_max(numbers):
    """Find the maximum number in a list."""
    return max(numbers) if numbers else None

def find_min(numbers):
    """Find the minimum number in a list."""
    return min(numbers) if numbers else None

def calculate_mean(numbers):
    """Calculate the mean of a list of numbers."""
    return sum(numbers) / len(numbers) if numbers else None

def calculate_median(numbers):
    """Calculate the median of a list of numbers."""
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 1:
        return sorted_numbers[n // 2]
    else:
        mid1, mid2 = sorted_numbers[n // 2 - 1], sorted_numbers[n // 2]
        return (mid1 + mid2) / 2

def calculate_standard_deviation(numbers):
    """Calculate the standard deviation of a list of numbers."""
    mean = calculate_mean(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return math.sqrt(variance)

def is_palindrome(s):
    """Check if a string is a palindrome."""
    return s == s[::-1]

def main():
    sample_numbers = generate_random_numbers()
    print("Random String:", generate_random_string(12))
    print("Fibonacci Sequence:", fibonacci(10))
    print("Prime Check (17):", is_prime(17))
    print("Random Numbers:", sample_numbers)
    print("Reversed String:", reverse_string("Hello World"))
    print("Factorial (5):", factorial(5))
    print("Sorted Numbers:", sort_numbers(sample_numbers))
    print("Max Number:", find_max(sample_numbers))
    print("Min Number:", find_min(sample_numbers))
    print("Mean:", calculate_mean(sample_numbers))
    print("Median:", calculate_median(sample_numbers))
    print("Standard Deviation:", calculate_standard_deviation(sample_numbers))
    print("Vowel Count in 'Cryptography':", count_vowels("Cryptography"))
    print("Is 'racecar' a palindrome?", is_palindrome("racecar"))

if __name__ == "__main__":
    main()
