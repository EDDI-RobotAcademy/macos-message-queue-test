import subprocess
import os

CHUNK_SIZE = 4096

def run_rust_binary():
    current_dir = os.getcwd()
    print("Current working directory:", current_dir)

    rust_binary = os.path.join(current_dir, "../target/debug/task_executor")
    env = os.environ.copy()

    # `subprocess.run`을 사용하여 프로세스를 실행하고, 출력을 캡처합니다.
    result = subprocess.run([rust_binary], env=env, stdout=subprocess.PIPE)

    # 프로세스가 종료된 후 출력을 처리합니다.
    return result.stdout

def receive_data(output):
    # 데이터 전체 길이를 먼저 읽습니다.
    total_length_bytes = output[:8]
    total_length = int.from_bytes(total_length_bytes, byteorder='little')

    # 데이터를 청크 단위로 읽습니다.
    received_data = bytearray()
    offset = 8
    while len(received_data) < total_length:
        chunk = output[offset:offset + CHUNK_SIZE]
        received_data.extend(chunk)
        offset += CHUNK_SIZE
        print(f"Received chunk: {len(chunk)} bytes")

    print(f"Total received: {len(received_data)} bytes")
    return received_data.decode('utf-8')

if __name__ == '__main__':
    output = run_rust_binary()
    received_data = receive_data(output)
    print("Received data:", received_data)
