from http import HTTPStatus

from fastapi.testclient import TestClient

from src.fastapi_zero_dunossauro.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # (A)rrange = organização

    response = client.get('/')  # (A)ct = ação

    assert response.status_code == HTTPStatus.OK  # (A)ssert = afirmação
    assert response.json() == {'message': 'Olá mundo'}  # (A)ssert = afirmação
