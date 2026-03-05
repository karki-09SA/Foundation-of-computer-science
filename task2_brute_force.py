from itertools import permutations
import time
import math

students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

friendships = {
    ("Alice", "Bob"),
    ("Bob", "Charlie"),
    ("Diana", "Eve"),
    ("Alice", "Eve"),
}

same_city = {
    ("Alice", "Charlie"),
    ("Bob", "Diana"),
}

def are_conflicting(s1, s2):
    pair = (s1, s2)
    rpair = (s2, s1)
    if pair in friendships or rpair in friendships:
        return True
    if pair in same_city or rpair in same_city:
        return True
    return False

def is_valid_arrangement(arrangement):
    for i in range(len(arrangement) - 1):
        if are_conflicting(arrangement[i], arrangement[i + 1]):
            return False
    return True

print("=" * 55)
print("   BRUTE FORCE SEATING ARRANGEMENT SOLVER")
print("=" * 55)
print(f"\nStudents    : {students}")
print(f"\nRule 1: Friends cannot sit next to each other")
print(f"Rule 2: Same city students cannot sit next to each other")

total = math.factorial(len(students))
print(f"\nTotal arrangements to check: {total}")

start_time = time.time()
checked = 0
valid_found = []

for perm in permutations(students):
    checked += 1
    if is_valid_arrangement(perm):
        valid_found.append(perm)

end_time = time.time()

print(f"\nChecked    : {checked}")
print(f"Time taken : {round(end_time - start_time, 4)} seconds")
print(f"Valid found: {len(valid_found)}")

if valid_found:
    print("\n--- Valid Arrangements ---")
    for i, arr in enumerate(valid_found, 1):
        print(f"  Option {i}: {' | '.join(arr)}")
else:
    print("\nNo valid arrangement exists.")

print("\n" + "=" * 55)
print("   FACTORIAL COMPLEXITY TABLE")
print("=" * 55)
print(f"\n{'Students':>10} | {'Arrangements (n!)':>25} | Estimated Time")
print("-" * 60)
speed = 1_000_000_000
for n in [5, 10, 15, 20, 25, 30]:
    fact = math.factorial(n)
    seconds = fact / speed
    if seconds < 60:
        time_str = f"{round(seconds, 4)} sec"
    elif seconds < 3600:
        time_str = f"{round(seconds/60, 2)} mins"
    elif seconds < 86400:
        time_str = f"{round(seconds/3600, 2)} hrs"
    elif seconds < 31536000:
        time_str = f"{round(seconds/86400, 2)} days"
    elif seconds < 31536000 * 1000:
        time_str = f"{round(seconds/31536000, 2)} years"
    else:
        time_str = f"{seconds/31536000:.2e} years"
    print(f"{n:>10} | {fact:>25,} | {time_str}")

print("\nBrute force only works for very small inputs!")
