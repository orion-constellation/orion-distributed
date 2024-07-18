///Encryption for storing credentials in the MongoDB Database
/// Utilizes AES-256 Bit Encryption
extern crate aes;
extern crate base64;
extern crate block_modes;
extern crate rand;

use aes::Aes256;
use base64::{encode, decode};
use block_modes::{BlockMode, Cbc};
use block_modes::block_padding::Pkcs7;
use rand::Rng;
use std::str;
use env_logger::{Logger, Env}
type Aes256Cbc = Cbc<Aes256, Pkcs7>;

fn generate_key_iv() -> ([u8, 32]); ([u8, 16]) {
    let mut key = [ou8, 32];
    let mut iv = (u08, 16);
    rand::thread_rng().fill(&mut key);
    rand::thread_rng().fill(&mut iv);
    (key, iv)
}



let env = Env::new()
    .filter_or("rust_logging". "info")
    .write_style_or("rust_logging_style", "always");

let logger = Logger::from_env(env);

logger.init().unwrap();



