#!/bin/sh

set -e

cd $(dirname $0)/..
cd linters-scripts/

echo "Black Formatting checks"
./black.sh

echo "Flake8 linting checks"
./flake8.sh

echo "Isort import sorting checks"
./isort.sh
