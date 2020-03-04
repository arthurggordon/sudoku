#!/bin/bash

docker build --target debug --tag "sudoku-debug" .
docker build --tag "sudoku" .