# Data Capture Challenge

The challenge is to create a program that computes some
basic statistics on a collection of small positive integers. You
can assume all values will be less than 1,000.

## Requirements

The DataCapture object accepts numbers and returns an object for querying
statistics about the inputs. Specifically, the returned object supports
querying how many numbers in the collection are less than a value, greater
than a value, or within a range.

### Challenge conditions:

- You cannot import a library that solves it instantly
- The methods add(), less(), greater(), and between() should have
constant time O(1)
- The method build_stats() can be at most linear O(n)
- Apply the best practices you know
- Share a public repo with your project


## Setup

- Clone the repo.
- Create a virtual environment `pienv install`.
- Activate it.

## Usage

Run the command: `python src/main.py`

## Testing

Run the command: `pipenv run pytest`

