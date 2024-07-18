///Implementing the NEAR Smart Contract
///Tracks Node Creation and defines the Threat Network
/// Struct implemented is a Decentralized Threat Network
/// 
use near_sdk::borsh::{self, BorshDeserialize, BorshSerialize};
use near_sdk::{env, near_bindgen, AccountId};
use near_sdk::collections::{UnorderedMap};
use crate::node::Node;
use crate::summary::ThreatSummary;

#[near_bindgen]
#[derive(BorshDeserialize, BorshSerialize)]
pub struct DecentralizedThreatNetwork {
    nodes: UnorderedMap<AccountId, Node>,
    summaries: UnorderedMap<String, ThreatSummary>,
}

impl Default for DecentralizedThreatNetwork {
    fn default() -> Self {
        Self {
            nodes: UnorderedMap::new(b"n".to_vec()),
            summaries: UnorderedMap::new(b"s".to_vec()),
        }
    }
}

///Submit a new  threat summary
/// Summary ID, Description, Severity, Timestamp
    pub fn submit_summary(&mut self, id: String, description: String, severity: u8, timestamp: u64) {
        let summary = ThreatSummary { id, description, severity, timestamp };
        self.summaries.insert(&summary.id, &summary);
    }

    pub fn get_summaries(&self) -> Vec<ThreatSummary> {
        self.summaries.values().collect()
    }
