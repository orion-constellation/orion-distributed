use near_sdk::env::predecessor_account_id;
use near_sdk::{AccountId, MockedBlockchain};
use near_sdk::{testing_env, VMContext};
use crate::DecentralizedThreatNetwork;


fn get_context(predecessor_account_id: AccountId) -> VMContext {
    VMContext {
        current_account_id: "contract".to_string(),
        signer_account_id: predecessor_account_id.clone(),
        predecessor_account_id,
        ..Default::default()

    }
}

#[test]
fn test_register_node() {
    let context = get_context("alice.near".to_string);
    testing_env!(context);
    let mut contract = DecentralizedThreatNetwork::default();
    contract.register_node("node1".to_string(), "192.168.1.1".to_string(), "pubkey".to_string()); 

    let node = contract.nodes.get(&"alice.near".to_string()).unwrap()
    assert_eq!(node.id, "node1") 

}

