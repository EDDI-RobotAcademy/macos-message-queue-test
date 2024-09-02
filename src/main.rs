use std::fs::File;
use std::io::{Write, Result};

const FILE_PATH: &str = "shared_data.txt";
const DATA_SIZE: usize = 6000;

fn write_data_to_file() -> Result<()> {
    let mut file = File::create(FILE_PATH)?;

    let data = vec![b'a'; DATA_SIZE]; // 예시 데이터
    file.write_all(&data)?;

    println!("Data written to file '{}'.", FILE_PATH);
    Ok(())
}

fn main() -> Result<()> {
    write_data_to_file()
}
