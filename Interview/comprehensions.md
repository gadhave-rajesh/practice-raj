# Python List & Dict Comprehension: Interview Trick Questions (2026)

---

### 1. The "Flattening" Challenge
**Question:** How do you flatten a nested list (2D to 1D) using list comprehension?
*   **The Trick:** The order of the `for` clauses must match the order of nested loops in regular syntax.

```python
nested_list = [[1, 2], [3, 4], [5, 6]]

# Solution
flattened = [item for sublist in nested_list for item in sublist]

# Explanation: Equivalent to:
# for sublist in nested_list:
#     for item in sublist:
#         flattened.append(item)
```

### 2. List Comprehension with Conditional Logic (if-else)
**Question:** Create a list where even numbers are kept as is, and odd numbers are squared.
*   **The Trick:** When using else, the conditional must be at the start of the comprehension, not the end.

```Python
nums = [1, 2, 3, 4, 5]
# Solution
result = [x if x % 2 == 0 else x**2 for x in nums]

# Common Mistake: [x for x in nums if x % 2 == 0 else x**2] -> SyntaxError
```

### 3. Dict Comprehension from Two Lists
**Question:** Given keys = ['a', 'b'] and values = [1, 2], create a dictionary.
*   **The Trick:** Efficiently pairing elements using zip().

```Python
keys = ['name', 'age', 'role']
values = ['Alice', 25, 'Dev']

# Pythonic Solution
my_dict = {k: v for k, v in zip(keys, values)}

# Alternative (No built-in zip)
my_dict_manual = {keys[i]: values[i] for i in range(len(keys))}
```

### 4. Nested Dictionary Comprehension
**Question:** Create a dictionary where keys are numbers 1-3, and values are dictionaries containing that number's square.
*   **Target:** {1: {'sq': 1}, 2: {'sq': 4}, 3: {'sq': 9}}

```Python
# Solution
nested_dict = {x: {'sq': x**2} for x in range(1, 4)}
```

### 5. Filtering and Transforming Simultaneously
**Question:** From a list of strings, create a dictionary where the key is the string and the value is its length, but only for strings longer than 3 characters.


```Python
words = ["hi", "python", "code", "ai"]

# Solution
word_map = {w: len(w) for w in words if len(w) > 3}
```



### 6. The "Scope Leak" Trick (Legacy Python vs. Modern)
**Question:** What happens to the variable x after res = [x for x in range(5)] is executed?
*   **The Trick:** In Python 3+, list comprehensions have their own scope. x will not exist in the local namespace.

```Python
[x for x in range(10)]
try:
    print(x) 
except NameError:
    print("x is not defined!") # Correct in 2026 (Python 3+)

```


## 7. Matrix Creation (The Reference Trap)
**Question:** Create a 3x3 matrix of zeros using comprehension.
*   **The Trick:** Why is [[0]*3 for _ in range(3)] better than [[0]*3]*3?
[[0]*3]*3 creates 3 references to the same list object. Changing one row changes all.

```Python
# The Correct Way
matrix = [[0 for _ in range(3)] for _ in range(3)]

# Verification
matrix[0][0] = 1
# matrix remains [[1, 0, 0], [0, 0, 0], [0, 0, 0]]

```

### 9. Conditional Filtering (Multiple Conditions)
**Question:** Generate a list of numbers between 1 and 50 that are divisible by both 2 and 5.

```python
# Approach 1: Pythonic
res = [x for x in range(1, 51) if x % 2 == 0 if x % 5 == 0]

# Approach 2: Recursive (No comprehension)
def get_divisible(n):
    if n == 0: return []
    rest = get_divisible(n - 1)
    if n % 10 == 0: rest.append(n)
    return rest

```

### Summary of Best Practices (2026)
**Readability:** If a comprehension exceeds two lines or becomes complex, use a standard for loop.
**Memory:** For massive datasets, use Generator Expressions (x for x in range(1000000)) instead of List Comprehensions [...] to save RAM.
**Side Effects:** Never call functions that modify state inside a comprehension (e.g., [print(x) for x in list]).
