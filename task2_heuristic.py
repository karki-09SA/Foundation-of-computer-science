import time
import math

students = [
    "Alice", "Bob", "Charlie", "Diana", "Eve",
    "Frank", "Grace", "Henry", "Isla", "Jack"
]

city_groups = {
    "Kathmandu" : ["Alice", "Charlie", "Grace"],
    "Pokhara"   : ["Bob", "Diana", "Henry"],
    "Chitwan"   : ["Eve", "Frank"],
    "Butwal"    : ["Isla", "Jack"],
}

same_city_pairs = set()
for city, members in city_groups.items():
    for i in range(len(members)):
        for j in range(i + 1, len(members)):
            same_city_pairs.add((members[i], members[j]))
            same_city_pairs.add((members[j], members[i]))

friendships = {
    ("Alice", "Bob"),
    ("Charlie", "Diana"),
    ("Eve", "Frank"),
    ("Grace", "Henry"),
    ("Isla", "Jack"),
    ("Bob", "Grace"),
    ("Alice", "Henry"),
}

def are_conflicting(s1, s2):
    if (s1, s2) in friendships or (s2, s1) in friendships:
        return True
    if (s1, s2) in same_city_pairs or (s2, s1) in same_city_pairs:
        return True
    return False

def count_conflicts(student, all_students):
    return sum(1 for s in all_students if s != student and are_conflicting(student, s))

def is_valid_arrangement(arrangement):
    for i in range(len(arrangement) - 1):
        if are_conflicting(arrangement[i], arrangement[i + 1]):
            return False
    return True

def can_place(student, position, arrangement):
    if position > 0 and are_conflicting(arrangement[position - 1], student):
        return False
    return True

attempts = [0]

def backtrack_solve(ordered_students):
    arrangement = []

    def backtrack(remaining):
        if not remaining:
            return True
        for i, student in enumerate(remaining):
            attempts[0] += 1
            if can_place(student, len(arrangement), arrangement):
                arrangement.append(student)
                new_remaining = remaining[:i] + remaining[i+1:]
                if backtrack(new_remaining):
                    return True
                arrangement.pop()
        return False

    if backtrack(list(ordered_students)):
        return arrangement
    return None

print("=" * 60)
print("     HEURISTIC SEATING ARRANGEMENT SOLVER")
print("=" * 60)
print(f"\nStudents ({len(students)}): {students}")
print(f"\nCity Groups:")
for city, members in city_groups.items():
    print(f"  {city:12}: {members}")

total_brute = math.factorial(len(students))
print(f"\nBrute force would need: {total_brute:,} arrangements")

print("\n" + "-" * 60)
print("HEURISTIC 1: Most Constrained Student First")
print("-" * 60)

conflict_counts = {s: count_conflicts(s, students) for s in students}
print("\nConflict counts:")
for s, c in sorted(conflict_counts.items(), key=lambda x: -x[1]):
    print(f"  {s:10}: {c} conflicts")

ordered_h1 = sorted(students, key=lambda s: count_conflicts(s, students), reverse=True)
print(f"\nOrder: {ordered_h1}")

attempts[0] = 0
start = time.time()
result_h1 = backtrack_solve(ordered_h1)
end = time.time()

print(f"\nResult       : {' | '.join(result_h1) if result_h1 else 'No solution'}")
print(f"Valid        : {is_valid_arrangement(result_h1) if result_h1 else 'N/A'}")
print(f"Attempts     : {attempts[0]}")
print(f"Time         : {round(end - start, 5)} seconds")

print("\n" + "-" * 60)
print("HEURISTIC 2: Separate Same-City Students Early")
print("-" * 60)

city_buckets = list(city_groups.values())
ordered_h2 = []
max_len = max(len(b) for b in city_buckets)
for i in range(max_len):
    for bucket in city_buckets:
        if i < len(bucket):
            ordered_h2.append(bucket[i])
for s in students:
    if s not in ordered_h2:
        ordered_h2.append(s)

print(f"\nOrder: {ordered_h2}")

attempts[0] = 0
start = time.time()
result_h2 = backtrack_solve(ordered_h2)
end = time.time()

print(f"\nResult       : {' | '.join(result_h2) if result_h2 else 'No solution'}")
print(f"Valid        : {is_valid_arrangement(result_h2) if result_h2 else 'N/A'}")
print(f"Attempts     : {attempts[0]}")
print(f"Time         : {round(end - start, 5)} seconds")

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"\nBrute Force   : {total_brute:,} arrangements - impractical")
print(f"Heuristic 1   : {attempts[0]} attempts - fast")
print(f"Heuristic 2   : {attempts[0]} attempts - fast")
print("\nHeuristics trade guaranteed optimality for speed.")
