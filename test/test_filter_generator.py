import pytest
import csv
from main import load_csv_file
from src.domain.filter_generator import FilterData
import csv
import random
from pathlib import Path
from src.domain.filter_generator import FilterData, FilterGenerator

def create_test_csv_file(data, file_path=Path('.') / 'test' / 'test.csv'):

    # Generate random data for the CSV file

    # Write the data to the CSV file
    with open(file_path, 'w') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)


class TestLoadCSVFile:
    def test_column_order(self):
        """Test if the function returns the correct data regardless of the CSV column order"""
        file_path = Path('.') / 'test' / 'test.csv'
        expected_data = [['source', 'element_type', 'phrase'], ['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3']]
        create_test_csv_file(expected_data, file_path)
        
        # Call the function and check if the returned data matches the expected data
        actual_data = load_csv_file(file_path)
        assert actual_data == [FilterData('a1', 'a2', 'a3'), FilterData('b1', 'b2', 'b3'), FilterData('c1', 'c2', 'c3')]

        expected_data = [['element_type', 'phrase', 'source'], ['a2', 'a3', 'a1'], ['b2', 'b3', 'b1'], ['c2', 'c3', 'c1']]
        create_test_csv_file(expected_data, file_path)
        actual_data = load_csv_file(file_path)
        assert actual_data == [FilterData('a1', 'a2', 'a3'), FilterData('b1', 'b2', 'b3'), FilterData('c1', 'c2', 'c3')]


# Existing test code...

class TestFilterGenerator:
    def test_create_filter(self):
        """Test if the create_filter method returns the correct filter"""
        source = 'example'
        filter_str = 'example-filter'
        selectors = {'element1': 'selector1', 'element2': 'selector2'}
        generator = FilterGenerator(source, filter_str, selectors)

        # Test with valid element and phrase
        element = 'element1'
        phrase = 'example-phrase'
        expected_filter = f'www.{source}.com##{filter_str.format(element=selectors[element], phrase=phrase)}'
        actual_filter = generator.create_filter(element, phrase)
        assert actual_filter == expected_filter

        # Test with invalid element
        element = 'element3'
        phrase = 'example-phrase'
        expected_filter = None
        actual_filter = generator.create_filter(element, phrase)
        assert actual_filter == expected_filter

        # Test with empty phrase
        element = 'element2'
        phrase = ''
        expected_filter = f'www.{source}.com##{filter_str.format(element=selectors[element], phrase=phrase)}'
        actual_filter = generator.create_filter(element, phrase)
        assert actual_filter == expected_filter

class TestFilterData:
    def test_str(self):
        """Test the __str__ method of FilterData"""
        data = FilterData('example', 'element1', 'example-phrase')
        expected_str = "example, element1, example-phrase"
        assert str(data) == expected_str

    def test_eq(self):
        """Test the __eq__ method of FilterData"""
        data1 = FilterData('example', 'element1', 'example-phrase')
        data2 = FilterData('example', 'element1', 'example-phrase')
        data3 = FilterData('example', 'element2', 'example-phrase')
        assert data1 == data2
        assert data1 != data3

    def test_hash(self):
        """Test the __hash__ method of FilterData"""
        data1 = FilterData('example', 'element1', 'example-phrase')
        data2 = FilterData('example', 'element1', 'example-phrase')
        data3 = FilterData('example', 'element2', 'example-phrase')
        assert hash(data1) == hash(data2)
        assert hash(data1) != hash(data3)