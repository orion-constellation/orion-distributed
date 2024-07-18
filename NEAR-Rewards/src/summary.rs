///NEAR Summary of Threats
///This file declares the data structures for a summary of threats
/// struct Threat Summary
/// 

use near_sdk::borsh::{self, BorshDeserialize, BorshSerialize};
use near_sdk::serde::{Deserialize, Serialize};
use serde_json::{Value, json};

//@TODO Need to define threat schema
#[derive(BorshDeserialize, BorshSerialize, Serialize, Deserialize, Debug, Clone)]
#[serde(crate = "near_sdk::serde")]
pub Struct ThreatSummary {
    pub id: String,
    pub description: String,
    pub severity: u8,
    pub timestamp: u64,
}
