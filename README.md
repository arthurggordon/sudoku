# Sudoku solver
Simple sudoku solver written in Python. 

A sudoku to solve looks like this example:
```
sudoku1 = [
    [0,1,0, 0,0,5, 0,8,3],
    [0,0,0, 8,0,0, 0,2,0],
    [0,0,0, 0,9,0, 0,0,5],
    
    [3,0,0, 0,6,9, 0,0,7],
    [0,0,6, 0,0,0, 5,0,0],
    [4,0,0, 7,3,0, 0,0,6],
    
    [7,0,0, 0,4,0, 0,0,0],
    [0,4,0, 0,0,3, 0,0,0],
    [8,6,0, 2,0,0, 0,1,0],
]
```
Where ```0``` indicates that this element is unknown.

Note that if insufficent elements  are provided (less than 17) the solver will find multiple solutions.

## Build
To build the code run the following:
```
./build.sh
```
This will create a docker image `sudoku`.
As well as a `sudoku-debug` image used by the linting, formatting and debugging scripts

## Run
To execute the code: 
```
./run.sh
```
This will execute the `sudoku` docker image created in the build step and wull produce output similar to:
```
no of solutions = 1
solution = 1
------------
[ [2, 1, 9, 6, 7, 5, 4, 8, 3],
  [5, 3, 7, 8, 1, 4, 6, 2, 9],
  [6, 8, 4, 3, 9, 2, 1, 7, 5],
  [3, 2, 1, 5, 6, 9, 8, 4, 7],
  [9, 7, 6, 4, 2, 8, 5, 3, 1],
  [4, 5, 8, 7, 3, 1, 2, 9, 6],
  [7, 9, 2, 1, 4, 6, 3, 5, 8],
  [1, 4, 5, 9, 8, 3, 7, 6, 2],
  [8, 6, 3, 2, 5, 7, 9, 1, 4]]
```

## Developer Tools
To lint the code and perform checks of the typing using mypy:
```
./lint.sh
```
To correct the formatting of the Python source code:
```
./format.sh
```
To debug the Python source code:
```
./debug.sh
```
