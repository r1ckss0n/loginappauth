from project import create_app

def test_config():
    assert not create_app().testibg
    assert create_app({'TESTING': True}).testing

def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'