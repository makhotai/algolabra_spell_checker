# README
This is implementation of terminal based spell-checker using Damerau-Levenshtein distance and Trie data-structure.

## Documentation 
* [Project specification](./documentation/specification.md)
* [User guide](./documentation/userguide.md)
* [Implementation report](./documentation/implementation.md)
* [Testing report](./documentation/testing.md)

## Running the program


Install Poetry dependencies using command:
```
poetry install
```

## Running the program

To run the program:
```
poetry run invoke start
```
## Running tests

To run unit tests:
```
poetry run invoke test
```

To compile coverage report:
```
poetry run invoke coverage
```

To run Pylint tests:
```
poetry run invoke pylint
```