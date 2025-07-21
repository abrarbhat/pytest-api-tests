def test_auth(auth_token):
    expected_payload = auth_token
    assert expected_payload is not None