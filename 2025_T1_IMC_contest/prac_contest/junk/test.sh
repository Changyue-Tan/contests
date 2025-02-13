#!/bin/bash

# Ensure the user provides the N value as an argument
if [[ -z "$1" ]]; then
    echo "Error: Number of ropes (N) is required as an argument."
    exit 1
fi

# Set test case parameters as variables
N=$1  # Number of ropes (taken from the argument)
MAX_VALUE=$((N * 10))  # Maximum rope length
TARGET=$((RANDOM % 1000000 + 1))  # Random target sum to check for (1 <= T <= 1,000,000)
C_PROGRAM_SOURCE=${2:-"./sample_solution_C.c"}  # C source file (default: sample_solution_C.c)
TEST_PROGRAM="./sample_solution_C"  # Name of the compiled C program to test
LOG_FILE="test_results.log"  # Log file for output and performance results

# Redirect all output to the log file as well as to the terminal
exec > >(tee -a "$LOG_FILE") 2>&1

# Function to compile the C program
compile_c_program() {
    if [[ ! -f "$C_PROGRAM_SOURCE" ]]; then
        echo "Error: Source file $C_PROGRAM_SOURCE does not exist."
        exit 1
    fi

    gcc -Wall -Wextra -Werror -pedantic -Wconversion -Wshadow -Wuninitialized "$C_PROGRAM_SOURCE" -o "$TEST_PROGRAM"
    if [[ $? -ne 0 ]]; then
        echo "Compilation failed."
        exit 1
    fi
    echo "Compilation successful."
}

# Function to generate a random test case with n ropes and a fixed target sum
generate_test_case() {
    local n=$1
    local max_value=$2
    local target=$3

    # Generate unique rope lengths
    ropes=($(shuf -i 1-$max_value -n $n | sort -n))
    echo "$n $target ${ropes[@]}"
}

# Function to run the test case on the C program and measure execution time and memory usage
run_test_case() {
    local n=$1
    local target=$2
    local ropes=($3)

    input_data="$n $target"
    for rope in "${ropes[@]}"; do
        input_data="$input_data $rope"
    done

    # Measure start time
    start_time=$(date +%s%3N)

    # Run the C program and capture output and error
    output=$(echo "$input_data" | /usr/bin/time -v "$TEST_PROGRAM" 2>&1)
    error_code=$?

    # Measure execution time
    end_time=$(date +%s%3N)
    execution_time=$((end_time - start_time))

    # Log to file
    timestamp=$(date +"%Y-%m-%d %H:%M:%S")
    echo "Timestamp: $timestamp"
    echo "Input Parameters:"
    echo "  Number of ropes: $N"
    echo "  Maximum rope length: $MAX_VALUE"
    echo "  Target: $TARGET"
    if [[ $error_code -ne 0 ]]; then
        echo "Error in C program: $output"
    else   
        echo "Output:"
        echo "------------"
        echo "$output"
        echo "------------"
        echo "Execution Time: $execution_time ms"
        echo "Process memory usage: $(echo "$output" | grep 'Maximum resident set size' | awk '{print $6}') bytes"
    fi
    echo "==========================================="
}

# Main script execution
compile_c_program

test_case=$(generate_test_case $N $MAX_VALUE $TARGET)

# Run the test case and measure performance
run_test_case $N $TARGET "$test_case"