
docker run --rm \
  --mount type=bind,source="$(pwd -P)/src",destination=/app/src \
    sudoku-debug black src

  