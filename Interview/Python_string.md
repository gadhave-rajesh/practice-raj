# Python String Interview Questions & Solutions (2026 Edition)

This guide provides dual solutions for common Python string interview questions: a **Pythonic method** (using modern built-in functions) and an **Algorithmic method** (solving manually via loops or recursion to demonstrate logic).

---

### 1. Palindrome Check
**Question:** Determine if a string reads the same forward and backward.

*   **Approach 1: Pythonic (Slicing)**
    ```python
    def is_palindrome(s):
        return s == s[::-1]
    ```
*   **Approach 2: Recursive (No Built-ins)**
    ```python
    def is_palindrome_recursive(s):
        if len(s) <= 1:
            return True
        if s[0] != s[-1]:
            return False
        return is_palindrome_recursive(s[1:-1])
    ```

---

### 2. String Reversal
**Question:** Reverse a string without using the standard slice `[::-1]`.

*   **Approach 1: Pythonic (Join/Reversed)**
    ```python
    def reverse_string(s):
        return "".join(reversed(s))
    ```
*   **Approach 2: Manual (Iterative)**
    ```python
    def reverse_string_manual(s):
        res = ""
        for i in range(len(s) - 1, -1, -1):
            res += s[i]
        return res
    ```

---

### 3. Anagram Check
**Question:** Check if two strings are anagrams (contain same letters with same frequencies).

*   **Approach 1: Pythonic (Sorting)**
    ```python
    def are_anagrams(s1, s2):
        return sorted(s1) == sorted(s2)
    ```
*   **Approach 2: Character Mapping (Manual Frequency)**
    ```python
    def are_anagrams_manual(s1, s2):
        if len(s1) != len(s2): return False
        counts = {}
        for char in s1:
            counts[char] = counts.get(char, 0) + 1
        for char in s2:
            if char not in counts or counts[char] == 0:
                return False
            counts[char] -= 1
        return True
    ```

---

### 4. Reverse Word Order
**Question:** Reverse the order of words in a sentence (e.g., "Hello World" -> "World Hello").

*   **Approach 1: Pythonic (Split & Join)**
    ```python
    def reverse_words(s):
        return " ".join(s.split()[::-1])
    ```
*   **Approach 2: Manual (Two-Pointer Style)**
    ```python
    def reverse_words_manual(s):
        words = []
        word = ""
        for char in s:
            if char == " ":
                if word: words.append(word)
                word = ""
            else:
                word += char
        if word: words.append(word)
        
        # Manually reversing list and joining
        res = ""
        for i in range(len(words)-1, -1, -1):
            res += words[i] + (" " if i != 0 else "")
        return res
    ```

---

### 5. Count Vowels
**Question:** Count the occurrences of vowels in a string.

*   **Approach 1: Pythonic (List Comprehension)**
    ```python
    def count_vowels(s):
        return sum(1 for char in s.lower() if char in 'aeiou')
    ```
*   **Approach 2: Recursive**
    ```python
    def count_vowels_recursive(s):
        if not s:
            return 0
        vowels = "aeiouAEIOU"
        count = 1 if s[0] in vowels else 0
        return count + count_vowels_recursive(s[1:])
    ```

---

### 6. First Non-Repeating Character
**Question:** Find the first character that appears only once.

*   **Approach 1: Pythonic (Using `count()`)**
    ```python
    def first_unique(s):
        for char in s:
            if s.count(char) == 1:
                return char
        return None
    ```
*   **Approach 2: Optimized O(n) (No `count()` in loop)**
    ```python
    def first_unique_optimized(s):
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        for char in s:
            if freq[char] == 1:
                return char
        return None
    ```

---

### **Learning Tips for 2026**
1.  **Complexity Matters:** Always mention that `s.count()` inside a loop makes an algorithm **O(n²)**. The dictionary approach is **O(n)**.
2.  **Immutability:** Remember that strings in Python are immutable; "modifying" a string always creates a new one in memory.
3.  **Practice:** Use the [Official Python String Documentation](https://docs.python.org) to stay updated on new methods.
4.  **Practice:** GeeksforGeeks String Exercises: A comprehensive collection of 50+ practice problems. - https://www.geeksforgeeks.org/python/python-string-exercise/
