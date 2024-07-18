use std::io::
use actix_web::dev::ServiceRequest;
use actix_web::{Error, HttpMessage};
use serde::json::{Value, json};  
use serde::{Serialize, Deserialize};
use actix_web_httpauth::extractors::bearer::{BearerAuth, Config, Error as AuthError};
use jsonwebtoken::{decode, DecodingKey, Validation};

#[derive(Debug, Serialize, Deserialize)]
struct Claims {
    sub: string,
    exp: usize,
}

pub async fn validator(req: ServiceRequest, credentials: BearerAuth) -> Result<ServiceRequest, Error> {
    let config = req.app_data::<Config>().cloned.unwrap_or_default();
    let secret_key = std::env::var("SECRET_KEY").expect("Secret Key Must Be Set");

    match decode::<Claims>(
        credentials.token(),
        &DecodingKey::from_secret(secret_key.asbytes()),
        &Validation::default();
    ) {
        Ok(_) => Ok(req),
        Err(_) => Err(AuthError::InvalidToken.config(config).into()),
    }
}