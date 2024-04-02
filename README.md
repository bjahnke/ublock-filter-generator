# Filter Generator

This project generates filters compatible with UBlock Origin to block unwanted jobs in linkedin. It can create filters to block job posts by company name or by job title.

## CSV Format

The input CSV file should have the following columns:

- `source`: The website where the filter will be applied. Currently, only "linkedin" is supported.
- `type`: The type of element to block. This can be "company" or "title".
- `phrase`: The phrase to match in order to block the element.

Here's an example of what the CSV file might look like:

| source | phrase | type |
| -------- | -------- | -------- |
| linkedin  | Unwanted Company | company |
| linkedin  | Unwanted Job Title | title |
| teamblind  | Jobot | company |
| all  | Sales | title |


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6 or higher
- pip

### Installation

1. Clone the repository:
```sh
git clone https://github.com/bjahnke/filter-generator.git
```

2. Navigate to the project directory:
```sh
cd path/to/filter-generator
```

## Usage

Run the script with the input CSV file as an argument:

```sh
python main.py sample-io/block-elements.csv
```

By default, the filters will be written to `filters.txt`. You can specify a different output file as a second argument:

```sh
python main.py sample-io/block-elements.csv output.txt
```

## Running the Tests

You can run the tests with pytest:

```sh
python -m pytest test/
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
```
