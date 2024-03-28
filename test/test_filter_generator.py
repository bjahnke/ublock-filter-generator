import pytest
import csv
from src.filter_generator import load_csv_file

class TestLoadCSVFile:
    def test_load_csv_file(self):
        file_path = '/path/to/test.csv'
        expected_data = [['row1', 'value1'], ['row2', 'value2'], ['row3', 'value3']]
        
        # Create a test CSV file with the expected data
        with open(file_path, 'w') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(expected_data)
        
        # Call the function and check if the returned data matches the expected data
        actual_data = load_csv_file(file_path)
        self.assertEqual(actual_data, expected_data)