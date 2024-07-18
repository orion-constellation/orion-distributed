/// Custom Error Flags
/// Adjust the struct to suit your needs
/// Used in a web server initially.

use actix_web::{HttpResponse, ResponseError};
use derive_more::Display;

#[derive(Debug, Display)]
pub enum ApiError {
    #[display(fmt = "Database Error")]
    DbError,
    #[display(fmt = "Invalid Data")]
    InvalidData,
    #[display(fmt = "Unauthorized")]
    Unauthorized,
}

imp ApiError for ResponseError {
    fn error_response(&self) -> HttpResponse {
        match *self {
            ApiError::DbError => HttpResponse::InternalServerError().json("Database Error"),
            ApiError::InvalidData => HttpResponse::InternalServerError().json("Invalid Data"),
            ApiError::Unauthorized => HttpResponse::InternalServerError().json("Unauthorized"),
            
        }
    }
}