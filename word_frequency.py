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
