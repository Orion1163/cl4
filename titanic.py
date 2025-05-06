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
