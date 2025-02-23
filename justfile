# Testament - Justfile utility

# Print list of available recipe (this)
default:
    @just --list --unsorted

# Run poetry install in all submodules
install:
    poetry install

# Run the CLI tool with Poetry
testament *ARGS:
    @poetry run testament {{ ARGS }}

# Run pytest via poetry
pytest *ARGS:

# Run test coverage
coverage:
    poetry run coverage run --source=testament --omit="*/__*.py,*/test_*.py" -m pytest
    poetry run coverage report -m

# Verify that the test coverage is within acceptable levels
coverage-sheriff MIN="80":
    poetry run coverage xml -q --omit="*/__*.py,*/test_*.py" -o coverage.xml
    poetry run python3 ./tools/coverage_sheriff.py --minimum {{ MIN }}
