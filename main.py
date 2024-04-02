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
    in_default = './sample-io/block-elements.csv'
    out_default = './sample-io/filters.txt'
    filters_gen_config = './src/filters.json'

    parser = argparse.ArgumentParser(description='Filter Generator')
    parser.add_argument('-i', '--input', type=str, default=in_default, help='input CSV file')
    parser.add_argument('-o', '--output', type=str, default=out_default, help='output TXT file')
    
    args = parser.parse_args()
    input_csv = args.input
    output_txt = args.output

    # Load CSV file
    data = load_csv_file(input_csv)

    filter_manager = FilterManager()

    # Add filter generators to filter manager
    with open(filters_gen_config, 'r') as file:
        filter_generators_raw = json.load(file)
    
    for filter_generator in filter_generators_raw:
        filter_manager.add_filter_generator(filter_generator)

    # Create filters
    for filter_data in data:
        filter_manager.add_filter(filter_data.source, filter_data.element_type, filter_data.phrase)


    # Write filters to output file
    with open(output_txt, 'w') as file:
        file.write(str(filter_manager))

    print(f"Filters generated and saved to {output_txt}")


if __name__ == "__main__":
    main()