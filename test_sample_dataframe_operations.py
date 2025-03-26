# test_sample_dataframe_operations.py
import pytest
import pandas as pd
from sample_dataframe_operations import (
    filter_dataframe,
    calculate_average,
    add_column,
    create_sample_dataframe,
)

def test_filter_dataframe():
    df = create_sample_dataframe()
    filtered_df = filter_dataframe(df, 'city', 'London')
    assert len(filtered_df) == 1
    assert filtered_df['name'].iloc[0] == 'Bob'

def test_calculate_average():
    df = create_sample_dataframe()
    average_age = calculate_average(df, 'age')
    assert average_age == 28.0

def test_add_column():
    df = create_sample_dataframe()
    updated_df = add_column(df.copy(), 'country', 'Various') #using .copy to avoid modifying the original dataframe.
    assert 'country' in updated_df.columns
    assert all(updated_df['country'] == 'Various')

def test_create_sample_dataframe():
    df = create_sample_dataframe()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 5
    assert list(df.columns) == ['name', 'city', 'age', 'salary']


def test_filter_nonexistent_column():
    df = create_sample_dataframe()
    with pytest.raises(KeyError):
        filter_dataframe(df, 'nonexistent_column', 'value')