from collections import defaultdict

# Map function: Emits tuples of student_id and score
def map_function(student_scores):
    for student_id, score in student_scores:
        yield student_id, score

# Reduce function: Assigns grades based on scores
def reduce_function(mapped_data):
    grades = {}
    for student_id, score in mapped_data:
        if score > 80:
            grade = 'A'
        elif score > 60:
            grade = 'B'
        elif score > 40:
            grade = 'C'
        else:
            grade = 'D'
        grades[student_id] = grade
    return grades

# Simulates the MapReduce process
def map_reduce(student_scores):
    mapped_data = list(map_function(student_scores))
    grades = reduce_function(mapped_data)
    return grades

# Load student scores from external text file
def load_scores_from_file(filename):
    student_scores = []
    with open(filename, 'r') as file:
        for line in file:
            if line.strip():
                parts = line.strip().replace(',', ' ').split()
                name = parts[0]
                score = int(parts[1])
                student_scores.append((name, score))
    return student_scores


# Path to your file
file_path = 'student_scores_multi_names.txt'  # Change this to your actual file name

# Load, process, and print results
student_scores = load_scores_from_file(file_path)
grades = map_reduce(student_scores)

for student_id, grade in grades.items():
    print(f"Student {student_id} has been assigned grade {grade}.")

