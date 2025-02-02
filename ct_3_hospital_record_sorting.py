import random
import string
import time
import datetime
import copy
from memory_profiler import memory_usage

# ----------------------------
# Data Generation
# ----------------------------

def random_name(length=7):
    """Generate a random string of uppercase letters to simulate patient name."""
    return ''.join(random.choices(string.ascii_uppercase, k=length))

def random_date(start_year=2015, end_year=2024):
    """Generate a random date."""
    start_date = datetime.date(start_year, 1, 1)
    end_date = datetime.date(end_year, 12, 31)
    delta_days = (end_date - start_date).days
    random_days = random.randint(0, delta_days)
    date_result = start_date + datetime.timedelta(days=random_days)
    return date_result.isoformat()

def generate_patient_records(n):
    """Generate n patient records with random data.
    
    Each record is a dictionary with the following keys:
      - patient_id: Unique integer ID
      - name: Randomly generated name
      - age: Random age between 1 and 100
      - admission_date: A random date string
      - diagnosis: Random diagnosis from a fixed list
    """
    diagnoses = ["Flu", "Cold", "COVID-19", "Allergy", "Asthma", "Diabetes", "Hypertension", "Migraine"]
    
    # Create patient_ids from 1 to n and then shuffle to randomize order.
    patient_ids = list(range(1, n + 1))
    random.shuffle(patient_ids)
    
    records = []
    for pid in patient_ids:
        record = {
            "patient_id": pid,
            "name": random_name(),
            "age": random.randint(1, 100),
            "admission_date": random_date(),
            "diagnosis": random.choice(diagnoses)
        }
        records.append(record)
    
    return records

# ----------------------------
# Sorting Algorithms
# ----------------------------

def bubble_sort(records):
    """Sort the list of records in-place using bubble sort based on patient_id."""
    n = len(records)
    for i in range(n):
        # Optimization: Track if any swap happened. If not, the list is sorted.
        swapped = False
        for j in range(0, n - i - 1):
            if records[j]["patient_id"] > records[j + 1]["patient_id"]:
                records[j], records[j + 1] = records[j + 1], records[j]
                swapped = True
        if not swapped:
            break
    return records

def merge_sort(records):
    """Sort the list of records using merge sort based on patient_id."""
    if len(records) <= 1:
        return records

    mid = len(records) // 2
    left_half = merge_sort(records[:mid])
    right_half = merge_sort(records[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    """Merge two sorted lists of records."""
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i]["patient_id"] <= right[j]["patient_id"]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # Append any remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# ----------------------------
# Timing and Memory Profiling
# ----------------------------

def profile_sort(sort_func, data):
    """
    Profiles the given sort function using memory_profiler and time.
    Returns the sorted data, time taken, and peak memory usage.
    """
    # Use a deep copy of data to ensure each sort works on identical input
    data_copy = copy.deepcopy(data)

    # Record start time
    start_time = time.time()
    
    # Use memory_usage to measure the memory footprint of the sorting function.
    # The function will run with the data_copy as argument.
    mem_usage, sorted_result = memory_usage(
        (sort_func, (data_copy,), {}),
        retval=True,
        interval=0.1,
        timeout=None
    )
    end_time = time.time()
    time_taken = end_time - start_time
    peak_memory = max(mem_usage) if mem_usage else None
    
    return sorted_result, time_taken, peak_memory

# ----------------------------
# Main Execution
# ----------------------------

def main():
    NUM_RECORDS = 100000 
    print(f"Generating {NUM_RECORDS} patient records...")
    records = generate_patient_records(NUM_RECORDS)
    print("Data generation complete.\n")
    
    # Bubble Sort Profiling
    print("Starting Bubble Sort...")
    sorted_bubble, time_bubble, mem_bubble = profile_sort(bubble_sort, records)
    print("Bubble Sort complete.")
    print(f"Records processed: {NUM_RECORDS}")
    print(f"Time taken (Bubble Sort): {time_bubble:.4f} seconds")
    print(f"Peak memory usage (Bubble Sort): {mem_bubble:.2f} MiB\n")
    
    # Merge Sort Profiling
    print("Starting Merge Sort...")
    sorted_merge, time_merge, mem_merge = profile_sort(merge_sort, records)
    print("Merge Sort complete.")
    print(f"Records processed: {NUM_RECORDS}")
    print(f"Time taken (Merge Sort): {time_merge:.4f} seconds")
    print(f"Peak memory usage (Merge Sort): {mem_merge:.2f} MiB")

if __name__ == "__main__":
    main()
