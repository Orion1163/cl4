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



Practical 4: Perform the data clustering algorithm using any Clustering algorithm
Theory
Clustering is an unsupervised machine learning technique used to group similar data points together based on specific characteristics or patterns without having predefined labels. Unlike classification, clustering doesn’t require labeled data. Instead, it tries to find hidden structures within the data.

The main goal of clustering is to divide the data into groups (clusters) such that data points in the same cluster are more similar to each other than to those in other clusters.

Types of Clustering Algorithms:
K-Means Clustering

Partitions the data into K clusters.

Each data point is assigned to the nearest cluster center (centroid).

Centroids are updated iteratively until convergence.

Hierarchical Clustering

Builds a tree (dendrogram) of clusters either by merging or dividing clusters.

Doesn’t require the number of clusters to be specified in advance.

DBSCAN (Density-Based Spatial Clustering of Applications with Noise)

Groups together points that are closely packed.

Can identify outliers and noise in the data.

Mean Shift Clustering

Shifts data points towards the mode (densest part) of the data.

Does not need the number of clusters in advance.

Steps in Clustering:
Data Collection – Gather raw data for analysis.

Data Preprocessing – Normalize or scale the data, handle missing values.

Algorithm Selection – Choose a suitable clustering algorithm based on data structure.

Apply Clustering – Run the algorithm to group data into clusters.

Evaluation – Use metrics like Silhouette Score or visual methods to evaluate cluster quality.

Visualization – Represent the clusters using graphs or plots to interpret the results.

Advantages of Clustering:
Works well with unlabeled data.

Helps to discover hidden patterns or groupings.

Useful for exploratory data analysis.

Applications of Clustering:
Customer segmentation in marketing.

Grouping genes with similar expression patterns in bioinformatics.

Document or news article grouping.

Image compression and pattern recognition.

Let me know the title of the next practical when you're ready!







You said:
Exploring Student Grade Calculation with MapReduce.


ChatGPT said:
Here is the detailed theory for your practical titled:

Practical 5: Exploring Student Grade Calculation with MapReduce
Theory
MapReduce is a powerful programming model introduced by Google for processing large-scale data in a distributed computing environment. It breaks down a task into two main phases: Map and Reduce. This approach is especially useful for performing calculations over large datasets in parallel, efficiently and reliably.

In this practical, the focus is on calculating student grades using the MapReduce model. The goal is to analyze student records (such as marks in different subjects) and compute useful insights like total marks, average, and grade assignment.

MapReduce Phases Explained:
Map Phase

Processes input key-value pairs and produces intermediate key-value pairs.

In this context, the input could be student ID and their list of marks.

The Map function extracts relevant data, e.g., emits (studentID, marks).

Shuffle and Sort Phase

The intermediate data is grouped by key (student ID) and sorted.

This step prepares data for the Reduce phase.

Reduce Phase

Aggregates or performs computations on all values associated with a key.

In this case, it might calculate total marks, average, and assign a grade.

Why MapReduce for Grade Calculation?
Suitable for large datasets with many student records.

Processes data in parallel, increasing speed and efficiency.

Makes it easy to apply consistent rules for grade calculation across all records.

Grade Calculation Logic (General)
Calculate total marks across all subjects.

Compute the average by dividing the total by the number of subjects.

Assign grades based on average:

A: 90 and above

B: 80–89

C: 70–79

D: 60–69

F: Below 60

Applications of MapReduce:
Student data analysis at a university level.

Processing logs and records in bulk.

Large-scale business intelligence tasks.

Survey or feedback analysis.

Advantages:
Scalability: Handles massive datasets across distributed systems.

Fault Tolerance: Can recover from node failures.

Flexibility: Can be adapted for many use cases, including academic and administrative tasks.

