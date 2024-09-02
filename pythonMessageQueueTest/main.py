import os
import subprocess

FILE_PATH = "shared_data.txt"

def run_rust_program():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    rust_binary = os.path.join(current_dir, "../target/debug/task_executor")
    print(f"Running Rust program from: {rust_binary}")

    result = subprocess.run([rust_binary], capture_output=True, text=True)
    print("Rust program output:", result.stdout)
    if result.returncode != 0:
        raise RuntimeError(f"Rust program failed with exit code {result.returncode}")

def read_data_from_file(file_path):
    try:
        with open(file_path, "rb") as file:
            data = file.read()
            print(f"Read data from file '{file_path}'")
            return data
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        raise

def main():
    # Rust 프로그램 실행 (파일에 데이터 쓰기)
    run_rust_program()

    # 데이터 읽기
    try:
        data = read_data_from_file(FILE_PATH)
        print("Read data:", data.decode())
        print("Data length:", len(data))
    except RuntimeError as e:
        print(f"Failed to read data from file: {e}")

if __name__ == "__main__":
    main()
