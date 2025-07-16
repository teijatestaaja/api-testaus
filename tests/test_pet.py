import requests

BASE_URL = "https://petstore3.swagger.io/api/v3"

def test_add_pet():
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

    response = requests.post(f"{BASE_URL}/pet", json=payload)
    assert response.status_code == 200
    
    response_data = response.json()
    assert response_data["id"] == payload["id"]
    assert response_data["name"] == payload["name"]
    assert response_data["status"] == payload["status"]
