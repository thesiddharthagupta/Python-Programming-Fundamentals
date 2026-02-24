# Original tuple
original_tuple = (10, 20, 30, 40)

# Method 1: Direct assignment (creates a reference, not a true copy)
copy_tuple1 = original_tuple

# Method 2: Using tuple() constructor
copy_tuple2 = tuple(original_tuple)

# Method 3: Using slicing
copy_tuple3 = original_tuple[:]

# Display results
print("Original Tuple:", original_tuple)
print("Copy using assignment:", copy_tuple1)
print("Copy using tuple():", copy_tuple2)
print("Copy using slicing:", copy_tuple3)

# Check if they are the same object
print("Is copy_tuple1 same object as original?", copy_tuple1 is original_tuple)
print("Is copy_tuple2 same object as original?", copy_tuple2 is original_tuple)
print("Is copy_tuple3 same object as original?", copy_tuple3 is original_tuple)