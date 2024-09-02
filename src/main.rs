use std::io::{self, Write};
use std::thread;
use std::time::Duration;

const DATA_SIZE: usize = 6000;
const CHUNK_SIZE: usize = 4096;

fn main() {
    let data = generate_data();
    send_data(&data);
    thread::sleep(Duration::from_secs(2));
}

fn generate_data() -> String {
    // 6000바이트 크기의 문자열 데이터를 생성합니다.
    let data = "a".repeat(DATA_SIZE);
    data
}

fn send_data(data: &str) {
    let stdout = io::stdout();
    let mut handle = stdout.lock();

    let total_length = data.len();
    handle.write_all(&total_length.to_le_bytes()).unwrap();
    handle.flush().unwrap();

    let mut offset = 0;
    while offset < total_length {
        let end = (offset + CHUNK_SIZE).min(total_length);
        handle.write_all(&data[offset..end].as_bytes()).unwrap();
        handle.flush().unwrap();
        offset += CHUNK_SIZE;
    }
}
