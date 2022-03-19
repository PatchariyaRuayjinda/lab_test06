from fastapi.testclient import TestClient
import sys
sys.path.insert(0, "../lab_test06")
from main import app

client = TestClient(app)

def test_post_todo_insert(db):
    response = client.post("/",
        json={
            "name": "string2",
            "description": "idk",
            "completed": "true",
            "date": "15-3-2565"
        }
    )
    assert response.status_code == 200
    assert response.json()[0]["name"] == "string2"
    assert response.json()[0]["description"] == "idk"
    assert response.json()[0]["completed"] == True
    assert response.json()[0]["date"] == "15-3-2565"

def test_put_todo_update(db):
    response = client.put("/622ff5f0bf73eb21b7baf473",
        json={
            "name": "update",
            "description": "idk",
            "completed": "true",
            "date": "15-3-2565"
        }
    )
    assert response.status_code == 200
    assert response.json()[0]["name"] == "update"
    assert response.json()[0]["description"] == "idk"
    assert response.json()[0]["completed"] == True
    assert response.json()[0]["date"] == "15-3-2565"

def test_delete_todo(db):
    response = client.delete("/622ff5f0bf73eb21b7baf473")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}