#!/bin/bash

# Hardcoded values
TEST_CASE_DIR="./samples-A2"
SOLUTION="A2"

# Compile the C++ program
g++ "$SOLUTION.cpp" -o "$SOLUTION"

# Run the compiled program for each test case
for input_file in "$TEST_CASE_DIR"/*.in; do
    base_name=$(basename "$input_file" .in)
    expected_output_file="$TEST_CASE_DIR/$base_name.ans"

    # Run the program and compare output
    output=$("./$SOLUTION" < "$input_file")
    expected_output=$(cat "$expected_output_file")

    if [[ "$output" == "$expected_output" ]]; then
        echo "Test case $base_name: PASSED"
    else
        echo "Test case $base_name: FAILED"
        echo "Expected: $expected_output"
        echo "Got: $output"
    fi
done
