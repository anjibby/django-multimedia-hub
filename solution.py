import os
import re

# ==========================================
# Task 1: Name Extraction
# ==========================================
# Write your actual name to name.txt
with open("name.txt", "w") as file:
    file.write("Ogunjobi Anjola")

# Read and extract names
with open("name.txt", "r") as file:
    full_name = file.read().strip()

name_parts = full_name.split()

first_name = name_parts[0]
middle_name = name_parts[1] if len(name_parts) > 2 else ""
last_name = name_parts[-1]

print("--- TASK 1 ---")
print(f"First Name: {first_name}")
print(f"Middle Name: {middle_name if middle_name else 'N/A'}")
print(f"Last Name: {last_name}\n")


# ==========================================
# Task 2: Print File Path using 'os'
# ==========================================
print("--- TASK 2 ---")
current_file_path = os.path.abspath(__file__)
print(f"Local File Path: {current_file_path}\n")


# ==========================================
# Task 3: Regex, Sorting, and Binary Search
# ==========================================
print("--- TASK 3 ---")

# 1. Regex Extraction from HTML
with open("baby2008.html", "r", encoding="utf-8") as f:
    html_content = f.read()

pattern = r"<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>"
matches = re.findall(pattern, html_content)

names_list = []
for match in matches:
    names_list.append(match[1])  # Boy name
    names_list.append(match[2])  # Girl name

# 2. Custom QuickSort Algorithm (No built-in sort)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x.lower() < pivot.lower()]
    middle = [x for x in arr if x.lower() == pivot.lower()]
    right = [x for x in arr if x.lower() > pivot.lower()]
    return quick_sort(left) + middle + quick_sort(right)

sorted_names = quick_sort(names_list)
print(f"Successfully extracted and sorted {len(sorted_names)} baby names.")

# 3. Custom Binary Search Algorithm
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    target_clean = target.lower()

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid].lower()

        if mid_val == target_clean:
            return mid
        elif mid_val < target_clean:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Search for a test name in the sorted list
search_target = "Jacob"
index = binary_search(sorted_names, search_target)

if index != -1:
    print(f"Found '{search_target}' at index {index} using Binary Search!")
else:
    print(f"'{search_target}' not found in the list.")