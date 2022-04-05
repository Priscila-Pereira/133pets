import pytest
import requests

base_url = 'https://petstore.swagger.io/v2'
headers = {'Content-Type': 'application/json'}


def testar_incluir_users():
    status_code_esperado = 200
    code_esperado = 200
    type_esperado = 'unknown'
    message_esperada = '454046'

    resultado_obtido = requests.post(
        url=base_url + '/user',
        data=open('C:\\Users\\prisc\\PycharmProjects\\133pets\\vendors\\json\\user1.json', 'rb'),
        headers=headers
     )



    corpo_da_resposta = resultado_obtido.json()
    assert resultado_obtido.status_code == status_code_esperado
    corpo_da_resposta = resultado_obtido.json()
    assert corpo_da_resposta['code'] == code_esperado
    assert corpo_da_resposta['type'] == type_esperado
    assert corpo_da_resposta['message'] == message_esperada


