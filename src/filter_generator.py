from ast import List
import csv
# util
def load_csv_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data


# domain

def create_filter(source, element, phrase):
    return f"{source}##li:has({element}:has-text({phrase}))"


def create_filters(data: List[List[str, str, str]]):
    filters = []
    for row in data:
        filters.append(create_filter(row[0], row[1], row[2]))
    return filters


# logic



# Example usage
csv_data = load_csv_file('/path/to/csv/file.csv')
filter_builder = FilterBuilder('example.com', '.class')
for row in csv_data:
    filter_str = filter_builder.create_filter(row[0])
    print(filter_str)