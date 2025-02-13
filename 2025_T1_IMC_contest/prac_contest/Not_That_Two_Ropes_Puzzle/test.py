import subprocess
import random
import time
import os
import psutil
from typing import Tuple, List
from datetime import datetime

# Set test case parameters as variables
N = 5000  # Number of ropes
MAX_VALUE = N * 10  # Maximum rope length
TARGET = random.randint(1, MAX_VALUE)  # Target sum to check for
C_PROGRAM_SOURCE = "./sample_solution_C.c"  # C source file
TEST_PROGRAM = "./sample_solution_C"  # Name of the compiled C program to test
LOG_FILE = "test_results.log"  # Log file for output and performance results

def compile_c_program(source_file: str, output_file: str) -> None:
    """Compiles the C source file into an executable, with better error handling."""
    if not os.path.exists(source_file):
        print(f"Error: Source file {source_file} does not exist.")
        exit(1)

    compile_command = ["gcc", "-Wall", "-Wextra", "-Werror", "-pedantic", "-Wconversion", "-Wshadow", "-Wuninitialized", source_file, "-o", output_file]

    try:
        subprocess.run(compile_command, check=True)
        print("Compilation successful.")
    except subprocess.CalledProcessError as e:
        print(f"Compilation failed: {e}")
        exit(1)

def generate_test_case(n: int, max_value: int, target: int) -> Tuple[int, int, List[int]]:
    """Generates a random test case with n ropes and a fixed target sum."""
    ropes = [random.randint(1, max_value) for _ in range(n)]
    return n, target, ropes

def run_test_case(n: int, target: int, ropes: List[int]) -> Tuple[str, float, int, float]:
    """Runs the test case on the specified C program and measures execution time and memory usage."""
    input_data = f"{n} {target}\n" + " ".join(map(str, ropes))

    start_time = time.perf_counter()

    # Run the C program and capture output, error
    process = subprocess.Popen(TEST_PROGRAM, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, error = process.communicate(input_data)

    # Check for any errors in the C program
    if error:
        print(f"Error in C program: {error}")
        return "", 0, 0, 0

    execution_time = (time.perf_counter() - start_time) * 1000  # Convert to milliseconds

    # Using psutil to get real-time memory usage of the process
    process_memory = psutil.Process(process.pid).memory_info().rss

    return output.strip(), execution_time, process_memory

def log_results(output: str, exec_time: float, process_mem: float, n: int, max_value: int, target: int) -> None:
    """Logs the results to a file, adding a timestamp for better tracking, and includes test parameters."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"Timestamp: {timestamp}\n")
        log_file.write(f"Test Parameters:\n")
        log_file.write(f"  Number of ropes: {n}\n")
        log_file.write(f"  Maximum rope length: {max_value}\n")
        log_file.write(f"  Target: {target}\n")
        log_file.write(f"Output: {output}\n")
        log_file.write(f"Execution Time: {exec_time:.6f} ms\n")
        log_file.write(f"Process memory usage: {process_mem} bytes\n")
        log_file.write("=" * 40 + "\n")

def main() -> None:
    """Main function to generate a test case, compile the C program, run it, and display the results."""
    # Compile the C program before running the test cases
    compile_c_program(C_PROGRAM_SOURCE, TEST_PROGRAM)

    n, target, ropes = generate_test_case(N, MAX_VALUE, TARGET)

    # Run the test case and measure performance
    output, exec_time, process_mem = run_test_case(n, target, ropes)

    if output:  # If there was no error in running the C program
        print(f"Number of ropes: {N}")
        print(f"Maximum rope length: {MAX_VALUE}")
        print(f"Target: {TARGET}")
        print(f"Output:\n{output}")
        print(f"Execution Time: {exec_time:.6f} ms")
        print(f"Process memory usage: {process_mem} bytes")

        # Log the results, including test parameters
        log_results(output, exec_time, process_mem, N, MAX_VALUE, TARGET)

if __name__ == "__main__":
    main()
