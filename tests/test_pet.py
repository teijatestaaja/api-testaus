import requests
from jsonschema import validate

BASE_URL = "https://petstore3.swagger.io/api/v3"
payload = {
        "id": 987654321,
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

def test_add_pet():    
    response = requests.post(f"{BASE_URL}/pet", json=payload)
    assert response.status_code == 200
    
    data = response.json()
    assert data["id"] == payload["id"]
    assert data["name"] == payload["name"]
    assert data["status"] == payload["status"]

def test_find_pet_by_id():
    requests.post(f"{BASE_URL}/pet", json=payload)
    response = requests.get(f"{BASE_URL}/pet/987654321")
    assert response.status_code == 200
    validate(instance=response.json(), schema=schema_pet)
