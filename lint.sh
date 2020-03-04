
docker run --rm \
  --mount type=bind,source="$(pwd -P)/src",destination=/app/src \
    sudoku-debug flake8 src


docker run --rm \
  --mount type=bind,source="$(pwd -P)/src",destination=/app/src \
    sudoku-debug mypy --ignore-missing-imports src
