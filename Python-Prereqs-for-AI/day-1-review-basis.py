# 1. Comprehensions(list,set)
# Task A:
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even_squares = [n * n for n in nums if n % 2 == 0]
# print(even_squares)

# Task B:
# words = ["apple", "cat", "banana", "dog", "elephant"]
# word_lengths = {word: len(word) for word in words if len(word) > 4}
# print(word_lengths)

# Task C:
# text = "Heloo, this is a sample text with some repeated words. This text is just for testing."
# vowels = {"a", "e", "i", "o", "u"}
# unique_vowels = {char.lower() for char in text if char.lower() in vowels}
# print(unique_vowels)

# 2. Slicing, unpacking, f-string
# Task A:
# a = [1,6,3,8,90,4,8,4,8,190]
# a[:3]       # first 3 elements
# a[-3:]      # last 3 elements
# a[::2]      # every 2nd element
# a[::-1]     # reversed list
# a[1:-1]     # everything except the first and last
# print(a)

# Task B:

# my_tuple = (10, 20, 30, 40, 50)
# first, *rest, last = my_tuple

# print(f"First: {first}")
# print(f"Rest: {rest}")
# print(f"Last: {last}")

# def get_user_info():
#     """Function that returns 3 values"""
#     name = "Alice"
#     age = 25
#     city = "New York"
#     return name, age, city

# name, age, city = get_user_info()

# print(f"\nUser Info:")
# print(f"Name: {name}")
# print(f"Age: {age}")
# print(f"City: {city}")

# Task C:
# value = 3.14159265

# print(f"{value=:>10.0f}")  # Output: value=         3

# nums = [10, 20, 30, 40, 50]
# first, *middle, last = nums
# print(f"\nfirst = {first} (type: {type(first).__name__})")
# print(f"middle = {middle} (type: {type(middle).__name__})")  # LIST, not tuple!
# print(f"last = {last} (type: {type(last).__name__})")

# # SLICING DEEP DIVE: [start:stop:step]
# # Indices: forward counting starts at 0, backward starts at -1
# # a[0]   = first element
# # a[-1]  = last element
# # a[-2]  = second to last
# # a[start:stop:step]
# #   - start: included (default: 0 or -len if step < 0)
# #   - stop: excluded (default: len or -1 if step < 0)
# #   - step: increment (default: 1, can be negative for reverse)

# test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(f"\nOriginal: {test_list}")
# print(f"[::2]      = {test_list[::2]}")      # Every 2nd: [0, 2, 4, 6, 8]
# print(f"[::-1]     = {test_list[::-1]}")     # Reversed: [9, 8, 7, ...]
# print(f"[1::2]     = {test_list[1::2]}")     # Start at 1, every 2nd: [1, 3, 5, 7, 9]
# print(f"[-3:]      = {test_list[-3:]}")      # Last 3: [7, 8, 9]
# print(f"[:-3]      = {test_list[:-3]}")      # Everything except last 3: [0, 1, 2, 3, 4, 5, 6]
# print(f"[1:-1]     = {test_list[1:-1]}")     # Exclude first & last: [1, 2, 3, 4, 5, 6, 7, 8]
# print(f"[2:7:2]    = {test_list[2:7:2]}")    # From index 2 to 7, step 2: [2, 4, 6]

# 3. Function with defaults, *args, **kwargs

# def build_profile(name, age=18, *args, **kwargs):
#     profile = {
#         "name": name,
#         "age": age,
#         "hobbies": list(args),
#     }
#     profile.update(kwargs)
#     return profile

# profile = build_profile("Jack", 25, "Soccer", "Basketball", "Video Games", city="Dushanbe")
# print(profile)