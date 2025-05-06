def map_reduce(file_path, target_word):
    word_count = 0

    with open(file_path, 'r') as file:
        # Map phase: Emit each word with count 1
        mapped_data = [(word.lower(), 1) 
                       for line in file 
                       for word in line.strip().split()]

    # Reduce phase: Aggregate counts for the target word
    for word, count in mapped_data:
        if word == target_word.lower():
            word_count += count

    return word_count

# Example usage
file_path = 'index.txt'  # Update to your actual file path
target_word = "Pranav"

# Calculate the frequency of the target word in the file
frequency = map_reduce(file_path, target_word)

print(f"The word '{target_word}' appears {frequency} times.")


Practical 5: Exploring Word Frequency Calculation Using MapReduce Paradigm
Theory
The MapReduce paradigm is a programming model used for processing large-scale datasets in a distributed computing environment. It works by dividing the task into two main functions: Map and Reduce. In this practical, we use MapReduce to perform word frequency calculation, which is a fundamental example of text processing.

Objective of the Practical:
To count how many times each word appears in a given large text file using the MapReduce framework.

Working of MapReduce in This Practical:
Map Phase

The input text is split into lines or chunks.

Each line is processed to break it into individual words.

For every word, the mapper emits a key-value pair:
word → 1

Shuffle and Sort Phase

The framework groups all identical words together.

For example, all pairs like ("data", 1), ("data", 1) will be grouped as:
data → [1, 1]

Reduce Phase

The reducer takes each group and sums the values.

This gives the total frequency of each word:
data → 2

Why Use MapReduce for Word Frequency?
Handles massive volumes of text data (like books, logs, or web pages).

Automatically distributes processing across multiple nodes.

Provides fault-tolerance and scalability for large data tasks.

Applications:
Search engines (indexing and ranking pages).

Text mining and sentiment analysis.

Spam filtering and document classification.

Real-time log analysis and social media monitoring.

Advantages:
Parallel and distributed processing improves speed.

Can handle unstructured data efficiently.

Simplifies the logic of word counting using key-value pairs.
