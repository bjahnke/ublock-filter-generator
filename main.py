import json
import sys
import argparse
import csv
from typing import Tuple, List
from src.logic.filter_manager import FilterManager
from src.domain.filter_generator import FilterData

# util
def load_csv_file(file_path) -> List[FilterData]:
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        cols = next(csv_reader)
        
        for row in csv_reader:
            data.append(FilterData(**dict(zip(cols, row))))
    return data



def main():
    """
    main program:
    - process command line arguments
    - load CSV file
    - init filter manager
    - create filters and ouput filters to txt file
    """
    parser = argparse.ArgumentParser(description='Filter Generator')
    parser.add_argument('input_csv', type=str, help='input CSV file')
    parser.add_argument('output_txt', type=str, nargs='?', default='filters.txt', help='output TXT file')
    
    try:
        args = parser.parse_args()
    except:
        input_csv = './sample-io/block-elements.csv'
        output_txt = './sample-io/filters.txt'
    else:
        input_csv = args.input_csv
        output_txt = args.output_txt

    # Load CSV file
    data = load_csv_file(input_csv)

    filter_manager = FilterManager()

    # Add filter generators to filter manager
    with open('./src/filters.json', 'r') as file:
        filter_generators_raw = json.load(file)
    
    for filter_generator in filter_generators_raw:
        filter_manager.add_filter_generator(filter_generator)

    # Create filters
    for filter_data in data:
        filter_manager.add_filter(filter_data.source, filter_data.element_type, filter_data.phrase)


    # Write filters to output file
    with open(output_txt, 'w') as file:
        file.write(str(filter_manager))


if __name__ == "__main__":
    main()