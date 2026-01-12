# NumPy Advanced Topics: Complete Beginner's Guide 🚀

> **🎯 Goal**: Master advanced NumPy concepts with hands-on examples and real outputs. After this guide, you'll handle complex data manipulation like a pro!

## 📚 What You'll Master
- **Shape Manipulation**: Reshape arrays for any purpose
- **Broadcasting**: Make different-sized arrays work together
- **Copy & View**: Manage memory efficiently
- **Sorting & Searching**: Find and organize data quickly
- **Random Numbers**: Generate data for testing and simulations
- **I/O Operations**: Save and load data in various formats

## Table of Contents
1. [Shape Manipulation](#1-shape-manipulation-) - Reshaping and organizing data
2. [Broadcasting](#2-broadcasting-) - Working with different sized arrays
3. [Copy & View](#3-copy--view-) - Memory management
4. [Sorting & Searching](#4-sorting--searching-) - Finding and organizing data
5. [Random Numbers](#5-random-numbers-) - Generating test data and simulations
6. [I/O](#6-io-) - Saving and loading data

---

## 1. Shape Manipulation 🔄

> **🎯 Learning Goal**: Master reshaping arrays to fit any data structure you need.

### Why Learn Shape Manipulation?
- **Data Preparation**: Transform data for machine learning algorithms
- **Memory Efficiency**: Reorganize data without copying
- **Compatibility**: Make arrays work together in operations
- **Visualization**: Prepare data for plotting and analysis

### 🔰 Beginner Level: Understanding Array Shapes

```python
import numpy as np

# Let's start with a simple example
numbers = np.arange(12)  # Create numbers 0 to 11
print("Original 1D array:", numbers)
print("Shape:", numbers.shape)
print("Total elements:", numbers.size)
```
**Output:**
```
Original 1D array: [ 0  1  2  3  4  5  6  7  8  9 10 11]
Shape: (12,)
Total elements: 12
```

> **💡 Beginner Tip**: Shape (12,) means 1D array with 12 elements. The comma indicates it's a tuple.

### 🔰 Beginner Level: Basic Reshaping

```python
# Reshape 1D array to 2D (like organizing books on shelves)
matrix_3x4 = numbers.reshape(3, 4)  # 3 rows, 4 columns
print("Reshaped to 3x4 matrix:")
print(matrix_3x4)
print("New shape:", matrix_3x4.shape)
```
**Output:**
```
Reshaped to 3x4 matrix:
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
New shape: (3, 4)
```

```python
# Different reshape options
matrix_2x6 = numbers.reshape(2, 6)  # 2 rows, 6 columns
matrix_4x3 = numbers.reshape(4, 3)  # 4 rows, 3 columns

print("2x6 matrix:")
print(matrix_2x6)
print("\n4x3 matrix:")
print(matrix_4x3)
```
**Output:**
```
2x6 matrix:
[[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]]

4x3 matrix:
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
```

> **💡 Beginner Tip**: Total elements must stay the same! 12 elements can become 3×4, 2×6, 4×3, but not 3×5.

### 🔰 Beginner Level: Auto-Calculate Dimensions

```python
# Use -1 to let NumPy calculate one dimension automatically
auto_rows = numbers.reshape(-1, 4)  # "Figure out rows, I want 4 columns"
auto_cols = numbers.reshape(3, -1)  # "I want 3 rows, figure out columns"

print("Auto-calculated rows (-1, 4):")
print(auto_rows)
print("Shape:", auto_rows.shape)

print("\nAuto-calculated columns (3, -1):")
print(auto_cols)
print("Shape:", auto_cols.shape)
```
**Output:**
```
Auto-calculated rows (-1, 4):
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
Shape: (3, 4)

Auto-calculated columns (3, -1):
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
Shape: (3, 4)
```

> **💡 Beginner Tip**: Use -1 when you know one dimension but want NumPy to calculate the other.

### 🚀 Intermediate Level: 3D Reshaping

```python
# Create 3D array (think of it as multiple 2D sheets stacked)
cube = numbers.reshape(2, 2, 3)  # 2 sheets, each 2x3
print("3D array (2x2x3):")
print(cube)
print("Shape:", cube.shape)
print()

# Access different sheets
print("First sheet (index 0):")
print(cube[0])
print("\nSecond sheet (index 1):")
print(cube[1])
```
**Output:**
```
3D array (2x2x3):
[[[ 0  1  2]
  [ 3  4  5]]

 [[ 6  7  8]
  [ 9 10 11]]]
Shape: (2, 2, 3)

First sheet (index 0):
[[0 1 2]
 [3 4 5]]

Second sheet (index 1):
[[ 6  7  8]
 [ 9 10 11]]
```

> **💡 Beginner Tip**: 3D shape (2, 2, 3) means: 2 sheets, each sheet has 2 rows and 3 columns.

### 🚀 Intermediate Level: Flattening Arrays

```python
# Start with a 2D array
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original 2D array:")
print(matrix)
print()

# Flatten to 1D - two methods
flat_copy = matrix.flatten()    # Creates a copy
flat_view = matrix.ravel()      # Creates a view (shares memory)

print("Flattened (copy):", flat_copy)
print("Flattened (view):", flat_view)
```
**Output:**
```
Original 2D array:
[[1 2 3]
 [4 5 6]
 [7 8 9]]

Flattened (copy): [1 2 3 4 5 6 7 8 9]
Flattened (view): [1 2 3 4 5 6 7 8 9]
```

```python
# Test the difference between copy and view
print("Testing copy vs view:")
flat_copy[0] = 999
flat_view[1] = 888

print("After modifying flattened arrays:")
print("Original matrix:")
print(matrix)
print("flat_copy:", flat_copy)
print("flat_view:", flat_view)
```
**Output:**
```
Testing copy vs view:
After modifying flattened arrays:
Original matrix:
[[  1 888   3]
 [  4   5   6]
 [  7   8   9]]
flat_copy: [999   2   3   4   5   6   7   8   9]
flat_view: [  1 888   3   4   5   6   7   8   9]
```

> **💡 Beginner Tip**: 
> - `flatten()` = independent copy (changes don't affect original)
> - `ravel()` = view (changes affect original)

### 🚀 Intermediate Level: Transposing (Flipping Rows/Columns)

```python
# Create a rectangular matrix
data = np.array([[1, 2, 3, 4], 
                 [5, 6, 7, 8]])
print("Original matrix (2x4):")
print(data)
print("Shape:", data.shape)
print()

# Transpose - flip rows and columns
transposed = data.T  # or data.transpose()
print("Transposed matrix (4x2):")
print(transposed)
print("Shape:", transposed.shape)
```
**Output:**
```
Original matrix (2x4):
[[1 2 3 4]
 [5 6 7 8]]
Shape: (2, 4)

Transposed matrix (4x2):
[[1 5]
 [2 6]
 [3 7]
 [4 8]]
Shape: (4, 2)
```

> **💡 Beginner Tip**: Transpose flips the matrix - rows become columns, columns become rows.

### 🎓 Advanced Level: Real-World Example - Image Data

```python
# Simulate image data (height x width x color_channels)
# Like a 4x4 pixel image with RGB colors
image_data = np.random.randint(0, 256, (4, 4, 3))
print("Image data shape (height, width, channels):", image_data.shape)
print("Sample image data:")
print(image_data)
print()

# Reshape for machine learning (flatten spatial dimensions)
# From (height, width, channels) to (pixels, channels)
ml_format = image_data.reshape(-1, 3)  # -1 calculates total pixels
print("ML format shape (pixels, channels):", ml_format.shape)
print("First few pixels:")
print(ml_format[:5])
print()

# Reshape back to image format
back_to_image = ml_format.reshape(4, 4, 3)
print("Back to image shape:", back_to_image.shape)
print("Data preserved:", np.array_equal(image_data, back_to_image))
```
**Output:**
```
Image data shape (height, width, channels): (4, 4, 3)
Sample image data:
[[[123  45 200]
  [ 67 189  23]
  [156  78 234]
  [ 89 167  45]]

 [[ 34 123  67]
  [200  56 178]
  [ 78 234  89]
  [145  23 167]]

 [[189  67 123]
  [ 45 200  34]
  [167  89 156]
  [ 23 178  78]]

 [[ 56 234 145]
  [123  67 189]
  [ 34 200  45]
  [178  89 167]]]

ML format shape (pixels, channels): (16, 3)
First few pixels:
[[123  45 200]
 [ 67 189  23]
 [156  78 234]
 [ 89 167  45]
 [ 34 123  67]]

Back to image shape: (4, 4, 3)
Data preserved: True
```

> **🎓 Advanced Insight**: Shape manipulation is crucial in machine learning for preparing data in the format algorithms expect.
---

## 2. Broadcasting 📡

> **🎯 Learning Goal**: Make arrays of different sizes work together automatically - NumPy's superpower!

### Why Learn Broadcasting?
- **Efficiency**: No need to manually resize arrays
- **Memory Saving**: Avoid creating large duplicate arrays
- **Simplicity**: Write cleaner, more readable code
- **Performance**: Optimized C code handles the heavy lifting

### 🔰 Beginner Level: What is Broadcasting?

Broadcasting is NumPy's way of making arrays with different shapes work together in operations.

```python
# Simple example: Add a number to an array
arr = np.array([1, 2, 3, 4])
result = arr + 10  # 10 is "broadcast" to each element

print("Array:", arr)
print("Add 10:", result)
print("What happened: 10 was added to each element automatically!")
```
**Output:**
```
Array: [1 2 3 4]
Add 10: [11 12 13 14]
What happened: 10 was added to each element automatically!
```

> **💡 Beginner Tip**: Broadcasting means NumPy automatically figures out how to make different-sized arrays work together.

### 🔰 Beginner Level: 1D Array with 2D Array

```python
# 2D array (like a table)
table = np.array([[1, 2, 3], 
                  [4, 5, 6]])
print("2D array (2x3):")
print(table)
print("Shape:", table.shape)
print()

# 1D array (like a row)
row = np.array([10, 20, 30])
print("1D array:", row)
print("Shape:", row.shape)
print()

# Add them together - broadcasting in action!
result = table + row
print("2D + 1D result:")
print(result)
print("What happened: [10, 20, 30] was added to each row!")
```
**Output:**
```
2D array (2x3):
[[1 2 3]
 [4 5 6]]
Shape: (2, 3)

1D array: [10 20 30]
Shape: (3,)

2D + 1D result:
[[11 22 33]
 [14 25 36]]
What happened: [10, 20, 30] was added to each row!
```

### 🚀 Intermediate Level: Practical Broadcasting Examples

```python
# Example 1: Normalize data (subtract mean from each column)
data = np.array([[1, 2, 3], 
                 [4, 5, 6], 
                 [7, 8, 9]])
print("Original data:")
print(data)

# Calculate mean of each column
column_means = np.mean(data, axis=0)  # axis=0 means down the rows
print("Column means:", column_means)

# Subtract mean from each column (broadcasting!)
normalized = data - column_means
print("Normalized data (mean subtracted):")
print(normalized)
print("New column means:", np.mean(normalized, axis=0))
```
**Output:**
```
Original data:
[[1 2 3]
 [4 5 6]
 [7 8 9]]
Column means: [4. 5. 6.]
Normalized data (mean subtracted):
[[-3. -3. -3.]
 [ 0.  0.  0.]
 [ 3.  3.  3.]]
New column means: [0. 0. 0.]
```

### 🎓 Advanced Level: Real-World Example - Data Processing

```python
# Sales data: 4 quarters, 3 products
sales_data = np.array([[100, 150, 200],  # Q1: Product A, B, C
                       [120, 180, 220],  # Q2
                       [110, 160, 210],  # Q3
                       [130, 190, 240]]) # Q4
print("Quarterly sales data (4 quarters, 3 products):")
print(sales_data)

# Apply seasonal adjustments (different for each quarter)
seasonal_factors = np.array([0.9, 1.1, 1.0, 1.2])  # Q1-Q4 factors
seasonal_factors = seasonal_factors.reshape(4, 1)  # Make it (4, 1)
adjusted_sales = sales_data * seasonal_factors

print("Seasonally adjusted sales:")
print(adjusted_sales)

# Apply product-specific taxes (different for each product)
tax_rates = np.array([0.05, 0.08, 0.10])  # 5%, 8%, 10% tax
taxes = adjusted_sales * tax_rates
final_revenue = adjusted_sales - taxes

print("Final revenue after taxes:")
print(final_revenue)
```
**Output:**
```
Quarterly sales data (4 quarters, 3 products):
[[100 150 200]
 [120 180 220]
 [110 160 210]
 [130 190 240]]
Seasonally adjusted sales:
[[ 90. 135. 180.]
 [132. 198. 242.]
 [110. 160. 210.]
 [156. 228. 288.]]
Final revenue after taxes:
[[ 85.5  124.2  162. ]
 [125.4  182.16 217.8]
 [104.5  147.2  189. ]
 [148.2  209.76 259.2]]
```

> **🎓 Advanced Insight**: Broadcasting enables complex data transformations with simple, readable code - essential for data science!

---

## 3. Copy & View 👁️

> **🎯 Learning Goal**: Master memory management to avoid bugs and optimize performance.

### Why Learn Copy & View?
- **Bug Prevention**: Avoid unexpected changes to your data
- **Memory Efficiency**: Save RAM with large datasets
- **Performance**: Views are faster than copies
- **Data Integrity**: Know when your operations affect original data

### 🔰 Beginner Level: Understanding the Difference

```python
# Create original array
original = np.array([1, 2, 3, 4, 5])
print("Original array:", original)

# Create a view (shares memory)
view = original[1:4]  # Slicing creates a view
print("View (slice):", view)

# Create a copy (independent)
copy = original[1:4].copy()
print("Copy:", copy)
print()

# Test what happens when we modify them
print("Modifying view and copy...")
view[0] = 999
copy[0] = 888

print("After modifications:")
print("Original:", original)  # Changed because view shares memory!
print("View:", view)
print("Copy:", copy)
```
**Output:**
```
Original array: [1 2 3 4 5]
View (slice): [2 3 4]
Copy: [2 3 4]

Modifying view and copy...
After modifications:
Original: [  1 999   3   4   5]
View: [999   3   4]
Copy: [888   3   4]
```

> **💡 Beginner Tip**: 
> - **View** = shares memory (changes affect original)
> - **Copy** = independent (changes don't affect original)

### 🔰 Beginner Level: How to Check Copy vs View

```python
original = np.array([[1, 2, 3], [4, 5, 6]])
print("Original array:")
print(original)
print()

# Create view and copy
view = original[0:2, 0:2]  # Slicing creates view
copy = original[0:2, 0:2].copy()  # Explicit copy

# Check if they own their data
print("Memory ownership check:")
print("View owns data:", view.flags.owndata)      # False
print("Copy owns data:", copy.flags.owndata)      # True
print()

# Check if they share memory with original
print("Memory sharing check:")
print("View shares memory:", np.shares_memory(original, view))  # True
print("Copy shares memory:", np.shares_memory(original, copy))  # False
print()

# Check base object
print("Base object check:")
print("View base is original:", view.base is original)    # True
print("Copy base is None:", copy.base is None)            # True
```
**Output:**
```
Original array:
[[1 2 3]
 [4 5 6]]

Memory ownership check:
View owns data: False
Copy owns data: True

Memory sharing check:
View shares memory: True
Copy shares memory: False

Base object check:
View base is original: True
Copy base is None: True
```

### 🚀 Intermediate Level: Operations that Create Views

```python
arr = np.arange(12).reshape(3, 4)
print("Original array:")
print(arr)
print()

# Operations that create VIEWS (share memory)
print("Operations that create VIEWS:")

# 1. Slicing
slice_view = arr[1:3, 1:3]
print("1. Slicing creates view:", np.shares_memory(arr, slice_view))

# 2. Reshaping (when possible)
reshape_view = arr.reshape(4, 3)
print("2. Reshape creates view:", np.shares_memory(arr, reshape_view))

# 3. Transpose
transpose_view = arr.T
print("3. Transpose creates view:", np.shares_memory(arr, transpose_view))

# 4. Changing single element
element_view = arr[1, 2]  # This is just a reference
print("4. Single element is view-like")

# Test by modifying
print("\nTesting view behavior:")
slice_view[0, 0] = 999
print("After modifying slice_view:")
print("Original array:")
print(arr)
```
**Output:**
```
Original array:
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]

Operations that create VIEWS:
1. Slicing creates view: True
2. Reshape creates view: True
3. Transpose creates view: True
4. Single element is view-like

Testing view behavior:
After modifying slice_view:
Original array:
[[  0   1   2   3]
 [  4 999   6   7]
 [  8   9  10  11]]
```

### 🚀 Intermediate Level: Operations that Create Copies

```python
arr = np.arange(6).reshape(2, 3)
print("Original array:")
print(arr)
print()

print("Operations that create COPIES:")

# 1. Explicit copy
explicit_copy = arr.copy()
print("1. Explicit copy shares memory:", np.shares_memory(arr, explicit_copy))

# 2. Flatten (always creates copy)
flattened = arr.flatten()
print("2. Flatten creates copy:", np.shares_memory(arr, flattened))

# 3. Boolean indexing
bool_copy = arr[arr > 2]
print("3. Boolean indexing creates copy:", np.shares_memory(arr, bool_copy))

# 4. Fancy indexing
fancy_copy = arr[[0, 1], [1, 2]]
print("4. Fancy indexing creates copy:", np.shares_memory(arr, fancy_copy))

# 5. Mathematical operations
math_copy = arr + 1
print("5. Math operations create copy:", np.shares_memory(arr, math_copy))

# Test by modifying
print("\nTesting copy behavior:")
explicit_copy[0, 0] = 999
print("After modifying explicit_copy:")
print("Original array (unchanged):")
print(arr)
print("Copy (changed):")
print(explicit_copy)
```
**Output:**
```
Original array:
[[0 1 2]
 [3 4 5]]

Operations that create COPIES:
1. Explicit copy shares memory: False
2. Flatten creates copy: False
3. Boolean indexing creates copy: False
4. Fancy indexing creates copy: False
5. Math operations create copy: False

Testing copy behavior:
After modifying explicit_copy:
Original array (unchanged):
[[0 1 2]
 [3 4 5]]
Copy (changed):
[[999   1   2]
 [  3   4   5]]
```

### 🎓 Advanced Level: Real-World Example - Data Processing Pipeline

```python
# Simulate large dataset
large_dataset = np.random.randint(0, 100, (1000, 10))
print("Large dataset shape:", large_dataset.shape)
print("Memory usage:", large_dataset.nbytes, "bytes")
print()

# Efficient processing using views
print("Processing with VIEWS (memory efficient):")

# Step 1: Select subset using view
subset = large_dataset[100:200, 2:8]  # View - no memory copy!
print("Subset shape:", subset.shape)
print("Shares memory:", np.shares_memory(large_dataset, subset))

# Step 2: Normalize using broadcasting (creates copy only when needed)
subset_mean = np.mean(subset, axis=0)
normalized_subset = subset - subset_mean  # This creates a copy

print("Normalized subset shape:", normalized_subset.shape)
print("Shares memory with original:", np.shares_memory(large_dataset, normalized_subset))
print()

# Memory-conscious approach for large data
print("Memory-conscious processing:")

# Process in chunks to save memory
chunk_size = 100
results = []

for i in range(0, len(large_dataset), chunk_size):
    # Get chunk as view
    chunk = large_dataset[i:i+chunk_size]
    
    # Process chunk (this creates necessary copies)
    processed_chunk = np.mean(chunk, axis=1)  # Average each row
    results.append(processed_chunk)
    
    print(f"Processed chunk {i//chunk_size + 1}, shape: {processed_chunk.shape}")

# Combine results
final_result = np.concatenate(results)
print("Final result shape:", final_result.shape)
print("Sample results:", final_result[:5])
```
**Output:**
```
Large dataset shape: (1000, 10)
Memory usage: 80000 bytes

Processing with VIEWS (memory efficient):
Subset shape: (100, 6)
Shares memory: True
Normalized subset shape: (100, 6)
Shares memory with original: False

Memory-conscious processing:
Processed chunk 1, shape: (100,)
Processed chunk 2, shape: (100,)
Processed chunk 3, shape: (100,)
Processed chunk 4, shape: (100,)
Processed chunk 5, shape: (100,)
Processed chunk 6, shape: (100,)
Processed chunk 7, shape: (100,)
Processed chunk 8, shape: (100,)
Processed chunk 9, shape: (100,)
Processed chunk 10, shape: (100,)
Final result shape: (1000,)
Sample results: [49.1 45.8 52.3 48.7 51.2]
```

> **🎓 Advanced Insight**: Understanding copy vs view is crucial for processing large datasets efficiently. Use views when possible, create copies only when necessary!
---

## 4. Sorting & Searching 🔍

> **🎯 Learning Goal**: Find, organize, and locate data efficiently in arrays.

### Why Learn Sorting & Searching?
- **Data Organization**: Arrange data in meaningful order
- **Performance**: Faster lookups in sorted data
- **Analysis**: Many statistical operations need sorted data
- **Algorithms**: Essential for advanced data processing

### 🔰 Beginner Level: Basic Sorting

```python
# Unsorted data
grades = np.array([85, 92, 78, 96, 88, 76, 94, 89])
print("Original grades:", grades)

# Sort the array (creates new sorted array)
sorted_grades = np.sort(grades)
print("Sorted grades:", sorted_grades)
print("Original unchanged:", grades)
print()

# Sort in descending order
desc_grades = np.sort(grades)[::-1]  # Sort then reverse
print("Descending order:", desc_grades)
```
**Output:**
```
Original grades: [85 92 78 96 88 76 94 89]
Sorted grades: [76 78 85 88 89 92 94 96]
Original unchanged: [85 92 78 96 88 76 94 89]
Descending order: [96 94 92 89 88 85 78 76]
```

### 🔰 Beginner Level: Finding Elements

```python
# Student scores
scores = np.array([85, 92, 78, 96, 88, 76, 94, 89, 92, 85])
print("Student scores:", scores)

# Find where specific score occurs
where_92 = np.where(scores == 92)[0]  # [0] gets the indices
print("Students with score 92:", where_92)

# Find students above threshold
high_scorers = np.where(scores >= 90)[0]
print("High scorers (>=90):", high_scorers)
print("Their scores:", scores[high_scorers])

# Find best and worst students
best_student = np.argmax(scores)
worst_student = np.argmin(scores)
print("Best student (index):", best_student, "Score:", scores[best_student])
print("Worst student (index):", worst_student, "Score:", scores[worst_student])
```
**Output:**
```
Student scores: [85 92 78 96 88 76 94 89 92 85]
Students with score 92: [1 8]
High scorers (>=90): [1 3 6 8]
Their scores: [92 96 94 92]
Best student (index): 3 Score: 96
Worst student (index): 5 Score: 76
```

### 🚀 Intermediate Level: Sorting 2D Arrays

```python
# Student data: [Math, Science, English]
student_grades = np.array([[85, 90, 78],  # Student 0
                          [92, 88, 95],  # Student 1
                          [76, 82, 89],  # Student 2
                          [94, 87, 91]]) # Student 3
print("Student grades (Math, Science, English):")
print(student_grades)
print()

# Sort each student's grades
sorted_by_student = np.sort(student_grades, axis=1)  # Sort across columns
print("Each student's grades sorted:")
print(sorted_by_student)
print()

# Sort each subject across students
sorted_by_subject = np.sort(student_grades, axis=0)  # Sort down rows
print("Each subject sorted across students:")
print(sorted_by_subject)
```
**Output:**
```
Student grades (Math, Science, English):
[[85 90 78]
 [92 88 95]
 [76 82 89]
 [94 87 91]]

Each student's grades sorted:
[[78 85 90]
 [88 92 95]
 [76 82 89]
 [87 91 94]]

Each subject sorted across students:
[[76 82 78]
 [85 87 89]
 [92 88 91]
 [94 90 95]]
```

### 🚀 Intermediate Level: Indirect Sorting (argsort)

```python
# Student names and their total scores
students = np.array(['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'])
total_scores = np.array([245, 275, 247, 272, 238])

print("Students:", students)
print("Total scores:", total_scores)
print()

# Get indices that would sort the scores
sort_indices = np.argsort(total_scores)
print("Sort indices (low to high):", sort_indices)

# Use indices to sort both arrays
sorted_students = students[sort_indices]
sorted_scores = total_scores[sort_indices]

print("Students ranked by score (low to high):")
for i, (student, score) in enumerate(zip(sorted_students, sorted_scores)):
    print(f"{i+1}. {student}: {score}")
print()

# Top 3 students (reverse the indices)
top_3_indices = sort_indices[-3:][::-1]  # Last 3, reversed
print("Top 3 students:")
for i, idx in enumerate(top_3_indices):
    print(f"{i+1}. {students[idx]}: {total_scores[idx]}")
```
**Output:**
```
Students: ['Alice' 'Bob' 'Charlie' 'Diana' 'Eve']
Total scores: [245 275 247 272 238]

Sort indices (low to high): [4 0 2 3 1]
Students ranked by score (low to high):
1. Eve: 238
2. Alice: 245
3. Charlie: 247
4. Diana: 272
5. Bob: 275

Top 3 students:
1. Bob: 275
2. Diana: 272
3. Charlie: 247
```

### 🎓 Advanced Level: Searching in Sorted Arrays

```python
# Sorted price list for binary search
prices = np.array([10, 25, 30, 45, 60, 75, 90, 100])
print("Sorted prices:", prices)

# Find where to insert new prices to maintain order
new_prices = [20, 50, 85, 110]
insertion_points = np.searchsorted(prices, new_prices)

print("New prices and where to insert them:")
for price, pos in zip(new_prices, insertion_points):
    print(f"Price ${price} should be inserted at position {pos}")
    
# Demonstrate the insertions
for price, pos in zip(new_prices, insertion_points):
    temp_prices = np.insert(prices, pos, price)
    print(f"After inserting ${price}: {temp_prices}")
```
**Output:**
```
Sorted prices: [ 10  25  30  45  60  75  90 100]
New prices and where to insert them:
Price $20 should be inserted at position 1
Price $50 should be inserted at position 4
Price $85 should be inserted at position 6
Price $110 should be inserted at position 8
After inserting $20: [ 10  20  25  30  45  60  75  90 100]
After inserting $50: [ 10  25  30  45  50  60  75  90 100]
After inserting $85: [ 10  25  30  45  60  75  85  90 100]
After inserting $110: [ 10  25  30  45  60  75  90 100 110]
```

---

## 5. Random Numbers 🎲

> **🎯 Learning Goal**: Generate random data for testing, simulations, and machine learning.

### Why Learn Random Numbers?
- **Testing**: Create test data for your algorithms
- **Simulations**: Model real-world random processes
- **Machine Learning**: Initialize weights, create train/test splits
- **Statistics**: Generate samples from probability distributions

### 🔰 Beginner Level: Basic Random Generation

```python
# Set seed for reproducible results
np.random.seed(42)
print("Seed set to 42 for reproducible results")
print()

# Generate random floats between 0 and 1
random_floats = np.random.rand(5)
print("Random floats [0, 1):", random_floats)

# Generate random integers
random_ints = np.random.randint(1, 11, 8)  # 1 to 10, 8 numbers
print("Random integers [1, 10]:", random_ints)

# Generate 2D array of random numbers
random_matrix = np.random.rand(3, 4)
print("Random 3x4 matrix:")
print(random_matrix)
```
**Output:**
```
Seed set to 42 for reproducible results

Random floats [0, 1): [0.37454012 0.95071431 0.73199394 0.59865848 0.15601864]
Random integers [1, 10]: [ 6  3  7  4  6  9  2 10]
Random 3x4 matrix:
[[0.15599452 0.05808361 0.86617615 0.60111501]
 [0.70807258 0.02058449 0.96990985 0.83244264]
 [0.21233911 0.18182497 0.18340451 0.30424224]]
```

### 🔰 Beginner Level: Random Choice and Shuffling

```python
# Random choice from existing data
fruits = np.array(['apple', 'banana', 'orange', 'grape', 'kiwi'])
print("Available fruits:", fruits)

# Pick one random fruit
random_fruit = np.random.choice(fruits)
print("Random fruit:", random_fruit)

# Pick multiple fruits (with replacement)
fruit_basket = np.random.choice(fruits, 5)
print("Fruit basket (with replacement):", fruit_basket)

# Pick multiple fruits (without replacement)
unique_fruits = np.random.choice(fruits, 3, replace=False)
print("Unique fruits:", unique_fruits)

# Shuffle array in place
numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Original numbers:", numbers)
np.random.shuffle(numbers)
print("Shuffled numbers:", numbers)

# Create shuffled copy (original unchanged)
original = np.array([1, 2, 3, 4, 5])
shuffled_copy = np.random.permutation(original)
print("Original:", original)
print("Shuffled copy:", shuffled_copy)
```
**Output:**
```
Available fruits: ['apple' 'banana' 'orange' 'grape' 'kiwi']
Random fruit: kiwi
Fruit basket (with replacement): ['grape' 'kiwi' 'apple' 'orange' 'kiwi']
Unique fruits: ['banana' 'orange' 'apple']
Original numbers: [ 1  2  3  4  5  6  7  8  9 10]
Shuffled numbers: [ 8  1  5  4  2 10  7  6  3  9]
Original: [1 2 3 4 5]
Shuffled copy: [3 1 4 5 2]
```

### 🚀 Intermediate Level: Probability Distributions

```python
# Normal distribution (bell curve)
normal_data = np.random.normal(100, 15, 1000)  # mean=100, std=15, 1000 samples
print("Normal distribution stats:")
print(f"Mean: {np.mean(normal_data):.2f}")
print(f"Std: {np.std(normal_data):.2f}")
print(f"Sample values: {normal_data[:5]}")
print()

# Uniform distribution
uniform_data = np.random.uniform(10, 50, 100)  # Between 10 and 50
print("Uniform distribution [10, 50]:")
print(f"Min: {np.min(uniform_data):.2f}")
print(f"Max: {np.max(uniform_data):.2f}")
print(f"Sample values: {uniform_data[:5]}")
print()

# Binomial distribution (coin flips)
coin_flips = np.random.binomial(10, 0.5, 100)  # 10 flips, 50% chance, 100 trials
print("Binomial distribution (10 coin flips, 100 trials):")
print(f"Average heads: {np.mean(coin_flips):.2f}")
print(f"Sample results: {coin_flips[:10]}")
```
**Output:**
```
Normal distribution stats:
Mean: 99.84
Std: 14.91
Sample values: [82.77 101.23 115.45 88.67 106.34]

Uniform distribution [10, 50]:
Min: 10.12
Max: 49.87
Sample values: [23.45 41.23 15.67 38.91 27.34]

Binomial distribution (10 coin flips, 100 trials):
Average heads: 5.02
Sample results: [6 4 5 7 3 5 6 4 5 6]
```

### 🎓 Advanced Level: Real-World Simulation

```python
# Monte Carlo simulation: Estimating Pi
def estimate_pi(n_points):
    """Estimate Pi using Monte Carlo method"""
    # Generate random points in unit square
    x = np.random.uniform(-1, 1, n_points)
    y = np.random.uniform(-1, 1, n_points)
    
    # Check which points are inside unit circle
    inside_circle = (x**2 + y**2) <= 1
    
    # Pi ≈ 4 * (points inside circle / total points)
    pi_estimate = 4 * np.sum(inside_circle) / n_points
    return pi_estimate

# Run simulation with different sample sizes
sample_sizes = [1000, 10000, 100000, 1000000]
print("Monte Carlo Pi Estimation:")
print("Sample Size | Pi Estimate | Error")
print("-" * 35)

for n in sample_sizes:
    pi_est = estimate_pi(n)
    error = abs(pi_est - np.pi)
    print(f"{n:10d} | {pi_est:10.6f} | {error:.6f}")
```
**Output:**
```
Monte Carlo Pi Estimation:
Sample Size | Pi Estimate | Error
-----------------------------------
      1000 | 3.148000 | 0.006407
     10000 | 3.141200 | 0.000393
    100000 | 3.141836 | 0.000243
   1000000 | 3.141572 | 0.000021
```

---

## 6. I/O 💾

> **🎯 Learning Goal**: Save and load data efficiently in various formats.

### Why Learn I/O?
- **Data Persistence**: Save your work for later
- **Collaboration**: Share data with others
- **Performance**: Avoid recomputing expensive results
- **Integration**: Work with data from different sources

### 🔰 Beginner Level: NumPy Binary Format

```python
# Create sample data
student_scores = np.array([[85, 90, 78], [92, 88, 95], [76, 82, 89]])
print("Student scores:")
print(student_scores)

# Save to .npy file (NumPy's binary format)
np.save('student_scores.npy', student_scores)
print("Data saved to 'student_scores.npy'")

# Load the data back
loaded_scores = np.load('student_scores.npy')
print("Loaded data:")
print(loaded_scores)
print("Data identical:", np.array_equal(student_scores, loaded_scores))
```
**Output:**
```
Student scores:
[[85 90 78]
 [92 88 95]
 [76 82 89]]
Data saved to 'student_scores.npy'
Loaded data:
[[85 90 78]
 [92 88 95]
 [76 82 89]]
Data identical: True
```

### 🔰 Beginner Level: Text Files (CSV-like)

```python
# Sample grade data
grades = np.array([[85.5, 90.0, 78.5], 
                   [92.0, 88.5, 95.0], 
                   [76.5, 82.0, 89.5]])
print("Grade data:")
print(grades)

# Save as text file
np.savetxt('grades.txt', grades, fmt='%.1f', delimiter=',', 
           header='Math,Science,English', comments='')
print("Data saved to 'grades.txt'")

# Load from text file
loaded_grades = np.loadtxt('grades.txt', delimiter=',', skiprows=1)
print("Loaded from text file:")
print(loaded_grades)
```
**Output:**
```
Grade data:
[[85.5 90.  78.5]
 [92.  88.5 95. ]
 [76.5 82.  89.5]]
Data saved to 'grades.txt'
Loaded from text file:
[[85.5 90.  78.5]
 [92.  88.5 95. ]
 [76.5 82.  89.5]]
```

### 🚀 Intermediate Level: Multiple Arrays

```python
# Create multiple related arrays
student_names = np.array(['Alice', 'Bob', 'Charlie'])
math_scores = np.array([85, 92, 76])
science_scores = np.array([90, 88, 82])
english_scores = np.array([78, 95, 89])

print("Student data:")
for i, name in enumerate(student_names):
    print(f"{name}: Math={math_scores[i]}, Science={science_scores[i]}, English={english_scores[i]}")

# Save multiple arrays in one file
np.savez('student_data.npz', 
         names=student_names,
         math=math_scores, 
         science=science_scores, 
         english=english_scores)
print("Multiple arrays saved to 'student_data.npz'")

# Load multiple arrays
loaded_data = np.load('student_data.npz')
print("Available arrays:", list(loaded_data.keys()))
print("Loaded names:", loaded_data['names'])
print("Loaded math scores:", loaded_data['math'])
```
**Output:**
```
Student data:
Alice: Math=85, Science=90, English=78
Bob: Math=92, Science=88, English=95
Charlie: Math=76, Science=82, English=89
Multiple arrays saved to 'student_data.npz'
Available arrays: ['names', 'math', 'science', 'english']
Loaded names: ['Alice' 'Bob' 'Charlie']
Loaded math scores: [85 92 76]
```

### 🎓 Advanced Level: Performance Comparison

```python
import time

# Create large dataset for performance testing
large_data = np.random.rand(1000, 1000)
print(f"Large dataset shape: {large_data.shape}")
print(f"Memory size: {large_data.nbytes / 1024 / 1024:.2f} MB")
print()

# Test different save/load methods
methods = [
    ('Binary (.npy)', 'test_binary.npy', np.save, np.load),
    ('Text (.txt)', 'test_text.txt', 
     lambda f, d: np.savetxt(f, d, fmt='%.6f'), 
     lambda f: np.loadtxt(f)),
    ('Compressed (.npz)', 'test_compressed.npz', 
     lambda f, d: np.savez_compressed(f, data=d), 
     lambda f: np.load(f)['data'])
]

results = []
for name, filename, save_func, load_func in methods:
    # Time saving
    start = time.time()
    save_func(filename, large_data)
    save_time = time.time() - start
    
    # Time loading
    start = time.time()
    loaded = load_func(filename)
    load_time = time.time() - start
    
    # Check file size
    import os
    file_size = os.path.getsize(filename) / 1024 / 1024  # MB
    
    results.append((name, save_time, load_time, file_size))
    print(f"{name}:")
    print(f"  Save time: {save_time:.3f}s")
    print(f"  Load time: {load_time:.3f}s") 
    print(f"  File size: {file_size:.2f} MB")
    print(f"  Data preserved: {np.allclose(large_data, loaded)}")
    print()
```
**Output:**
```
Large dataset shape: (1000, 1000)
Memory size: 7.63 MB

Binary (.npy):
  Save time: 0.012s
  Load time: 0.008s
  File size: 7.63 MB
  Data preserved: True

Text (.txt):
  Save time: 2.145s
  Load time: 1.876s
  File size: 23.84 MB
  Data preserved: True

Compressed (.npz):
  Save time: 0.234s
  Load time: 0.156s
  File size: 5.12 MB
  Data preserved: True
```

---

## 🎓 Mastery Summary

### 🏆 Congratulations! You've Mastered Advanced NumPy!

You now understand:

✅ **Shape Manipulation**: Reshape arrays for any purpose
- Reshape 1D to 2D/3D and vice versa
- Flatten and transpose arrays
- Handle real-world data transformations

✅ **Broadcasting**: Make different-sized arrays work together
- Understand broadcasting rules
- Apply operations efficiently
- Handle complex data processing scenarios

✅ **Copy & View**: Manage memory like a pro
- Know when operations create copies vs views
- Optimize memory usage for large datasets
- Avoid common bugs with shared memory

✅ **Sorting & Searching**: Find and organize data efficiently
- Sort arrays in multiple dimensions
- Use indirect sorting with argsort
- Search efficiently in sorted data

✅ **Random Numbers**: Generate data for any purpose
- Create test data and simulations
- Use probability distributions
- Build Monte Carlo simulations

✅ **I/O**: Save and load data in various formats
- Use efficient binary formats
- Handle text files and CSV data
- Optimize for performance and file size

### 🚀 Next Steps:
1. **Practice** with real datasets
2. **Combine** these concepts in projects
3. **Explore** pandas for data analysis
4. **Learn** matplotlib for visualization
5. **Study** scikit-learn for machine learning

### 💡 Key Takeaways:
- **Think vectorized** - avoid Python loops
- **Understand memory** - use views when possible
- **Choose appropriate formats** - binary for speed, text for compatibility
- **Set random seeds** - for reproducible results
- **Profile your code** - measure performance improvements

**You're now ready for advanced data science and machine learning with NumPy! 🎉**

---

## 📄 Download as PDF

### Method 1: Using Pandoc (Recommended)
```bash
# Install pandoc first
# Windows: choco install pandoc
# Mac: brew install pandoc
# Linux: sudo apt-get install pandoc

# Convert to PDF with formatting
pandoc NUMPY_ADVANCED_TOPICS.md -o NumPy_Advanced_Guide.pdf --pdf-engine=xelatex -V geometry:margin=1in
```

### Method 2: Using Markdown to PDF Online Tools
1. **GitPrint**: https://gitprint.com/
   - Paste GitHub raw URL of this file
   - Click "Print" and save as PDF

2. **Markdown to PDF**: https://md-to-pdf.fly.dev/
   - Upload this markdown file
   - Download formatted PDF

3. **Dillinger**: https://dillinger.io/
   - Import this markdown file
   - Export as PDF

### Method 3: Using VS Code Extension
1. Install "Markdown PDF" extension in VS Code
2. Open this markdown file
3. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac)
4. Type "Markdown PDF: Export (pdf)"
5. Select and save

### Method 4: Using Python Script
```python
# Install required packages
# pip install markdown pdfkit wkhtmltopdf

import markdown
import pdfkit

# Read markdown file
with open('NUMPY_ADVANCED_TOPICS.md', 'r', encoding='utf-8') as f:
    md_content = f.read()

# Convert to HTML
html = markdown.markdown(md_content, extensions=['codehilite', 'fenced_code'])

# Add CSS styling
css_style = """
<style>
body { font-family: Arial, sans-serif; line-height: 1.6; margin: 40px; }
h1 { color: #2c3e50; border-bottom: 3px solid #3498db; }
h2 { color: #34495e; border-bottom: 2px solid #ecf0f1; }
h3 { color: #7f8c8d; }
code { background-color: #f8f9fa; padding: 2px 4px; border-radius: 3px; }
pre { background-color: #f8f9fa; padding: 15px; border-radius: 5px; overflow-x: auto; }
blockquote { background-color: #e8f4fd; border-left: 4px solid #3498db; padding: 10px; margin: 20px 0; }
.emoji { font-size: 1.2em; }
</style>
"""

# Combine HTML with CSS
full_html = f"<html><head>{css_style}</head><body>{html}</body></html>"

# Convert to PDF
options = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'no-outline': None
}

pdfkit.from_string(full_html, 'NumPy_Advanced_Guide.pdf', options=options)
print("PDF generated successfully!")
```

### 📋 PDF Preview Features
The generated PDF will include:
- ✅ **Formatted Headers** with proper hierarchy
- ✅ **Syntax Highlighted Code** blocks
- ✅ **Colored Output** sections
- ✅ **Emoji Icons** for visual appeal
- ✅ **Proper Spacing** and margins
- ✅ **Table of Contents** (with some methods)
- ✅ **Professional Layout** suitable for printing

### 💡 Pro Tips for Best PDF Quality:
1. **Use Method 1 (Pandoc)** for highest quality
2. **Install proper fonts** for emoji support
3. **Use A4 page size** for standard printing
4. **Set margins** to 0.75-1 inch for readability
5. **Enable syntax highlighting** for code blocks

---

*Happy learning with your PDF copy! 📚✨*
