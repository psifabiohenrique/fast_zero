from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_html_response_deve_retornar_ok_e_html():
    client = TestClient(app)

    response = client.get('/html')

    assert response.status_code == HTTPStatus.OK
    assert (
        response.text
        == """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Olá mundos</title>
</head>
<body>
    <h1>Olá Mundo!</h1>
    <p> Estamos aprendendo a fazer APIs com FastAPI!</p>
</body>
</html>"""
    )
