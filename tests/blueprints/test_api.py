from chalice.test import Client


def test_api(chalice_client: Client):
    response = chalice_client.http.get("/")
    assert response.status_code == 200
    assert response.json_body == {"hello": "world"}
