#!/bin/bash

# Test case parameters
N=10  # Number of ropes
MAX_VALUE=100  # Maximum rope length
TARGET=50  # Target sum to check for
TEST_PROGRAM="./rope_pairs"  # Compiled C program

# Generate random test case
generate_test_case() {
    local i
    echo "$N $TARGET"
    for ((i=0; i<N; i++)); do
        echo -n "$((RANDOM % MAX_VALUE + 1)) "
    done
    echo
}

# Run test case and measure execution time and memory
run_test_case() {
    local input_data
    input_data=$(generate_test_case)

    echo "Generated test case:"
    echo "$input_data"

    # Measure time and memory usage
    { time echo "$input_data" | /usr/bin/time -v $TEST_PROGRAM; } 2>&1 | tee result.log
}

run_test_case
