## Question: Merge two dictionaries and handle missing keys. Check if missing key exist if not then return "not found"

            dict1 = {'a': 1, 'b': 2}
            dict2 = {'b': 3, 'c': 4}
            
            # Use the Union Operator (Python 3.9+)
            merged = dict1 | dict2  # dict2 values overwrite dict1 for overlapping keys
            print(merged) # Output: {'a': 1, 'b': 3, 'c': 4}
            
            # Another way to merge
            dict1.update(dict2)
            
            # Safely getting a value that might not exist
            print(merged.get('d', "Not Found")) # Output: Not Found

## Question: Count the frequency of characters in a string.
          text = "excel_calendar"
          freq = {}
          
          for char in text:
              freq[char] = freq.get(char, 0) + 1
          print(freq)

          # Or use a Dictionary Comprehension for a list:
          # {x: text.count(x) for x in set(text)}

## Question: Invert a dictionary (Swap keys and values).
        old_dict = {'Apple': 'Red', 'Banana': 'Yellow', 'Grape': 'Green'}
        
        new_dict = {value: key for key, value in old_dict.items()}
        print(new_dict) # Output: {'Red': 'Apple', 'Yellow': 'Banana', 'Green': 'Grape'}

## Question: Sort a dictionary
  --using inbuilt function

      scores = {'Alice': 88, 'Bob': 95, 'Charlie': 78}
      
      # Sort ascending
      sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1]))
      print(sorted_scores) # Output: {'Charlie': 78, 'Alice': 88, 'Bob': 95}
  
  
  --- without using sort/ sorted
      data = {'Alice': 88, 'Bob': 95, 'Charlie': 78, 'David': 92}

      # Convert dictionary items to a list of tuples
      items = list(data.items()) # [('Alice', 88), ('Bob', 95), ...]
      
      # Manual Bubble Sort logic to sort by Value (index 1 of the tuple)
      n = len(items)
      for i in range(n):
          for j in range(0, n - i - 1):
              # Change > to < for descending order
              if items[j][1] > items[j + 1][1]:
                  # Swap the elements
                  items[j], items[j + 1] = items[j + 1], items[j]
      
      # 3. Rebuild the dictionary from the sorted list
      sorted_dict = {}
      for key, value in items:
          sorted_dict[key] = value
      
      print(sorted_dict)
      # Output: {'Charlie': 78, 'Alice': 88, 'David': 92, 'Bob': 95}


## Question: The "Two Sum" Problem (Find two indices that sum to a target).
    
    def two_sum(nums, target):
        seen = {} # Dictionary to store: {value: index}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
    
    # Example usage:
    print(two_sum([2, 7, 11, 15], 9)) # Output: [0, 1]

## Question: To sum values for keys present in either dictionary. It uses set() union logic to ensure no keys are missed.
      
      dict1 = {'a': 10, 'b': 20, 'c': 30}
      dict2 = {'b': 5, 'c': 15, 'd': 25}
      
      # Combine and sum values for all unique keys
      result = {k: dict1.get(k, 0) + dict2.get(k, 0) for k in set(dict1) | set(dict2)}
      
      print(result) 

## Question: Write a function to find the maximum depth of a nested dictionary.

    nested = {'a': 1, 'b': {'c': {'d': 4}}}
    
    -- Answer: Use recursion to explore the levels:
    def get_depth(d):
        if not isinstance(d, dict) or not d:
            return 0
        return 1 + max(get_depth(v) for v in d.values())
    
    print(get_depth(nested)) # Output: 3

## Question: What happens to a dictionary if you modify an object that is being used as a key?

    # Create a list and use it as a key... wait!
    my_list = [1, 2]
    my_dict = {my_list: "Values"} 
    Use code with caution.
    
    The Answer: This will raise a TypeError: unhashable type: 'list'. In Python, keys must be immutable (hashable)
    If you need to use a collection as a key, you must convert it to a tuple first: my_dict = {tuple(my_list): "Values"}

## Question: Given a list of words, group them into a dictionary where keys are the sorted letters and values are lists of words that are anagrams.
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # Target: {"aet": ["eat", "tea", "ate"], "ant": ["tan", "nat"], "abt": ["bat"]}
    The Answer:
    groups = {}
    for w in words:
        key = "".join(sorted(w))
        groups.setdefault(key, []).append(w)
    # .setdefault() is an optimized way to initialize a list for a new key
