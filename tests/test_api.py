def test_raiz_retorna_hello_world(client):
    resposta = client.get('/')
    assert resposta.status_code == 200
    assert resposta.get_data(as_text=True) == 'Hello World 1'


def test_status_retorna_online(client):
    resposta = client.get('/status')
    assert resposta.status_code == 200
    assert resposta.get_json()['status'] == 'online'


def test_tickets_retorna_lista_com_id_e_titulo(client):
    resposta = client.get('/tickets')
    assert resposta.status_code == 200
    tickets = resposta.get_json()
    assert len(tickets) == 3
    assert 'id' in tickets[0]
    assert 'titulo' in tickets[0]


def test_sobre_retorna_nome_e_versao(client):
    resposta = client.get('/sobre')
    assert resposta.status_code == 200
    j = resposta.get_json()
    assert j['nome'] == 'OpsTrack API'
    assert j['versao'] == '1.0.0'


def test_rota_inexistente_retorna_404(client):
    resposta = client.get('/nao-existe')
    assert resposta.status_code == 404
