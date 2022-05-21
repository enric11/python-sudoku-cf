# Sudoku generator

This code provides a sudoku generator

## Installation

Use the package manager [pip](https://pypi.org/project/py-sudoku/) autoinstalled with cf deploy.

```bash
cf deploy
```

## Usage

```python
#Generate the board
def generator():
```

```json
{"difficulty": 0.5, "board": [[7, null, null, null, null, 9, null, 2, 5], [null, null, null, 1, 7, 8, null, 6, null], [null, 6, 9, null, 2, null, null, 7, null], [5, null, 3, null, 1, 2, 8, null, 6], [8, null, 2, null, 4, 3, 7, null, 1], [4, null, null, null, 5, 7, 9, null, 2], [6, 2, null, null, null, 4, 5, 9, null], [3, 5, null, null, 9, null, null, null, 7], [null, null, null, null, 3, 6, 2, null, null]], "with": 3, "height": 3, "boardSolution": [[7, 3, 8, 4, 6, 9, 1, 2, 5], [2, 4, 5, 1, 7, 8, 3, 6, 9], [1, 6, 9, 3, 2, 5, 4, 7, 8], [5, 7, 3, 9, 1, 2, 8, 4, 6], [8, 9, 2, 6, 4, 3, 7, 5, 1], [4, 1, 6, 8, 5, 7, 9, 3, 2], [6, 2, 1, 7, 8, 4, 5, 9, 3], [3, 5, 4, 2, 9, 1, 6, 8, 7], [9, 8, 7, 5, 3, 6, 2, 1, 4]]}
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)