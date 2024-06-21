from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks/", json={"title": "Nova Tarefa", "description": "Descrição da nova tarefa"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Nova Tarefa"
    assert data["description"] == "Descrição da nova tarefa"
    assert data["status"] == "Pendente"
    assert "id" in data
    assert "created_at" in data
    global created_task_id  # Usar uma variável global para o ID da tarefa criada
    created_task_id = data["id"]

def test_list_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(task["id"] == created_task_id for task in data)

def test_get_task():
    test_create_task()
    response = client.get(f"/tasks/{created_task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == created_task_id
    assert data["title"] == "Nova Tarefa"
    assert data["description"] == "Descrição da nova tarefa"
    assert data["status"] == "Pendente"

def test_update_task():
    test_create_task()
    updated_task = {
        "title": "Tarefa Atualizada",
        "description": "Descrição atualizada",
        "status": "Concluída"
    }
    response = client.put(f"/tasks/{created_task_id}", json=updated_task)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == created_task_id
    assert data["title"] == updated_task["title"]
    assert data["description"] == updated_task["description"]
    assert data["status"] == updated_task["status"]

def test_delete_task():
    test_create_task()
    response = client.delete(f"/tasks/{created_task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == created_task_id
    # Verificar se a tarefa foi realmente deletada
    response = client.get(f"/tasks/{created_task_id}")
    assert response.status_code == 404
