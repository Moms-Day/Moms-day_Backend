from app.models.account import CareWorkerModel


def test_signup_success(flask_client, mongodb_set_for_test, info_test_user):
    resp = flask_client.post(
        '/care/signup',
        json=info_test_user
    )

    # status code 201
    assert resp.status_code == 201

    # Check that if data inserted the database
    assert CareWorkerModel.objects(id=info_test_user['id']).first() is not None


def test_id_duplicated(flask_client, mongodb_set_for_test, info_test_user):
    flask_client.post(
        '/care/signup',
        json=info_test_user
    )

    resp = flask_client.post(
        '/care/signup',
        json=info_test_user
    )

    # status code 409
    assert resp.status_code == 409

    # check message
    assert resp.json['msg'] == 'id duplicated'