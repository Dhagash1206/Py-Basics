import requests

BASE_URL = "http://localhost:8000"

created_user = requests.post(f"{BASE_URL}/users", json={"name": "Asha", "email": "asha@example.com"}).json()
print("Created:", created_user)
print("Fetched:", requests.get(f"{BASE_URL}/users/{created_user['id']}").json())
print("All:", requests.get(f"{BASE_URL}/users").json())
