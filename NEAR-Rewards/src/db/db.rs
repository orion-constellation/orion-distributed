/// # Database Connection
/// ## MongoDB Based
/// 
/// #### Generate your unique URI through the dashboard on Atlas
/// 

use mongodb::{Sync::Client, Sync::Database};
use std::env;
use tokio::

pub fn get_database() -> Database { 
    let mongo_uri = env::var("MONGO_URI").expect("MONGO_URI must be set");
    let client = Client::with_uri_str(mongo_uri).expect("Failed to initialize the client");
    client.database("data_hoover")
}