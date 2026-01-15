# Recursion problems

### 1. Factorial of a Number
Calculate the product of all integers from 1 up to \(n\).
Base Case: If \(n=0\) or \(1\), return \(1\).
Recursive Case: \(n\times \text{factorial}(n-1)\). python
 def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

-- Answer for factorial(5): 120

### 2. Fibonacci Sequence

Find the \(n^{th}\) number in the sequence where each number is the sum of the two preceding ones. Base Case: If \(n\le 1\), return \(n\).Recursive Case: \(\text{fibonacci}(n-1)+\text{fibonacci}(n-2)\).
   def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) +    fibonacci(n - 2)

-- Answer for fibonacci(7): 13

#### 3. Sum of Elements in a List

Find the total sum of all numbers in a given list. Base Case: If the list is empty, return \(0\).Recursive Case: First element + \(\text{sum}(\text{remaining\ elements})\).

-- Answer for sum_list([1, 2, 3, 4, 5]): 15

### 4. Binary String
Conversion Convert a decimal number into its binary string representation. Base Case: If \(n=0\), stop or return an empty result.Recursive Case: Divide \(n\) by \(2\) and append the remainder.

def convert_to_binary(n):
    if n == 0:
        return ""
    return convert_to_binary(n // 2) + str(n % 2)

 -- Answer for convert_to_binary(6): "110"


### 5. Greatest Common Divisor (GCD) Find the GCD of two numbers using the Euclidean algorithm. Base Case: If the second number is \(0\), the first number is the GCD.Recursive Case: \(\text{gcd}(b,a\mod b)\).

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

-- Answer for gcd(48, 18): 6

 ## Key Considerations Recursion Depth: 

Python has a default recursion limit (usually 1000). Exceeding it results in a 

RecursionError.Efficiency: Recursive functions can be slower and use more memory than iterative while or for loops due to the overhead of the call stack.

Tail Recursion: A specific type of recursion where the recursive call is the very last action of the function, allowing for potential optimization. 
