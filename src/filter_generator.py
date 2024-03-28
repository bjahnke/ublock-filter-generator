from typing import List, Tuple
import csv
import sys
import argparse

# util
def load_csv_file(file_path) -> Tuple[List[List[str]], List[str]]:
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data[1:], data[0]





# domain

def create_filter(source, element, phrase) -> str:
    return f"{source}##li:has({element}:has-text({phrase}))"


# logic

class FilterApply:
    filter_lookup = {
        "www.linkedin.com": {
            "company": ".job-card-container__primary-description",
            "title": ".job-card-list__title"
        }
    }

    @staticmethod
    def create_filters(data: List[List[str]]):
        """assume 3 strings in each row"""
        filters = []
        for row in data:
            source = row[0]
            filter_type = row[2]
            phrase = row[1]
            try:
                element = FilterApply.filter_lookup[source][filter_type]
            except KeyError:
                print(f"Element not found for {source} and {filter_type}")
                continue

            filters.append(create_filter(source, element, phrase))
        return filters


def main():
    parser = argparse.ArgumentParser(description='Filter Generator')
    parser.add_argument('input_csv', type=str, help='input CSV file')
    parser.add_argument('output_txt', type=str, nargs='?', default='filters.txt', help='output TXT file')
    args = parser.parse_args()

    input_csv = args.input_csv
    output_txt = args.output_txt

    # Load CSV file
    data, headers = load_csv_file(input_csv)

    # Create filters
    filters = FilterApply.create_filters(data)

    # Write filters to output file
    with open(output_txt, 'w') as file:
        for filter in filters:
            file.write(filter + '\n')

if __name__ == "__main__":
    main()