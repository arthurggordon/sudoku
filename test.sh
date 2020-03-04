docker run -it --rm \
  --mount type=bind,source="$(pwd -P)/src",destination=/app \
    sudoku-debug pytest