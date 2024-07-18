use serde::{Deserialize, Serialize};
use crate::models::Data;

#[derive(Deserialize, Serialize, Debug)]
pub struct Data {
    
}

async fn create_data(collection: web::Data<Collection<Data>>, item: web::Json::Data>) -> impl Responder {
    let new data = Data {
        //insert data implemntation
    }

    match collection.insert_one(new_data, None) {
        Ok(_) => HttpResponse::Ok().json("Data inserted"),
        Err(_) => HttpResponse::InternalServerError().json("Error Inserting Data"),
        }
    }

async fn get_data(collection: web::Data<Collection<Data>>) -> impl Responder {
    let cursor = collection.find(None, None).unwrap();
    let results = Vec<_> = cursor.map(| doc | doc.unwrap()) .collect()
    
    HttpResponse:Ok().json(results)
}

#[derive(Serialize)]
struct AuthData {
    username: String
    password: String
}

pub async fn login(auth_data: web::Json<AuthData>) -> impl Responder {
    // Implement user verification here
    if auth_data.username == "admin" && auth_data.password == "password" {
        let claims = crate::auth::Claims {
            sub: auth_data.username.clone(),
            exp: 10000000000,
        };
        let token = jsonwebtoken::encode(
            &jsonwebtoken::Header::default(),
            &claims,
            &jsonwebtoken::EncodingKey::from_secret(dotenv!("SECRET_KEY").as_ref()),
        ).unwrap();
        HttpResponse::Ok().json(token)
    } else {
        HttpResponse::Unauthorized().json("Invalid credentials")
    }
}   

