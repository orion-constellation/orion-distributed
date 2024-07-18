use serde::{Deserialize, Serialize};
use bson::{bson, Bson};

#[derive(Clone, Debug, PartialEq, Eq, Deserialize, Serialize)]
pub struct User {
    pub first_name: String,
    pub last_name: String,
    pub username: String,
    pub email: String,
    password: Bson::String
}

#[derive](Clone, PartialEq, Eq, Deser)
pub Struct ThreatAlert {
    
}