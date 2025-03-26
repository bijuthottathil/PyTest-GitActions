# sample_dataframe_operations.py
import pandas as pd

def filter_dataframe(df, column, value):
    """Filters a DataFrame based on a column and value."""
    return df[df[column] == value]

def calculate_average(df, column):
    """Calculates the average of a specified column."""
    return df[column].mean()

def add_column(df, new_column, value):
    """Adds a new column to the DataFrame with a given value."""
    df[new_column] = value
    return df

def create_sample_dataframe():
    """Creates a sample Pandas DataFrame."""
    data = {
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'city': ['New York', 'London', 'Tokyo', 'Paris', 'Sydney'],
        'age': [25, 30, 22, 35, 28],
        'salary': [50000, 60000, 45000, 70000, 55000]
    }
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = create_sample_dataframe()
    print(df)