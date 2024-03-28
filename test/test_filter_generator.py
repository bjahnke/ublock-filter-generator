import pytest
import csv
from src.filter_generator import load_csv_file
import csv
import random
from pathlib import Path

def create_test_csv_file(data, file_path=Path('.') / 'test' / 'test.csv'):

    # Generate random data for the CSV file

    # Write the data to the CSV file
    with open(file_path, 'w') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)


class TestLoadCSVFile:
    def test_load_csv_file(self):
        file_path = Path('.') / 'test' / 'test.csv'
        expected_data = [['col1', 'col2', 'col3'], ['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3']]
        
        create_test_csv_file(expected_data, file_path)
        
        # Call the function and check if the returned data matches the expected data
        actual_data, header = load_csv_file(file_path)
        assert actual_data == expected_data[1:]
        assert header == expected_data[0]