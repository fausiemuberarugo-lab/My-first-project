# Project 63: Crops Yield Tally
# This is my attempt to track crop yields and do some calculations!

# Integers: Let's start with some sample yield data
yields = [45, 67, 23, 89, 34]  # These are the crop quantities

# Compute total, average, minimum, and maximum
total = sum(yields)  # Adding up all the yields
average = total / len(yields)  # Dividing by the number of items for average
minimum = min(yields)  # Finding the smallest yield
maximum = max(yields)  # Finding the biggest yield

# Printing the results
print("Total Yield:", total)
print("Average Yield:", average)
print("Minimum Yield:", minimum)
print("Maximum Yield:", maximum)

# Strings: Making a simple report
print("Crops Yield Tally Report:")
print(f"Total yield is {total} and the average is {average}.")  # First string
print(f"The range is from {minimum} to {maximum}.")  # Second string

# Booleans: Checking against a threshold
threshold = 50  # Setting a threshold value
if average > threshold and total > 200:  # Compound condition
    print("Above Standard! Great job!")
else:
    print("Below Standard. Need to improve.")

# Lists: Working with the yield list
print("Original List:", yields)
yields.append(55)  # Adding a new yield
for i in range(len(yields)):  # Simple loop to find and remove a value
    if yields[i] < 30:
        yields.pop(i)
        break  # Stop after removing one
yields.sort()  # Sorting the list
print("List after adding, removing, and sorting:", yields)

# Arrays: Using array module for a fixed-size subset
import array
array_yields = array.array('i', yields[:3])  # Taking first 3 values
array_total = sum(array_yields)  # Sum of array
print("Array Subset:", list(array_yields))
print("Array Total:", array_total)


# Dictionaries: Creating a list of dictionaries
yield_records = [
    {"id": 1, "name": "Wheat", "value": 45},
    {"id": 2, "name": "Corn", "value": 67},
    {"id": 3, "name": "Rice", "value": 23}
]
# Update one record
yield_records[0]["value"] = 50
# Delete another
del yield_records[1]
# Compute total value
total_value = 0
for record in yield_records:
    total_value += record["value"]
print("Updated Records:", yield_records)
print("Total value of all records:", total_value)
