# Recursion Problems

### 1. Factorial of a Number
Calculate the product of all integers from 1 up to $n$.

**Base Case:** If $n=0$ or $n=1$, return $1$.  
**Recursive Case:** $n \times \text{factorial}(n-1)$

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
```

### 2. Fibonacci Sequence

Find the N th number in the sequence where each number is the sum of the two preceding ones.

**Base Case:** If $(n<=1)$, return (n).
**Recursive Case:** $(fibonacci(n-1)+fibonacci(n-2))$ 

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```
-- Answer for fibonacci(7): 13

#### 3. Sum of Elements in a List

Find the total sum of all numbers in a given list. 

**Base Case:**  If the list is empty, return 0.
**Recursive Case:** First element + (sum(remaining elements)).

```python
def sum_list(numbers):
    if not numbers:
        return 0
    return numbers[0] + sum_list(numbers[1:])
```

-- Answer for sum_list([1, 2, 3, 4, 5]): 15

### 4. Binary String
Conversion Convert a decimal number into its binary string representation. 

**Base Case:** If (n=0), stop or return an empty result.
**Recursive Case:** Divide n by 2 and append the remainder.

```python
def convert_to_binary(n):
    if n == 0:
        return ""
    return convert_to_binary(n // 2) + str(n % 2)
```
 -- Answer for convert_to_binary(6): "110"


### 5. Greatest Common Divisor 
(GCD) Find the GCD of two numbers using the Euclidean algorithm. 

**Base Case:** If the second number is \(0\), the first number is the GCD.
**Recursive Case:** (gcd(b,a\mod b)\).

```python
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
```

-- Answer for gcd(48, 18): 6

### 5. Recursion printer for string

**Base Case:** If the string is empty, the function returns and stops.
**Recursive Case:** Print the character at the current index (usually index 0) and then call the function again with a sliced version of the string starting from the next index. 

```python
def print_letters(s):
    # Base Case: stop if string is empty
    if not s:
        return
    
    # Print the first letter
    print(s[0])
    
    # Recursive Case: call with the rest of the string
    print_letters(s[1:])

        Example Usage:
        print_letters("Python")
        Output:
        P
        y
        t
        h
        o
        n
```

 ## Key Considerations Recursion Depth: 

-- Python has a default recursion limit (usually 1000). Exceeding it results in a RecursionError.Efficiency: Recursive functions can be slower and use more memory than iterative while or for loops due to the overhead of the call stack.

-- Tail Recursion: A specific type of recursion where the recursive call is the very last action of the function, allowing for potential optimization. 
