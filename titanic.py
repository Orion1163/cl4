import pandas as pd

def map_reduce_with_pandas(input_file):
    # Load the dataset
    df = pd.read_csv("titanic_dataset.csv")

    # Map: Filter deceased males
    deceased_males = df[(df['Survived'] == 0) & (df['Sex'] == 'male')]

    # Reduce: Calculate average age of deceased males
    average_age_deceased_males = deceased_males['Age'].mean()

    # Map: Filter deceased females
    deceased_females_by_class = df[(df['Survived'] == 0) & (df['Sex'] == 'female')]

    # Reduce: Count deceased females by class
    count_deceased_females_by_class = deceased_females_by_class['Pclass'].value_counts()

    return average_age_deceased_males, count_deceased_females_by_class
                                      
                                      
average_age, female_class_count = map_reduce_with_pandas("titanic_dataset.csv")

print(f"Average age of deceased males: {average_age:.2f}")
print("Number of deceased females in each class:")
print(female_class_count)



Practical 8: Analyzing Titanic Data with MapReduce: Gender-based Analysis of Casualties
Theory
MapReduce is a distributed data processing model that simplifies the processing of large datasets across multiple nodes. It consists of two major phases: Map and Reduce. This practical applies the MapReduce model to analyze the Titanic dataset with a focus on gender-based casualties.

The Titanic dataset is a popular real-world dataset that contains passenger details such as name, age, gender, class, and survival status. Using MapReduce, we can efficiently process this data to understand survival patterns based on gender.

Objective of the Practical:
To analyze how gender influenced the survival rates during the Titanic disaster using the MapReduce model.

MapReduce Phases in This Context:
Map Phase

Each input record (a line of Titanic data) is parsed to extract gender and survival status.

The Map function emits key-value pairs like:

(male, survived)

(female, not_survived)

Shuffle and Sort Phase

Groups all values by gender.

Helps in preparing data for reducing based on gender classification.

Reduce Phase

Counts the number of survivors and casualties for each gender.

Calculates survival and death ratios for males and females.

Expected Analysis Outcome:
Total number of males and females.

Number of male and female survivors.

Number of male and female casualties.

Comparative analysis to determine which gender had a higher survival rate.

Why Use MapReduce for Titanic Data Analysis?
Efficient processing of large-scale data in distributed environments.

Enables parallel processing, making it faster and scalable.

Allows customizable logic for specific analysis like gender-based filtering.

Applications:
Historical data analysis for insights and trends.

Policy-making and research in disaster management.

Demonstrating the use of distributed computing on real datasets.

Advantages:
Handles large datasets like Titanic records effortlessly.

Ensures fault tolerance and scalability in processing.

Promotes structured and repeatable analysis over complex data.
