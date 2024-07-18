///NEAR Node Definition File
///Defining the Data Structures of a Node in the Network
/// A struct Node with fields id, address, public key define the core

use near_sdk::borsh::{self,BorshDeserialize, BorshSerialize};
use near_sdk::serde::{Deserialize, Serialize};
use bson::{BSON, bson}, features::{"uuid-0_8"}
use crypto::aes; 

let key = aes::Key::generate();

#[derive(BorshDeserialize, BorshSerialize, Serialize, Deserialize, Debug, Clone)]
#[serde(crate = "near_sdk::serde")]

pub struct Node {
    pub id: String,
    pub account_id: String,
    pub username: String,
    pub password: String<aes::Key>,
    pub address: String,

    pub public_key: String,
}