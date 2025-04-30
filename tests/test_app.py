from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # (A)ct = ação

    assert response.status_code == HTTPStatus.OK  # (A)ssert = afirmação
    assert response.json() == {'message': 'Olá mundo'}  # (A)ssert = afirmação


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'user name',
            'email': 'useremail@example.com',
            'password': 'passworduser',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'user name',
        'email': 'useremail@example.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'user name',
                'email': 'useremail@example.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'password': 'passworduser',
            'username': 'test2',
            'email': 'test2@example.com',
            'id': 1,
        }
    )

    # assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'test2',
        'email': 'test2@example.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete(
        '/users/1'
    )

    # assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'message': 'User deleted!'
    }
