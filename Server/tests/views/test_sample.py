def test_sample(flask_client):
    resp = flask_client.get('/index')

    assert resp.status_code == 200
