import pytest
import requests
from datetime import datetime
from jsonschema import validate

BASE_URL = "https://petstore3.swagger.io/api/v3"

@pytest.fixture(scope="module")
def data_factory():
    def _create_data(data_type):
        if data_type == "pet":
            return requests.post(f"{BASE_URL}/pet", json=payload_pet)
        elif data_type == "order":
            return requests.post(f"{BASE_URL}/store/order", json=payload_order)
        elif data_type == "user":
            return requests.post(f"{BASE_URL}/user", json=payload_user)
        else:
            return "Testidataa ei luotu!"
    return _create_data

def test_add_pet(data_factory):    
    response = data_factory("pet")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == payload_pet["id"]
    assert data["name"] == payload_pet["name"]
    assert data["status"] == payload_pet["status"]

def test_find_pet_by_id(data_factory):
    response = data_factory("pet")
    response = requests.get(f"{BASE_URL}/pet/1")
    assert response.status_code == 200
    validate(instance=response.json(), schema=schema_pet)

def test_add_and_find_order_by_id(data_factory):
    response = data_factory("order")
    assert response.status_code == 200
    response = requests.get(f"{BASE_URL}/store/order/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == payload_order["id"]
    assert data["petId"] == payload_order["petId"]
    assert data["quantity"] == payload_order["quantity"]
    assert data["status"] == payload_order["status"]
    assert data["complete"] == payload_order["complete"]
    
    iso_string = data["shipDate"]
    dt = datetime.fromisoformat(iso_string.replace("Z", "+00:00"))  # Handles timezone
    assert dt.date().isoformat() == payload_order["shipDate"]

def test_create_user(data_factory):
    response = data_factory("user")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == payload_user["id"]
    assert data["username"] == payload_user["name"]
    assert data["firstName"] == payload_user["firstName"]
    assert data["lastName"] == payload_user["lastName"]
    assert data["lastName"] == payload_user["lastName"]
    assert data["password"] == payload_user["password"]
    assert data["phone"] == payload_user["phone"]
    assert data["userStatus"] == payload_user["userStatus"]
   
payload_pet = {
        "id": 1,
        "name": "Fluffy",
        "category": {
            "id": 1,
            "name": "Cats"
        },
        "photoUrls": ["https://example.com/photo.jpg"],
        "tags": [
            {
                "id": 1,
                "name": "cute"
            }
        ],
        "status": "available"
}

payload_order = {
  "id": 1,
  "petId": 1,
  "quantity": 10,
  "shipDate": "2025-08-04",
  "status": "approved",
  "complete": True
}

payload_user = {
  "id": 1,
  "username": "petOwner",
  "firstName": "Paul",
  "lastName": "Owens",
  "email": "paulowens@email.com",
  "password": "12345",
  "phone": "044-1234567",
  "userStatus": 1    
}

schema_pet = {
  "type": "object",
  "required": ["name", "photoUrls"],
  "properties": {
    "id": {
      "type": "integer",
      "format": "int64"
    },
    "category": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "format": "int64"
        },
        "name": {
          "type": "string"
        }
      }
    },
    "name": {
      "type": "string"
    },
    "photoUrls": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "tags": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "format": "int64"
          },
          "name": {
            "type": "string"
          },
           "status": {
                "type": "string",
                "enum": ["available", "pending", "sold"]
            }
        }
        }
    }
    }
}