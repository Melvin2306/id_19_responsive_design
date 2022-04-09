### testing content ###
### failing tests ###
def test_index_content_fail(client):
    response = client.get('/')
    assert b'this text does not exist' in response.data

### passing tests ###
def test_index_content_success(client):
    response = client.get('/')
    assert b'F.A.Q' in response.data