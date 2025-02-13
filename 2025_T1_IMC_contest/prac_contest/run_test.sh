#!/bin/bash

# Ensure an argument is provided
if [[ $# -ne 1 ]]; then
    echo "Usage: $0 <Question_name>"
    echo "Example: $0 A1"
    exit 1
fi

# Get the question name from argument
question="$1"

# Directory containing the test cases (always samples-A1)
TEST_CASE_DIR="./samples-$question"

# C program executable (based on question name)
C_PROGRAM="./$question"

# Compile the C program
gcc -Wall -Wextra -Werror -pedantic -Wconversion -Wshadow -Wuninitialized "$question.c" -o "$C_PROGRAM"
if [[ $? -ne 0 ]]; then
    echo "Compilation failed."
    exit 1
fi
echo "Compilation successful."

# Iterate over each .in file in the test case directory
for input_file in "$TEST_CASE_DIR"/*.in; do
    # Get the base name of the test case (without extension)
    base_name=$(basename "$input_file" .in)

    # Corresponding .ans file
    expected_output_file="$TEST_CASE_DIR/$base_name.ans"

    # Ensure the expected output file exists
    if [[ ! -f "$expected_output_file" ]]; then
        echo "Warning: Missing expected output file for test case $base_name"
        continue
    fi

    # Run the C program with the input file and capture the output
    output=$("$C_PROGRAM" < "$input_file")

    # Read the expected output
    expected_output=$(cat "$expected_output_file")

    # Compare the program output with the expected output
    if diff -q <(echo "$output") <(echo "$expected_output") > /dev/null; then
        echo "Test case $base_name: PASSED"
    else
        echo "Test case $base_name: FAILED"
        echo "Expected:"
        echo "$expected_output"
        echo "Got:"
        echo "$output"
    fi
done
